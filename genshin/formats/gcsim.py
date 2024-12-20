from __future__ import annotations

import collections
import json
import pathlib
import re

import attr
from genshin import artifact, character, weapon
from typing import Any, DefaultDict, List, NewType


def artifact_set_to_str(artifact_set: artifact.ArtifactSet) -> str:
    return {
        artifact.ArtifactSet.CW: "crimsonwitchofflames",
        artifact.ArtifactSet.VV: "viridescentvenerer",
        artifact.ArtifactSet.NO: "noblesseoblige",
        artifact.ArtifactSet.HD: "heartofdepth",
        artifact.ArtifactSet.TM: "tenacityofthemillelith",
        artifact.ArtifactSet.AP: "archaicpetra",
        artifact.ArtifactSet.WT: "wandererstroupe",
        artifact.ArtifactSet.ESF: "emblemofseveredfate",
        artifact.ArtifactSet.GF: "gladiatorsfinale",
        artifact.ArtifactSet.TF: "thunderingfury",
        artifact.ArtifactSet.SR: "shimenawasreminiscence",
        artifact.ArtifactSet.BS: "blizzardstrayer",
        artifact.ArtifactSet.OHC: "oceanhuedclam",
    }[artifact_set]


def artifact_stat_type_to_str(stat_type: artifact.ArtifactStatType) -> str:
    return {
        artifact.ArtifactStatType.HP: "hp",
        artifact.ArtifactStatType.HP_PCT: "hp%",
        artifact.ArtifactStatType.HB_PCT: "heal",
        artifact.ArtifactStatType.EM: "em",
        artifact.ArtifactStatType.CR_PCT: "cr",
        artifact.ArtifactStatType.CD_PCT: "cd",
        artifact.ArtifactStatType.ATK: "atk",
        artifact.ArtifactStatType.ATK_PCT: "atk%",
        artifact.ArtifactStatType.DEF: "def",
        artifact.ArtifactStatType.DEF_PCT: "def%",
        artifact.ArtifactStatType.ER_PCT: "er",
        artifact.ArtifactStatType.EDP_PCT: "pyro%",
        artifact.ArtifactStatType.EDH_PCT: "hydro%",
        artifact.ArtifactStatType.EDE_PCT: "electro%",
        artifact.ArtifactStatType.EDC_PCT: "cryo%",
    }[stat_type]


def character_name_to_str(name: character.CharacterName) -> str:
    return {
        character.CharacterName.Yanfei: "yanfei",
        character.CharacterName.KaedeharaKazuha: "kazuha",
        character.CharacterName.Bennett: "bennett",
        character.CharacterName.Xingqiu: "xingqiu",
        character.CharacterName.Zhongli: "zhongli",
        character.CharacterName.Xiangling: "xiangling",
        character.CharacterName.RaidenShogun: "raiden",
        character.CharacterName.Mona: "mona",
        character.CharacterName.Fischl: "fischl",
        character.CharacterName.KamisatoAyaka: "ayaka",
        character.CharacterName.SangonomiyaKokomi: "kokomi",
        character.CharacterName.Rosaria: "rosaria",
    }[name]


