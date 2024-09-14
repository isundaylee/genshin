from __future__ import annotations

from genshin import account, artifact
from typing import Dict, List, Tuple
import enum
import collections
import attr


_LEVEL_CAPS: List[int] = [20, 40, 50, 60, 70, 80, 90]


class CharacterName(enum.IntEnum):
    """Character name following the GOOD format.

    See https://frzyc.github.io/genshin-optimizer/#/doc/CharacterKey
    """

    KamisatoAyaka = enum.auto()
    Jean = enum.auto()
    Traveler = enum.auto()
    Lisa = enum.auto()
    Barbara = enum.auto()
    Kaeya = enum.auto()
    Diluc = enum.auto()
    Razor = enum.auto()
    Amber = enum.auto()
    Venti = enum.auto()
    Xiangling = enum.auto()
    Beidou = enum.auto()
    Xingqiu = enum.auto()
    Xiao = enum.auto()
    Ningguang = enum.auto()
    Klee = enum.auto()
    Zhongli = enum.auto()
    Fischl = enum.auto()
    Bennett = enum.auto()
    Tartaglia = enum.auto()
    Noelle = enum.auto()
    Qiqi = enum.auto()
    Chongyun = enum.auto()
    Ganyu = enum.auto()
    Albedo = enum.auto()
    Diona = enum.auto()
    Mona = enum.auto()
    Keqing = enum.auto()
    Sucrose = enum.auto()
    Xinyan = enum.auto()
    Rosaria = enum.auto()
    HuTao = enum.auto()
    KaedeharaKazuha = enum.auto()
    Yanfei = enum.auto()
    Yoimiya = enum.auto()
    Thoma = enum.auto()
    Eula = enum.auto()
    RaidenShogun = enum.auto()
    Sayu = enum.auto()
    SangonomiyaKokomi = enum.auto()
    Gorou = enum.auto()
    KujouSara = enum.auto()
    AratakiItto = enum.auto()
    YaeMiko = enum.auto()
    ShikanoinHeizo = enum.auto()
    Yelan = enum.auto()
    Kirara = enum.auto()
    Aloy = enum.auto()
    Shenhe = enum.auto()
    YunJin = enum.auto()
    KukiShinobu = enum.auto()
    KamisatoAyato = enum.auto()
    Collei = enum.auto()
    Dori = enum.auto()
    Tighnari = enum.auto()
    Nilou = enum.auto()
    Cyno = enum.auto()
    Candace = enum.auto()
    Nahida = enum.auto()
    Layla = enum.auto()
    Wanderer = enum.auto()
    Faruzan = enum.auto()
    Yaoyao = enum.auto()
    Alhaitham = enum.auto()
    Dehya = enum.auto()
    Mika = enum.auto()
    Kaveh = enum.auto()
    Baizhu = enum.auto()
    Lynette = enum.auto()
    Lyney = enum.auto()
    Freminet = enum.auto()
    Wriothesley = enum.auto()
    Neuvillette = enum.auto()
    Charlotte = enum.auto()
    Furina = enum.auto()
    Chevreuse = enum.auto()
    Navia = enum.auto()
    Gaming = enum.auto()
    Xianyun = enum.auto()
    Chiori = enum.auto()
    Sigewinne = enum.auto()
    Arlecchino = enum.auto()
    Sethos = enum.auto()
    Clorinde = enum.auto()
    Emilie = enum.auto()
    Kachina = enum.auto()
    Mualani = enum.auto()


_BASE_STATS: Dict[Tuple[CharacterName, int, int], Tuple[int, int, int]] = {
    (CharacterName.Yanfei, 6, 90): (9352, 240, 587),
}


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
        return _BASE_STATS[(self.name, self.ascension, self.level)][0]

    @property
    def base_atk(self) -> int:
        return _BASE_STATS[(self.name, self.ascension, self.level)][1]

    @property
    def base_atk_with_weapon(self) -> int:
        return self.base_atk + self.weapon.base_atk

    @property
    def base_def(self) -> int:
        return _BASE_STATS[(self.name, self.ascension, self.level)][2]

    @property
    def combined_artifact_stats(self) -> Dict[artifact.ArtifactStatType, float]:
        stats = collections.defaultdict(lambda: 0.0)
        for a in self.artifacts:
            for s in [a.main_stat] + a.sub_stats:
                stats[s.stat_type] += s.stat_value
        return stats

    def to_string(self, weapon_map: Dict[str, weapon.Weapon]) -> str:
        weapon_name = None
        for name, weapon in weapon_map.items():
            if weapon == self.weapon:
                weapon_name = name
                break

        assert weapon_name is not None, self

        return "\n".join(
            [
                "@{}/{}/{}/{}/{}/{}/{}/{}".format(
                    self.name.name,
                    self.ascension,
                    self.level,
                    self.constellations,
                    self.talent_level_a,
                    self.talent_level_e,
                    self.talent_level_q,
                    weapon_name,
                ),
                *(af.to_string() for af in self.artifacts),
            ]
        )
