# Genshin Version Upgrade — Packet Capture Data Import

Use this skill when a new Genshin Impact version releases and you need to
import account data (artifacts, weapons, characters) from a freshly captured
`.pcap` into the dataset.

The game changes **opcode values (cmd IDs)** and **protobuf field numbers**
every version due to obfuscation.  The `_infer_xor_key` method in
`genshin/packet/session.py` is now opcode-independent, so the main work is
updating proto field numbers and lookup-table data.

## Prerequisites

- A packet capture in `captures/` (both LAN and SLL2 variants are fine).
- The C extension built: `cd cpython_extensions && cmake -B build && cmake --build build`
- `grpcio-tools` installed (for proto compilation matching the protobuf runtime).
- Know your approximate in-game ping (e.g. ~150 ms) — used as a sanity check.

## Step-by-step

### 1. Infer the XOR key (automatic)

The key inference in `session.py` is version-independent.  It:
1. Derives `key[0:2]` from the dispatch magic `\x45\x67`.
2. Derives `key[4:12]` from empty (length-12 heartbeat) packets.
3. Derives additional bytes from `\x89\xab` trailers of various-length packets.
4. Uses RTT (ping) packets — identified by having exactly **one** varying
   byte — to fill remaining gaps via the protobuf varint continuation byte.
5. Brute-forces the remaining unknown bytes (typically just `key[2:4]`, the
   opcode field) through `find_seed`.

**You usually do not need to touch this.**  If it fails:
- Check that the capture has heartbeat packets (length-12) and periodic RTT
  packets.  Short captures may lack these.
- Increase the brute-force limit in `_infer_xor_key` if > 3 key bytes are
  unknown.

### 2. Decrypt all packets and identify new opcodes

```python
from genshin.packet import session
s = session.Session('captures/<new-capture>.pcap')
for p in s.get_decrypted_packets():
    # p.raw_opcode, p.data, p.direction
```

Use a raw protobuf wire-format decoder to examine top-level fields of large
received packets.  Look for:

| Message               | How to identify                                  |
|-----------------------|--------------------------------------------------|
| `PlayerStoreNotify`   | Huge packet (>100 KB), has `store_type` varint=1 (STORE_PACK) and a repeated `Item` list |
| `AvatarDataNotify`    | Medium-large packet, repeated entries with valid `avatar_id` (100000XX) |

### 3. Determine changed proto field numbers

Decode the raw protobuf wire format (tag = `field_number << 3 | wire_type`)
of the top-level message and compare against the current `.proto` file in
`resources/proto/`.  Only the **top-level container** messages tend to change
field numbers; nested messages (`Item`, `Equip`, `Weapon`, `Reliquary`,
`AvatarInfo`, `PropValue`) are typically stable.

In 6.7 the changes were:
- `PlayerStoreNotify`: `store_type` 10→1, `item_list` 3→2, `weight_limit` 8→12
- `AvatarDataNotify`: `avatar_list` 2→14

Update the `.proto` files, then rebuild:
```bash
bash tools/build_proto.sh   # uses grpc_tools.protoc for version matching
```

### 4. Update opcodes

Update `genshin/packet/opcodes.py` with the new cmd IDs identified in step 2.
Only the opcodes used by the importer need to be correct:
- `PlayerStoreNotify`
- `AvatarDataNotify`
- (`WorldPlayerRTTNotify` and `PlayerLoginReq` are no longer needed for key
  inference but are kept for reference.)

### 5. Update game data lookup tables

New artifacts, weapons, and characters need entries in:
- `genshin/formats/official.py`: `_SET_NAME_MAPPING`, `_WEAPON_NAME_MAPPING`,
  `_CHARACTER_NAME_MAPPING`
- `resources/excel_bin_output/`: updated JSON dumps from the game data

### 6. Update level caps if the max level changed

Check `genshin/character.py` `_LEVEL_CAPS`.  If characters can exceed 90,
update accordingly (e.g. 6.7 raised the cap to 100).

### 7. Run the importer

```bash
PYTHONPATH=. python3 bin/account_data_importer.py captures/<new-capture>.pcap --verbose
```

Verify `data/artifacts.txt`, `data/weapons.txt`, `data/characters.txt`.

### 8. Verify with packet_parser (optional)

```bash
PYTHONPATH=. python3 bin/packet_parser.py captures/<new-capture>.pcap
```

## Key files

| File | Purpose |
|------|---------|
| `genshin/packet/session.py` | KCP reassembly, XOR key inference, packet decryption |
| `genshin/packet/opcodes.py` | Cmd ID enum (version-specific) |
| `resources/proto/` | Proto definitions (version-specific field numbers) |
| `genshin/packet/proto/` | Compiled Python protos (generated, git-tracked) |
| `genshin/formats/official.py` | Data parsing + lookup tables |
| `tools/build_proto.sh` | Proto compilation script |
| `cpython_extensions/` | C extension for MT64 seed search |
