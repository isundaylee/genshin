def get_expected_damage(dmg_when_crit, crit_rate, crit_dmg):
    return dmg_when_crit * (
        1.0 * crit_rate + (1.0 / (1.0 + crit_dmg)) * (1 - crit_rate)
    )


print(
    get_expected_damage(
        31786,
        0.431 + 0.12,
        1.394,
    )
)
