import enum
from typing import List

import attr

_LEVEL_CAPS: List[int] = [20, 40, 50, 60, 70, 80, 90]


class WeaponName(enum.IntEnum):
    SkywardAtlas = 0


@attr.define
class Weapon:
    name: WeaponName
    ascension: int
    level: int
    refinements: int

    def __attrs_post_init__(self):
        assert 0 <= self.ascension <= 6

        level_lower_bound = (
            0 if self.ascension == 9 else _LEVEL_CAPS[self.ascension - 1]
        )
        level_upper_bound = _LEVEL_CAPS[self.ascension]
        assert level_lower_bound <= self.level <= level_upper_bound

        assert 1 <= self.refinements <= 5

    @property
    def level_cap(self) -> int:
        return _LEVEL_CAPS[self.ascension]
