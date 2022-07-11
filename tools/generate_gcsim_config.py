#!/usr/bin/env python3

import pathlib
from genshin import character, gcsim, weapon
import click


@click.command()
@click.argument("rotation_file", type=pathlib.Path)
def main(rotation_file: pathlib.Path) -> None:
    weapons = weapon.load_weapon_list("data/weapons.txt")
    characters = character.load_character_list("data/characters.txt", weapons=weapons)

    with open(rotation_file) as f:
        rotation = f.read() + "\n"

    print(
        gcsim.generate_gcsim_config(
            [
                characters[character.CharacterName.Xingqiu],
                characters[character.CharacterName.Yanfei],
                characters[character.CharacterName.Kazuha],
                characters[character.CharacterName.Bennett],
            ],
            actions=[rotation],
            target="target lvl=90 resist=0.1;",
        )
    )


if __name__ == "__main__":
    main()
