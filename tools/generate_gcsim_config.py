#!/usr/bin/env python3

import pathlib
from typing import List
from genshin import character, gcsim, weapon
import click


@click.command()
@click.argument("rotation_file", type=pathlib.Path)
def main(rotation_file: pathlib.Path) -> None:
    weapons = weapon.load_weapon_list("data/weapons.txt")
    characters = character.load_character_list("data/characters.txt", weapons=weapons)

    with open(rotation_file) as f:
        header = next(f)
        _, team_str = header.strip().split("# team=")
        team = [character.CharacterName[c] for c in team_str.split(",")]

        rotation = f.read()

    print(
        gcsim.generate_gcsim_config(
            [characters[c] for c in team],
            actions=[rotation],
            target="target lvl=90 resist=0.1;",
        )
    )


if __name__ == "__main__":
    main()
