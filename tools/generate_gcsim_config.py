#!/usr/bin/env python3

from genshin import artifact, character, gcsim, weapon
import click


@click.command()
def main():
    yanfei = character.Character(
        name=character.CharacterName.Yanfei,
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

    kazuha = character.Character(
        name=character.CharacterName.Kazuha,
        ascension=6,
        level=80,
        constellations=0,
        talent_level_a=6,
        talent_level_e=6,
        talent_level_q=6,
        weapon=weapon.Weapon(
            name=weapon.WeaponName.IronSting,
            ascension=6,
            level=90,
            refinements=1,
        ),
        artifacts=tuple(
            artifact.parse_artifact(a)
            for a in (
                "VV@1@20 HP=4780 ATK=35 CR%=15.5 EM=35 DEF=16",
                "VV@2@20 ATK=311 ER%=5.8 CD%=26.4 HP=448 EM=47",
                "VV@3@20 EM=187 ER%=16.2 DEF%=5.1 ATK%=13.4 ATK=16",
                "TF@4@20 EM=187 ATK=47 HP=508 CD%=14.8 ATK%=5.8",
                "VV@5@20 EM=187 DEF%=7.3 CR%=18.8 HP=598 ATK%=11.1",
            )
        ),
    )

    print(
        gcsim.generate_gcsim_config(
            [yanfei, kazuha],
            actions=[
                "options mode=sl;",
                "yanfei attack:1;",
                "kazuha skill;",
                "yanfei attack:1,skill,attack:1,charge,attack:3,charge,attack:1,charge,attack:3,charge,attack:1,skill,charge;",
                "restart;",
            ],
            target="target lvl=88 resist=0.1;",
        )
    )


if __name__ == "__main__":
    main()
