from __future__ import annotations
import pathlib

from genshin import artifact, weapon, character
from typing import Dict, List, Optional, Tuple
import enum
import collections
import attr


_LEVEL_CAPS: List[int] = [20, 40, 50, 60, 70, 80, 90]


class CharacterName(enum.IntEnum):
    Yanfei = 0
    Kazuha = 1
    Bennett = 2
    Xingqiu = 3


@attr.define
class Character:
    name: CharacterName

    ascension: int
    level: int
    constellations: int

    # These do NOT include the +3s from constellations
    talent_level_a: int
    talent_level_e: int
    talent_level_q: int

    weapon: weapon.Weapon
    artifacts: Tuple[
        artifact.Artifact,
        artifact.Artifact,
        artifact.Artifact,
        artifact.Artifact,
        artifact.Artifact,
    ]

    def __attrs_post_init__(self):
        assert 0 <= self.ascension <= 6

        level_lower_bound = (
            0 if self.ascension == 9 else _LEVEL_CAPS[self.ascension - 1]
        )
        level_upper_bound = _LEVEL_CAPS[self.ascension]
        assert level_lower_bound <= self.level <= level_upper_bound

        assert 1 <= self.talent_level_a <= 10
        assert 1 <= self.talent_level_e <= 10
        assert 1 <= self.talent_level_q <= 10

        assert len(self.artifacts) == 5
        assert self.artifacts[0].artifact_slot == artifact.ArtifactSlot.Flower
        assert self.artifacts[1].artifact_slot == artifact.ArtifactSlot.Feather
        assert self.artifacts[2].artifact_slot == artifact.ArtifactSlot.Sand
        assert self.artifacts[3].artifact_slot == artifact.ArtifactSlot.Cup
        assert self.artifacts[4].artifact_slot == artifact.ArtifactSlot.Circlet

    @property
    def level_cap(self) -> int:
        return _LEVEL_CAPS[self.ascension]

    @property
    def base_hp(self) -> int:
        pass

    @property
    def combined_artifact_stats(self) -> Dict[artifact.ArtifactStatType, float]:
        stats = collections.defaultdict(lambda: 0.0)
        for a in self.artifacts:
            for s in [a.main_stat] + a.sub_stats:
                stats[s.stat_type] += s.stat_value
        return stats


def load_character_list(
    path: pathlib.Path, *, weapons: Dict[str, weapon.Weapon]
) -> Dict[CharacterName, Character]:
    characters: Dict[CharacterName, Character] = {}

    pending_profile_line: Optional[str] = None
    pending_artifacts: List[artifact.Artifact] = []

    def build_character() -> None:
        nonlocal pending_profile_line, pending_artifacts

        assert pending_profile_line is not None
        name, asc, lv, cons, tla, tle, tlq, wp = pending_profile_line.split("/")
        return Character(
            name=CharacterName[name],
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
