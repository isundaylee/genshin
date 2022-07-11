#!/usr/bin/env python3

import pathlib
from genshin import artifact, character, gcsim, weapon
import click


@click.command()
@click.argument("rotation_file", type=pathlib.Path)
def main(rotation_file: pathlib.Path) -> None:
    weapons = weapon.load_weapon_list("data/weapons.txt")

    yanfei = character.Character(
        name=character.CharacterName.Yanfei,
        ascension=6,
        level=90,
        constellations=6,
        talent_level_a=10,
        talent_level_e=10,
        talent_level_q=10,
        weapon=weapons["skyward_atlas"],
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
        weapon=weapons["iron_sting"],
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

    bennett = character.Character(
        name=character.CharacterName.Bennett,
        ascension=6,
        level=80,
        constellations=5,
        talent_level_a=1,
        talent_level_e=1,
        talent_level_q=9,
        weapon=weapons["favonius_sword"],
        artifacts=tuple(
            artifact.parse_artifact(a)
            for a in (
                "MB@1@20 HP=4780 ER%=11.7 CR%=14 CD%=16.2 EM=16",
                "NO@2@20 ATK=311 DEF=35 CD%=7.0 EM=35 ER%=17.5",
                "NO@3@20 ER%=51.8 CR%=6.2 CD%=17.9 DEF=19 DEF%=13.1",
                "NO@4@20 HP%=46.6 ER%=10.4 ATK=60 CR%=3.1 EM=21",
                "NO@5@20 CR%=31.1 ER%=9.7 EM=40 CD%=11.7 ATK=49",
            )
        ),
    )

    xingqiu = character.Character(
        name=character.CharacterName.Xingqiu,
        ascension=6,
        level=80,
        constellations=6,
        talent_level_a=1,
        talent_level_e=8,
        talent_level_q=8,
        weapon=weapons["sacrificial_sword"],
        artifacts=tuple(
            artifact.parse_artifact(a)
            for a in (
                "HD@1@20 HP=4780 ATK%=14.0 ER%=11.0 CR%=6.2 ATK=14",
                "NO@2@20 ATK=311 HP%=4.1 CR%=9.7 DEF%=13.9 CD%=15.5",
                "NO@3@20 ATK%=46.6 CR%=9.3 DEF=21 ER%=10.4 DEF%=11.7",
                "CW@4@20 EDH%=46.6 HP%=11.1 CD%=7.0 ATK%=9.9 ER%=20.7",
                "HD@5@20 CR%=31.1 CD%=13.2 DEF=21 ATK%=18.1 HP=269",
            )
        ),
    )

    with open(rotation_file) as f:
        rotation = f.read() + "\n"

    print(
        gcsim.generate_gcsim_config(
            [xingqiu, yanfei, kazuha, bennett],
            actions=[rotation],
            target="target lvl=90 resist=0.1;",
        )
    )


if __name__ == "__main__":
    main()
