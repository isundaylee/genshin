#include <cstdint>
#include <cstdio>
#include <cstring>

#include <optional>
#include <vector>

#include <nanobind/nanobind.h>
#include <nanobind/stl/optional.h>

////////////////////////////////////////////////////////////////////////////////
/// Utils

void print_uint64(const char *name, uint64_t v) {
  printf("%-20s: %016llX\n", name, v);
}

////////////////////////////////////////////////////////////////////////////////
/// Bit-op utils

uint64_t select(uint64_t v, uint64_t l, uint64_t r) {
  // MSB              LSB
  //   ................
  //           r    l

  return (v >> l) & ((1ULL << (r - l)) - 1ULL);
}

/*
 * Return a 64-bit number obtained by:
 *
 * LSB                                                            MSB
 *   ... a_bits MS bits of a ... ... (64 - a_bits) LS bits of b ...
 */
uint64_t select_adj(uint64_t a, uint64_t b, uint64_t a_bits) {
  return ((select(b, 0, 64 - a_bits) << a_bits) + select(a, 64 - a_bits, 64));
}

/*
 * Return a 64-bit number obtained by:
 *
 * LSB                                                            MSB
 *   ... a_bits LS bits of a ... ... (64 - a_bits) MS bits of b ...
 */
uint64_t select_mask(uint64_t a, uint64_t b, uint64_t a_bits) {
  return (select(a, 0, a_bits) + (select(b, a_bits, 64) << a_bits));
}

////////////////////////////////////////////////////////////////////////////////
/// MT64 utils

uint64_t mt64_init_scramble(uint64_t mti, uint64_t x) {
  x ^= x >> 62;
  x *= 6364136223846793005ULL;
  x += mti;
  return x;
}

uint64_t mt64_init_unscramble(uint64_t mti, uint64_t x) {
  x -= mti;
  x *= 13877824140714322085ULL;
  x ^= x >> 62;
  return x;
}

/*
 * x: mt[(mti - 1)@n : mti@n]
 *
 * gives mt[mti - 1]
 */
uint64_t mt64_init_unscramble_adj(uint64_t mti, uint64_t x, uint64_t n) {
  uint64_t tmp = ((x - mti) * 13877824140714322085ULL) ^ (x >> 62ULL);
  uint64_t mask = (1ULL << n) - 1ULL;
  return (x & ~mask) | (tmp & mask);
}

uint64_t mt64_generate_scramble(uint64_t x) {
  return ((x & 1) ? 13043109905998158313ULL : 0ULL) ^ (x >> 1);
}

uint64_t mt64_generate_unscramble(uint64_t x) {
  return ((x >> 63) ? 7639475738286765011ULL : 0ULL) ^ (x << 1);
}

uint64_t mt64_output_scramble(uint64_t x) {
  x ^= (x >> 29) & 22906492245ULL;
  x ^= (x & 62583042209491ULL) << 17;       // This step is not an involution
  x ^= (x & 18446744073709535095ULL) << 37; // same as 134201207ULL
  x ^= x >> 43;
  return x;
}

uint64_t mt64_output_unscramble(uint64_t x) {
  x ^= x >> 43;
  x ^= (x & 18446744073709535095ULL) << 37; // same as 134201207ULL
  x ^= (x & 62583042209491ULL) << 17;
  x ^= (x & 477468371ULL) << 34;
  x ^= (x >> 29) & 22906492245ULL;
  return x;
}

////////////////////////////////////////////////////////////////////////////////
/// MT64 impl

class MT64 {
public:
  MT64(uint64_t seed) {
    mt[0] = seed;
    for (mti = 1; mti < 312; mti++) {
      mt[mti] = mt64_init_scramble(mti, mt[mti - 1]);
    }
  }

  uint64_t generate() {
    if (mti >= 312) {
      for (uint64_t i = 312; i < 312 * 2; i++) {
        mt[i] = mt64_generate_scramble(
                    select_mask(mt[i - 312 + 1], mt[i - 312], 31)) ^
                mt[i - 156];
      }

      memcpy(mt, mt + 312, sizeof(mt[0]) * 312);
      mti = 0;
    }

    return mt64_output_scramble(mt[mti++]);
  }

