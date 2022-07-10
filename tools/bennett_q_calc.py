def calc(
    *,
    bennett_character_atk,
    bennett_weapon_atk,
    bennett_q_ratio,
    buffed_character_base_atk,
    buffed_character_regular_total_atk,
):
    atk = buffed_character_regular_total_atk
    atk += (bennett_character_atk + bennett_weapon_atk) * bennett_q_ratio

    return atk + buffed_character_base_atk * 0.2, atk


BENNETT_CHARACTER_ATK_80A = 178

BENNETT_WEAPON_ATK_FAVONIOUS = 454
BENNETT_WEAPON_ATK_AQUILA = 674

curr_no4, curr = calc(
    bennett_character_atk=BENNETT_CHARACTER_ATK_80A,
    bennett_weapon_atk=BENNETT_WEAPON_ATK_FAVONIOUS,
    bennett_q_ratio=0.9 + 0.2,
    buffed_character_base_atk=914,
    buffed_character_regular_total_atk=2237,
)

target_no4, target = calc(
    bennett_character_atk=BENNETT_CHARACTER_ATK_80A,
    bennett_weapon_atk=BENNETT_WEAPON_ATK_FAVONIOUS,
    bennett_q_ratio=0.95 + 0.2,
    buffed_character_base_atk=914,
    buffed_character_regular_total_atk=2237,
)


print(int(curr_no4), int(curr))
print(int(target_no4), int(target))
print(f"{target_no4/curr_no4:.2f} {target/curr:.2f}")
