#!/usr/bin/env python3

from genshin import artifact, character, weapon
import click


@click.command()
def main():
    yanfei = character.Character(
        ascension=6,
        level=90,
        constellations=6,
        talent_level_a=10,
        talent_level_e=10,
        talent_level_q=10,
        weapon=weapon.Weapon(
            name=weapon.WeaponName.SkywardAtlas,
            ascension=6,
            level=90,
            refinements=1,
        ),
        artifacts=tuple(
            artifact.parse_artifact(a)
            for a in (
                "CW@1@20 HP=4780 EM=23 CD%=18.7 ATK=37 CR%=11.7",
                "CW@2@20 ATK=311 CR%=9.7 EM=56 CD%=7.8 ER%=4.5",
                "CW@3@20 EM=187 CR%=12.4 ATK=19 CD%=13.2 ER%=6.5",
                "LW@4@20 EDP%=46.6 CD%=12.4 HP=448 CR%=10.1 EM=23",
                "CW@5@20 CR%=31.1 CD%=33.4 HP=209 ATK=18 DEF%=5.8",
            )
        ),
    )


if __name__ == "__main__":
    main()
