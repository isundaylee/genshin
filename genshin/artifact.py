import collections
import enum
from genshin import character
from typing import DefaultDict, Dict, List

import attr


class ArtifactSet(enum.Enum):
    RS = "resolutionOfSojourner"
    DW = "defenderWill"
    TMI = "tinyMiracle"
    B = "berserker"
    I = "instructor"
    G = "gambler"
    TE = "exile"
    A = "adventurer"
    LD = "luckyDog"
    S = "scholar"

    PI = "prayersForIllumination"
    PS = "prayersToSpringtime"

    AP = "archaicPetra"
    HD = "heartOfDepth"
    BS = "blizzardStrayer"
    RB = "retracingBolide"
    NO = "noblesseOblige"
    GF = "gladiatorFinale"
    MB = "maidenBeloved"
    VV = "viridescentVenerer"
    LW = "lavaWalker"
    CW = "crimsonWitch"
    TS = "thunderSmoother"
    TF = "thunderingFury"
    BC = "bloodstainedChivalry"
    WT = "wandererTroupe"
    SCH = "scholar"
    PF = "paleFlame"
    TM = "tenacityOfTheMillelith"
    ESF = "emblemOfSeveredFate"
    SR = "shimenawaReminiscence"
    HOD = "huskOfOpulentDreams"
    OHC = "oceanHuedClam"
    VH = "VermillionHereafter"
    EO = "EchoesOfAnOffering"
    DM = "DeepwoodMemories"
    GD = "GildedDreams"


class ArtifactSlot(enum.IntEnum):
    Flower = 1
    Feather = 2
    Sand = 3
    Cup = 4
    Circlet = 5


class ArtifactStatType(enum.Enum):
    HB_PCT = "cureEffect"
    HP = "lifeStatic"
    HP_PCT = "lifePercentage"
    ATK = "attackStatic"
    ATK_PCT = "attackPercentage"
    DEF = "defendStatic"
    DEF_PCT = "defendPercentage"
    CR_PCT = "critical"
    CD_PCT = "criticalDamage"
    EM = "elementalMastery"
    ER_PCT = "recharge"
    EDE_PCT = "thunderBonus"
    EDP_PCT = "fireBonus"
    EDH_PCT = "waterBonus"
    EDC_PCT = "iceBonus"
    EDA_PCT = "windBonus"
    EDG_PCT = "rockBonus"
    EDD_PCT = "dendroBonus"
    PD_PCT = "physicalBonus"


# Taken from https://docs.google.com/document/d/1_UpwP0VziHehZVwdsD74wYuWD9pdSAknNVzs30U4vFE/edit
_STANDARD_ROLL: Dict[ArtifactStatType, float] = {
    ArtifactStatType.HP: 253.94,
    ArtifactStatType.HP_PCT: 0.0496,
    ArtifactStatType.ATK: 16.54,
    ArtifactStatType.ATK_PCT: 0.0496,
    ArtifactStatType.DEF: 19.68,
    ArtifactStatType.DEF_PCT: 0.062,
    ArtifactStatType.CR_PCT: 0.0331,
    ArtifactStatType.CD_PCT: 0.0662,
    ArtifactStatType.EM: 19.82,
    ArtifactStatType.ER_PCT: 0.0551,
}


@attr.s(auto_attribs=True)
class ArtifactStat:
    stat_type: ArtifactStatType
    stat_value: float


@attr.s(auto_attribs=True)
class Artifact:
    level: int
    artifact_set: ArtifactSet
    artifact_slot: ArtifactSlot
    main_stat: ArtifactStat
    sub_stats: List[ArtifactStat]

    def to_string(self) -> str:
        def _format_attr(stat: ArtifactStat) -> str:
            if stat.stat_type.name.endswith("_PCT"):
                return f"{stat.stat_type.name[:-len('_PCP')]+'%'}={100.0*stat.stat_value:.1f}"
            else:
                return f"{stat.stat_type.name}={stat.stat_value:.0f}"

        return "{}@{}@{} {} {}".format(
            self.artifact_set.name,
            self.artifact_slot.value,
            self.level,
            _format_attr(self.main_stat),
            " ".join(_format_attr(s) for s in self.sub_stats),
        )


def parse_artifact(desc: str) -> Artifact:
    type_slot, main, sub1, sub2, sub3, sub4 = desc.split()
    art_type, art_slot, art_level = type_slot.split("@")

    def parse_stat(stat_desc: str) -> ArtifactStat:
        stat_type, stat_value = stat_desc.split("=")
        stat_value = float(stat_value)
        if stat_type.endswith("%"):
            stat_type = f"{stat_type[:-1]}_PCT"
            stat_value *= 0.01
        return ArtifactStat(
            stat_type=ArtifactStatType[stat_type], stat_value=stat_value
        )

    return Artifact(
        level=int(art_level),
        artifact_set=ArtifactSet[art_type],
        artifact_slot=ArtifactSlot(int(art_slot)),
        main_stat=parse_stat(main),
        sub_stats=[
            parse_stat(sub1),
            parse_stat(sub2),
            parse_stat(sub3),
            parse_stat(sub4),
        ],
    )


def to_dict(artifacts: List[Artifact]):
    SLOT_MAP = {
        ArtifactSlot.Flower: "flower",
        ArtifactSlot.Feather: "feather",
        ArtifactSlot.Sand: "sand",
        ArtifactSlot.Cup: "cup",
        ArtifactSlot.Circlet: "head",
    }

    def stat_to_json(stat: ArtifactStat):
        return {
            "name": stat.stat_type.value,
            "value": stat.stat_value,
        }

    def artifact_to_json(artifact: Artifact):
        return {
            "setName": artifact.artifact_set.value,
            "position": SLOT_MAP[artifact.artifact_slot],
            "mainTag": stat_to_json(artifact.main_stat),
            "normalTags": [stat_to_json(stat) for stat in artifact.sub_stats],
            "omit": False,
            "level": artifact.level,
            "star": 5,
        }

    result = {}
    for slot, slot_str in SLOT_MAP.items():
        result[slot_str] = [
            artifact_to_json(artifact)
            for artifact in artifacts
            if artifact.artifact_slot == slot
        ]

    return result


def get_artifact_scores(
    artifacts: List[Artifact], ch: character.Character, *, convert_nopct_stats: bool
) -> Dict[ArtifactStatType, float]:
    results: DefaultDict[ArtifactStatType, float] = collections.defaultdict(lambda: 0.0)
    for a in artifacts:
        for s in a.sub_stats:
            t, v = s.stat_type, s.stat_value

            if convert_nopct_stats:
                if t == ArtifactStatType.HP:
                    t = ArtifactStatType.HP_PCT
                    v /= ch.base_hp
                elif t == ArtifactStatType.ATK:
                    t = ArtifactStatType.ATK_PCT
                    v /= ch.base_atk_with_weapon
                elif t == ArtifactStatType.DEF:
                    t = ArtifactStatType.DEF_PCT
                    v /= ch.base_def

            results[t] += v / _STANDARD_ROLL[t]
    return dict(results)