  uint64_t get_mt(uint64_t mti) { return mt[mti]; }

private:
  uint64_t mt[312 * 2];
  uint64_t mti;
};

////////////////////////////////////////////////////////////////////////////////
/// Seed search impl

void search_seed(uint64_t cur_mt1, uint64_t cur_mt157, uint64_t n,
                 uint64_t top_mt2, uint64_t exp_mt313, uint64_t exp_mt314,
                 std::vector<uint64_t> &output) {
  if (n == 62) {
    const uint64_t seed = mt64_init_unscramble(1, cur_mt1);
    output.push_back(seed);
    return;
  }

  // Comment after each variable shows which bits are valid. The other bits are
  // unknown.

  for (uint64_t bit_mt1 = 0; bit_mt1 < 2; bit_mt1++) {
    for (uint64_t bit_mt157 = 0; bit_mt157 < 2; bit_mt157++) {
      uint64_t next_mt1 = cur_mt1 + (bit_mt1 << n);       // 0..n + 63 + 64
      uint64_t next_mt157 = cur_mt157 + (bit_mt157 << n); // 0..n + 63 + 64

      uint64_t guess_mt2 = select(mt64_init_scramble(2, next_mt1), 0, 62) +
                           (top_mt2 << 62ULL);               // 0..n + 63 + 64
      uint64_t guess_mt3 = mt64_init_scramble(3, guess_mt2); // 0..n
      uint64_t guess_mt158 = mt64_init_scramble(158, next_mt157); // 0..n
      uint64_t guess_mt313 =
          mt64_generate_scramble(select_mask(guess_mt2, next_mt1, 31)) ^
          next_mt157; // 0..n-1
      uint64_t guess_mt314 =
          mt64_generate_scramble(select_mask(guess_mt3, guess_mt2, 31)) ^
          guess_mt158; // 0..n-1

      const bool valid = [=] {
        if (n == 0) {
          return true;
        }

        if (n < 61) {
          return ((select(guess_mt313, 0, n) == select(exp_mt313, 0, n)) &&
                  (select(guess_mt314, 0, n) == select(exp_mt314, 0, n)));
        }

        return (guess_mt313 == exp_mt313) && (guess_mt314 == exp_mt314) &&
               (mt64_init_scramble(2, next_mt1) == guess_mt2);
      }();

      if (valid) {
        search_seed(next_mt1, next_mt157, n + 1, top_mt2, exp_mt313, exp_mt314,
                    output);
      }
    }
  }
}

std::optional<uint64_t> find_seed(uint64_t key0, uint64_t key1) {
  std::vector<uint64_t> potential_seeds;

  for (uint64_t top_mt1 = 0; top_mt1 < 4; top_mt1++) {
    for (uint64_t top_mt2 = 0; top_mt2 < 4; top_mt2++) {
      for (uint64_t top_mt157 = 0; top_mt157 < 4; top_mt157++) {
        search_seed((top_mt1 << 62ULL), (top_mt157 << 62UL), 0, top_mt2,
                    mt64_output_unscramble(key0), mt64_output_unscramble(key1),
                    potential_seeds);
      }
    }
  }

  for (const auto seed : potential_seeds) {
    MT64 mt64(seed);
    mt64.generate();
    uint64_t test_key0 = mt64.generate();
    uint64_t test_key1 = mt64.generate();

    if ((test_key0 == key0) && (test_key1 == key1)) {
      return seed;
    }
  }

  return std::nullopt;
}

////////////////////////////////////////////////////////////////////////////////
/// Nanobind

namespace nb = nanobind;

NB_MODULE(genshin_xor_key, m) {
  m.def("find_seed", &find_seed);

  nb::class_<MT64>(m, "MT64")
      .def(nb::init<uint64_t>())
      .def("generate", &MT64::generate);
}