def weapon_name_to_str(name: weapon.WeaponName) -> str:
    return {
        weapon.WeaponName.SkywardAtlas: "skywardatlas",
        weapon.WeaponName.IronSting: "ironsting",
        weapon.WeaponName.FavoniusSword: "favoniussword",
        weapon.WeaponName.FavoniusLance: "favoniuslance",
        weapon.WeaponName.SacrificialSword: "sacrificialsword",
        weapon.WeaponName.TheWidsith: "thewidsith",
        weapon.WeaponName.AquilaFavonia: "aquilafavonia",
        weapon.WeaponName.LostPrayerToTheSacredWinds: "lostprayertothesacredwinds",
        weapon.WeaponName.MemoryOfDust: "memoryofdust",
        weapon.WeaponName.PrimordialJadeWingedSpear: "primordialjadewingedspear",
        weapon.WeaponName.TheCatch: "thecatch",
        weapon.WeaponName.KagurasVerity: "kagura",
        weapon.WeaponName.ThrillingTalesOfDragonSlayers: "thrillingtalesofdragonslayers",
        weapon.WeaponName.FreedomSworn: "freedomsworn",
        weapon.WeaponName.TheViridescentHunt: "theviridescenthunt",
        weapon.WeaponName.TheStringless: "thestringless",
        weapon.WeaponName.AmenomaKageuchi: "amenoma",
        weapon.WeaponName.MistsplitterReforged: "mistsplitter",
        weapon.WeaponName.BeginnersProtector: "beginnersprotector",
        weapon.WeaponName.TomeOfTheEternalFlow: "tomeoftheeternalflow",
        weapon.WeaponName.XiphosMoonlight: "xiphosmoonlight",
    }[name]


def generate_gcsim_config(
    characters: List[character.Character], actions: List[str], target: str
) -> str:
    lines: List[str] = []

    for c in characters:
        lines.append(
            "{} char lvl={}/{} cons={} talent={},{},{};".format(
                character_name_to_str(c.name),
                c.level,
                c.level_cap,
                c.constellations,
                c.talent_level_a,
                c.talent_level_e,
                c.talent_level_q,
            )
        )

        lines.append(
            '{} add weapon="{}" refine={} lvl={}/{};'.format(
                character_name_to_str(c.name),
                weapon_name_to_str(c.weapon.name),
                c.weapon.refinements,
                c.weapon.level,
                c.weapon.level_cap,
            )
        )

        artifact_count_by_set: DefaultDict[
            artifact.ArtifactSet, int
        ] = collections.defaultdict(lambda: 0)
        for a in c.artifacts:
            artifact_count_by_set[a.artifact_set] += 1

        for s, count in artifact_count_by_set.items():
            if count < 2:
                continue

            lines.append(
                '{} add set="{}" count={};'.format(
                    character_name_to_str(c.name),
                    artifact_set_to_str(s),
                    2 if count <= 3 else 4,
                )
            )

        lines.append(
            "{} add stats {};".format(
                character_name_to_str(c.name),
                " ".join(
                    "{}={}".format(artifact_stat_type_to_str(t), v)
                    for t, v in c.combined_artifact_stats.items()
                ),
            )
        )

        lines.append("")

    lines.extend(actions)
    lines.append("")

    lines.append(target)
    lines.append("")

    lines.append("active {};".format(character_name_to_str(characters[0].name)))
    lines.append("")

    return "\n".join(lines)


@attr.frozen
class GcsimSummary:
    duration: float

    dps_avg: float
    dps_min: float
    dps_max: float
    dps_std: float

    @staticmethod
    def from_gcsim_output(v: str) -> GcsimSummary:
        m = re.search(
            r"Average ([0-9.]+) damage over ([0-9.]+) seconds, resulting in ([0-9.]+) dps \(min: ([0-9.]+) max: ([0-9.]+) std: ([0-9.]+)\)",
            v,
        )

        assert m is not None

        _, duration, dps_avg, dps_min, dps_max, dps_std = m.groups()

        return GcsimSummary(
            duration=float(duration),
            dps_avg=float(dps_avg),
            dps_min=float(dps_min),
            dps_max=float(dps_max),
            dps_std=float(dps_std),
        )


GcsimSampleLog = NewType("GcsimSampleLog", dict[str, Any])


@attr.define
class GcsimSample:
    logs: list[GcsimSampleLog]
    character_names: list[str]

    @classmethod
    def load(cls, sample_path: pathlib.Path) -> GcsimSample:
        data = json.loads(sample_path.read_text())

        return GcsimSample(
            logs=[GcsimSampleLog(l) for l in data["logs"]],
            character_names=[cd["name"] for cd in data["character_details"]],
        )
