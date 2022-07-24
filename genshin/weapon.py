from __future__ import annotations

import enum
from typing import Dict, List, Tuple

import attr

_LEVEL_CAPS: List[int] = [20, 40, 50, 60, 70, 80, 90]


class WeaponName(enum.IntEnum):
    SkywardAtlas = 0
    IronSting = 1
    FavoniusSword = 2
    FavoniusLance = 3
    SacrificialSword = 4
    TheWidsith = 5
    AquilaFavonia = 6
    LostPrayerToTheSacredWinds = 7
    MemoryOfDust = 8
    PrimordialJadeWingedSpear = 9
    TheCatch = 10
    KagurasVerity = 11
    ThrillingTalesOfDragonSlayers = 12
    FreedomSworn = 13
    TheViridescentHunt = 14
    TheStringless = 15


_BASE_STATS: Dict[Tuple[WeaponName, int, int], Tuple[int]] = {
    (WeaponName.SkywardAtlas, 6, 90): (674,),
}


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

    @property
    def base_atk(self) -> int:
        return _BASE_STATS[(self.name, self.ascension, self.level)][0]
