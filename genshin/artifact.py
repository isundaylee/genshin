import enum
from typing import List

import attr


class ArtifactSet(enum.Enum):
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
    PD_PCT = "physicalBonus"


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


def parse_artifact(desc: str) -> Artifact:
    type_slot, main, sub1, sub2, sub3, sub4 = desc.split()
    art_type, art_slot, art_level = type_slot.split("@")

    def parse_stat(stat_desc: str) -> ArtifactStat:
        stat_type, stat_value = stat_desc.split("=")
        if stat_type.endswith("%"):
            stat_type = f"{stat_type[:-1]}_PCT"
        return ArtifactStat(
            stat_type=ArtifactStatType[stat_type], stat_value=float(stat_value)
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
            "value": stat.stat_value * 0.01
            if stat.stat_type.name.endswith("_PCT")
            else stat.stat_value,
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
