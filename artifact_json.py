import enum
import json
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


artifacts = [
    parse_artifact(desc)
    for desc in [
        # ESF
        "ESF@2@20 ATK=311 HP=448 HP%=8.7 CR%=7.4 ER%=14.9",
        "ESF@3@20 ER%=51.8 EM=33 CD%=19.4 DEF%=12.4 HP=299",
        "ESF@3@20 ER%=51.8 ATK=18 CR%=9.7 HP%=9.3 EM=38",
        "ESF@1@20 HP=4780 EM=23 ATK%=9.9 CD%=28.8 DEF=19",
        "ESF@5@20 CR%=31.1 ER%=16.2 CD%=12.4 DEF%=5.1 ATK%=11.7",
        # SR
        "SR@2@20 ATK=311 CR%=10.5 HP=538 ATK%=9.9 ER%=10.4",
        "SR@3@20 HP%=46.6 ER%=6.5 ATK=16 CD%=14.8 EM=79",
        "SR@3@20 ATK%=46.6 ER%=9.7 CR%=7.8 DEF%=13.9 DEF=39",
        "SR@3@20 ATK%=46.6 CR%=7.0 ATK=31 EM=68 HP=209",
        "SR@1@20 HP=4780 DEF%=6.6 CR%=6.2 EM=61 ATK%=10.5",
        "SR@1@20 HP=4780 ER%=15.5 CR%=7.0 DEF=39 CD%=5.4",
        "SR@5@20 CR%=31.1 CD%=18.7 DEF=19 ATK=33 HP%=10.5",
        "SR@5@20 CD%=62.2 CR%=9.3 HP=209 ER%=17.5 ATK=18",
        "SR@4@20 EDE%=46.6 CD%=13.2 ATK=18 ER%=24.0 DEF=23",
        # BS
        "BS@1@20 HP=4780 ATK%=9.9 ER%=11.0 CR%=5.8 CD%=17.9",
        "BS@2@20 ATK=311 DEF=39 CD%=12.4 CR%=7.4 DEF%=19.0",
        "BS@3@20 ATK%=46.6 DEF=23 ATK=54 DEF%=17.5 CR%=3.9",
        "BS@1@20 HP=4780 ATK=16 CD%=26.4 DEF=19 ER%=10.4",
        "BS@5@20 CD%=62.2 CR%=14.0 DEF=19 EM=21 ATK=35",
        "BS@2@20 ATK=311 CD%=18.7 HP=538 CR%=7.0 DEF=23",
        # LW
        "LW@3@20 ATK%=46.6 CR%=7.0 CD%=7.0 HP%=5.3 HP=1016",
        "LW@5@20 CR%=31.1 CD%=13.2 ATK%=8.2 HP%=13.4 HP=239",
        "LW@4@20 EDP%=46.6 CD%=12.4 HP=448 CR%=10.1 EM=23",
        "LW@4@20 EDP%=46.6 CD%=12.4 HP=448 CR%=10.1 EM=23",
        # MB
        "MB@4@20 HP%=46.6 EM=65 HP=1135 ATK=19 ATK%=5.8",
        "MB@3@20 HP%=46.6 HP=747 EM=16 ATK%=10.5 DEF=37",
        "MB@1@20 HP=4780 ER%=11.7 CR%=14 CD%=16.2 EM=16",
        "MB@2@20 ATK=311 ER%=11.0 HP%=8.7 EM=23 DEF=60",
    ]
]

print(json.dumps(to_dict(artifacts)))
