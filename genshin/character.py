from __future__ import annotations

from genshin import artifact, weapon, character
from typing import Dict, List, Tuple
import enum
import collections
import attr


_LEVEL_CAPS: List[int] = [20, 40, 50, 60, 70, 80, 90]


class CharacterName(enum.IntEnum):
    Yanfei = 0
    Kazuha = 1
    Bennett = 2


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
