from __future__ import annotations

import pathlib
from genshin import artifact, character, weapon
from typing import Dict, Iterable, List, Optional
import attr


@attr.define
class Account:
    characters: Dict[character.CharacterName, character.Character]
    weapons: Dict[str, weapon.Weapon]
    artifacts: List[artifact.Artifact]

    @staticmethod
    def load(path: pathlib.Path) -> Account:
        weapons = load_weapon_list(path / "weapons.txt")
        characters = load_character_list(path / "characters.txt", weapons=weapons)
        artifacts = list(load_artifacts(path / "artifacts.txt"))

        return Account(characters=characters, weapons=weapons, artifacts=artifacts)

    def apply_overrides(self, overrides: str) -> None:
        for o in overrides.split(","):
            k, v = o.split("=")
            c, key = k.split(".")

            ch = self.characters[character.CharacterName[c]]

            if key == "weapon":
                ch.weapon = self.weapons[v]
            else:
                raise ValueError(f"Invalid key {key}")


def load_artifacts(path: pathlib.Path) -> Iterable[artifact.Artifact]:
    with open(path) as f:
        for line in f:
            line = line.strip()

            if (not line) or line.startswith("#"):
                continue

            yield artifact.parse_artifact(line)


def load_weapon_list(path: pathlib.Path) -> Dict[str, weapon.Weapon]:
    weapons: Dict[str, weapon.Weapon] = {}
    with open(path) as f:
        for line in f.read().splitlines():
            if (not line) or line.startswith("#"):
                continue

            name, value = line.split("=")
            wp_name, ascension, level, refinements = value.split("/")

            weapons[name] = weapon.Weapon(
                name=weapon.WeaponName[wp_name],
                ascension=int(ascension),
                level=int(level),
                refinements=int(refinements),
            )

    return weapons


def load_character_list(
    path: pathlib.Path, *, weapons: Dict[str, weapon.Weapon]
) -> Dict[character.CharacterName, character.Character]:
    characters: Dict[character.CharacterName, character.Character] = {}

    pending_profile_line: Optional[str] = None
    pending_artifacts: List[artifact.Artifact] = []

    def build_character() -> None:
        nonlocal pending_profile_line, pending_artifacts

        assert pending_profile_line is not None
        name, asc, lv, cons, tla, tle, tlq, wp = pending_profile_line.split("/")
        return character.Character(
            name=character.CharacterName[name],
            ascension=int(asc),
            level=int(lv),
            constellations=int(cons),
            talent_level_a=int(tla),
            talent_level_e=int(tle),
            talent_level_q=int(tlq),
            weapon=weapons[wp],
            artifacts=pending_artifacts,
        )

    with open(path) as f:
        for line in f:
            line = line.strip()

            if (not line) or line.startswith("#"):
                continue

            if line.startswith("@"):
                if pending_profile_line is not None:
                    ch = build_character()
                    characters[ch.name] = ch
                    pending_profile_line = None
                    pending_artifacts = []

                pending_profile_line = line[1:]
            else:
                pending_artifacts.append(artifact.parse_artifact(line))

    ch = build_character()
    characters[ch.name] = ch

    return characters
