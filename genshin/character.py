from genshin import artifact, weapon
from typing import List, Tuple
import attr


_LEVEL_CAPS: List[int] = [20, 40, 50, 60, 70, 80, 90]


@attr.define
class Character:
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
