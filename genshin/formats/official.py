import logging
import os
import json
import collections
from typing import Any, DefaultDict, Dict, List, Optional, Tuple

from genshin import artifact, character, weapon
from genshin.packet import session, opcodes

from genshin.packet.proto.Reliquary_pb2 import Reliquary
from genshin.packet.proto.Weapon_pb2 import Weapon
from genshin.packet.proto.PlayerStoreNotify_pb2 import PlayerStoreNotify
from genshin.packet.proto.AvatarDataNotify_pb2 import AvatarDataNotify
from genshin.packet.proto.StoreType_pb2 import StoreType
from genshin.packet.proto.AvatarInfo_pb2 import AvatarInfo


logger = logging.getLogger(__name__)


class AccountData:
    def __init__(self, s: session.Session) -> None:
        self.artifacts: Dict[int, artifact.Artifact] = {}
        self.weapons: Dict[int, weapon.Weapon] = {}
        self.characters: List[character.Character] = []

        self._parse(s)

    def _parse(self, s: session.Session) -> None:
        for p in s.get_decrypted_packets():
            if p.raw_opcode == opcodes.Opcode.PlayerStoreNotify.value:
                psn = PlayerStoreNotify()
                psn.ParseFromString(p.data)
                self._parse_artifacts_and_weapons(psn)

            if p.raw_opcode == opcodes.Opcode.AvatarDataNotify.value:
                adn = AvatarDataNotify()
                adn.ParseFromString(p.data)
                self._parse_characters(adn)

    def _parse_artifacts_and_weapons(self, psn: PlayerStoreNotify) -> None:
        assert psn.store_type == StoreType.STORE_TYPE_PACK

        artifact_parser = ArtifactParser()
        weapon_parser = WeaponParser()

        for item in psn.item_list:
            if item.WhichOneof("detail") != "equip":
                continue

            equip = item.equip

            if equip.WhichOneof("detail") == "reliquary":
                assert item.guid not in self.artifacts
                self.artifacts[item.guid] = artifact_parser.parse_artifact(
                    item.item_id, equip.reliquary
                )
            elif equip.WhichOneof("detail") == "weapon":
                assert item.guid not in self.weapons
                self.weapons[item.guid] = weapon_parser.parse_weapon(
                    item.item_id, equip.weapon
                )

    def _parse_characters(self, adn: AvatarDataNotify) -> None:
        character_parser = CharacterParser(self.artifacts, self.weapons)

        for avatar in adn.avatar_list:
            character = character_parser.parse_character(avatar)
            if character is not None:
                self.characters.append(character)


def _read_raw_excel_data(name: str) -> Any:
    with open(os.path.join(os.path.dirname(__file__), "../../resources", name)) as f:
        return json.load(f)


class ArtifactParser:
    _NUMERIC_SLOT_MAPPING = {
        "EQUIP_BRACER": 1,
        "EQUIP_NECKLACE": 2,
        "EQUIP_SHOES": 3,
        "EQUIP_RING": 4,
        "EQUIP_DRESS": 5,
    }

    # Look at images here
    # https://feixiaoqiu.com/static/images/reliquary/
    _SET_NAME_MAPPING = {
        10001: "RS",
        10003: "DW",
        10004: "TMI",
        10005: "B",
        10007: "I",
        10008: "G",
        10009: "TE",
        10010: "A",
        10011: "LD",
        10013: "S",
        14001: "BS",
        14002: "TS",
        14003: "LW",
        14004: "MB",
        15001: "GF",
        15002: "VV",
        15003: "WT",
        15005: "TF",
        15006: "CW",
        15007: "NO",
        15008: "BC",
        15009: "PI",
        15013: "PS",
        15014: "AP",
        15015: "RB",
        15016: "HD",
        15017: "TM",
        15018: "PF",
        15019: "SR",
        15020: "ESF",
        15021: "HOD",
        15022: "OHC",
        15023: "VH",
        15024: "EO",
        15025: "DM",
        15026: "GD",
    }

    _MAIN_STAT_MAPPING = {
        "FIGHT_PROP_CRITICAL": "CR_PCT",
        "FIGHT_PROP_CRITICAL_HURT": "CD_PCT",
        "FIGHT_PROP_ATTACK": "ATK",
        "FIGHT_PROP_ATTACK_PERCENT": "ATK_PCT",
        "FIGHT_PROP_ELEMENT_MASTERY": "EM",
        "FIGHT_PROP_CHARGE_EFFICIENCY": "ER_PCT",
        "FIGHT_PROP_HP": "HP",
        "FIGHT_PROP_HP_PERCENT": "HP_PCT",
        "FIGHT_PROP_DEFENSE": "DEF",
        "FIGHT_PROP_DEFENSE_PERCENT": "DEF_PCT",
        "FIGHT_PROP_PHYSICAL_ADD_HURT": "PD_PCT",
        "FIGHT_PROP_HEAL_ADD": "HB_PCT",
        "FIGHT_PROP_ROCK_ADD_HURT": "EDG_PCT",
        "FIGHT_PROP_WIND_ADD_HURT": "EDA_PCT",
        "FIGHT_PROP_ICE_ADD_HURT": "EDC_PCT",
        "FIGHT_PROP_WATER_ADD_HURT": "EDH_PCT",
        "FIGHT_PROP_FIRE_ADD_HURT": "EDP_PCT",
        "FIGHT_PROP_ELEC_ADD_HURT": "EDE_PCT",
        "FIGHT_PROP_GRASS_ADD_HURT": "EDD_PCT",
    }

    def __init__(self):
        self._item_info_map = {
            e["id"]: e for e in _read_raw_excel_data("ReliquaryExcelConfigData.json")
        }
        self._set_info_map = {
            e["setId"]: e
            for e in _read_raw_excel_data("ReliquarySetExcelConfigData.json")
        }
        self._main_stat_info_map = {
            e["id"]: e
            for e in _read_raw_excel_data("ReliquaryMainPropExcelConfigData.json")
        }
        self._main_stat_attr_map = {
            (e.get("rank"), e["level"]): {
                ape["propType"]: ape["value"] for ape in e["addProps"]
            }
            for e in _read_raw_excel_data("ReliquaryLevelExcelConfigData.json")
        }
        self._sub_stat_info_map = {
            e["id"]: e
            for e in _read_raw_excel_data("ReliquaryAffixExcelConfigData.json")
        }

    def parse_artifact(self, item_id: int, r: Reliquary) -> artifact.Artifact:
        item_info = self._item_info_map[item_id]

        numeric_slot = self._NUMERIC_SLOT_MAPPING[item_info["equipType"]]
        set_name = self._SET_NAME_MAPPING[item_info["setId"]]
        main_prop_type = self._main_stat_info_map[r.main_prop_id]["propType"]

        sub_stats: DefaultDict[str, float] = collections.defaultdict(float)

        for ss_id in r.append_prop_id_list:
            sub_stats[
                self._sub_stat_info_map[ss_id]["propType"]
            ] += self._sub_stat_info_map[ss_id]["propValue"]

        return artifact.Artifact(
            level=r.level - 1,
            artifact_set=artifact.ArtifactSet[set_name],
            artifact_slot=artifact.ArtifactSlot(numeric_slot),
            main_stat=artifact.ArtifactStat(
                stat_type=artifact.ArtifactStatType[
                    self._MAIN_STAT_MAPPING[main_prop_type]
                ],
                stat_value=self._main_stat_attr_map[(item_info["rankLevel"], r.level)][
                    main_prop_type
                ],
            ),
            sub_stats=[
                artifact.ArtifactStat(
                    stat_type=artifact.ArtifactStatType[self._MAIN_STAT_MAPPING[k]],
                    stat_value=v,
                )
                for k, v in sub_stats.items()
            ],
        )


class WeaponParser:
    _WEAPON_NAME_MAPPING: Dict[int, weapon.WeaponName] = {
        11101: weapon.WeaponName.DullBlade,
        11201: weapon.WeaponName.SilverSword,
        11301: weapon.WeaponName.CoolSteel,
        11302: weapon.WeaponName.HarbingerOfDawn,
        11303: weapon.WeaponName.TravelersHandySword,
        11305: weapon.WeaponName.FilletBlade,
        11306: weapon.WeaponName.SkyriderSword,
        11401: weapon.WeaponName.FavoniusSword,
        11402: weapon.WeaponName.TheFlute,
        11403: weapon.WeaponName.SacrificialSword,
        11405: weapon.WeaponName.LionsRoar,
        11406: weapon.WeaponName.PrototypeRancour,
        11407: weapon.WeaponName.IronSting,
        11409: weapon.WeaponName.TheBlackSword,
        11414: weapon.WeaponName.AmenomaKageuchi,
        11415: weapon.WeaponName.CinnabarSpindle,
        11416: weapon.WeaponName.KagotsurubeIsshin,
        11417: weapon.WeaponName.SapwoodBlade,
        11501: weapon.WeaponName.AquilaFavonia,
        12101: weapon.WeaponName.WasterGreatsword,
        12201: weapon.WeaponName.OldMercsPal,
        12301: weapon.WeaponName.FerrousShadow,
        12302: weapon.WeaponName.BloodtaintedGreatsword,
        12303: weapon.WeaponName.WhiteIronGreatsword,
        12305: weapon.WeaponName.DebateClub,
        12306: weapon.WeaponName.SkyriderGreatsword,
        12401: weapon.WeaponName.FavoniusGreatsword,
        12402: weapon.WeaponName.TheBell,
        12403: weapon.WeaponName.SacrificialGreatsword,
        12405: weapon.WeaponName.Rainslasher,
        12406: weapon.WeaponName.PrototypeArchaic,
        12407: weapon.WeaponName.Whiteblind,
        12409: weapon.WeaponName.SerpentSpine,
        12412: weapon.WeaponName.LuxuriousSealord,
        12414: weapon.WeaponName.KatsuragikiriNagamasa,
        13101: weapon.WeaponName.BeginnersProtector,
        13201: weapon.WeaponName.IronPoint,
        13301: weapon.WeaponName.WhiteTassel,
        13302: weapon.WeaponName.Halberd,
        13303: weapon.WeaponName.BlackTassel,
        13401: weapon.WeaponName.DragonsBane,
        13402: weapon.WeaponName.PrototypeStarglitter,
        13403: weapon.WeaponName.CrescentPike,
        13405: weapon.WeaponName.Deathmatch,
        13407: weapon.WeaponName.FavoniusLance,
        13409: weapon.WeaponName.DragonspineSpear,
        13415: weapon.WeaponName.TheCatch,
        13416: weapon.WeaponName.WavebreakersFin,
        13419: weapon.WeaponName.MissiveWindspear,
        13501: weapon.WeaponName.StaffOfHoma,
        13505: weapon.WeaponName.PrimordialJadeWingedSpear,
        14101: weapon.WeaponName.ApprenticesNotes,
        14201: weapon.WeaponName.PocketGrimoire,
        14301: weapon.WeaponName.MagicGuide,
        14302: weapon.WeaponName.ThrillingTalesOfDragonSlayers,
        14303: weapon.WeaponName.OtherworldlyStory,
        14304: weapon.WeaponName.EmeraldOrb,
        14305: weapon.WeaponName.TwinNephrite,
        14401: weapon.WeaponName.FavoniusCodex,
        14402: weapon.WeaponName.TheWidsith,
        14403: weapon.WeaponName.SacrificialFragments,
        14409: weapon.WeaponName.EyeOfPerception,
        14413: weapon.WeaponName.DodocoTales,
        14415: weapon.WeaponName.OathswornEye,
        14501: weapon.WeaponName.SkywardAtlas,
        15101: weapon.WeaponName.HuntersBow,
        15201: weapon.WeaponName.SeasonedHuntersBow,
        15301: weapon.WeaponName.RavenBow,
        15302: weapon.WeaponName.SharpshootersOath,
        15303: weapon.WeaponName.RecurveBow,
        15304: weapon.WeaponName.Slingshot,
        15305: weapon.WeaponName.Messenger,
        15401: weapon.WeaponName.FavoniusWarbow,
        15402: weapon.WeaponName.TheStringless,
        15403: weapon.WeaponName.SacrificialBow,
        15405: weapon.WeaponName.Rust,
        15409: weapon.WeaponName.TheViridescentHunt,
        15411: weapon.WeaponName.FadingTwilight,
        15414: weapon.WeaponName.Hamayumi,
        15416: weapon.WeaponName.MouunsMoon,
        15503: weapon.WeaponName.ElegyForTheEnd,
    }

    def __init__(self) -> None:
        pass

    def parse_weapon(self, item_id: int, r: Weapon) -> weapon.Weapon:
        refinements = 1
        if r.affix_map:
            assert len(r.affix_map) == 1
            refinements = 1 + next(iter(r.affix_map.values()))

        assert 1 <= refinements <= 5, r

        return weapon.Weapon(
            name=WeaponParser._WEAPON_NAME_MAPPING[item_id],
            ascension=r.promote_level,
            level=r.level,
            refinements=refinements,
        )


class CharacterParser:
    _CHARACTER_NAME_MAPPING = {
        10000002: character.CharacterName.KamisatoAyaka,
        10000003: character.CharacterName.Jean,
        10000005: character.CharacterName.Traveler,
        10000006: character.CharacterName.Lisa,
        10000007: character.CharacterName.Traveler,
        10000014: character.CharacterName.Barbara,
        10000015: character.CharacterName.Kaeya,
        10000016: character.CharacterName.Diluc,
        10000020: character.CharacterName.Razor,
        10000021: character.CharacterName.Amber,
        10000022: character.CharacterName.Venti,
        10000023: character.CharacterName.Xiangling,
        10000024: character.CharacterName.Beidou,
        10000025: character.CharacterName.Xingqiu,
        10000026: character.CharacterName.Xiao,
        10000027: character.CharacterName.Ningguang,
        10000029: character.CharacterName.Klee,
        10000030: character.CharacterName.Zhongli,
        10000031: character.CharacterName.Fischl,
        10000032: character.CharacterName.Bennett,
        10000033: character.CharacterName.Tartaglia,
        10000034: character.CharacterName.Noelle,
        10000035: character.CharacterName.Qiqi,
        10000036: character.CharacterName.Chongyun,
        10000037: character.CharacterName.Ganyu,
        10000038: character.CharacterName.Albedo,
        10000039: character.CharacterName.Diona,
        10000041: character.CharacterName.Mona,
        10000042: character.CharacterName.Keqing,
        10000043: character.CharacterName.Sucrose,
        10000044: character.CharacterName.Xinyan,
        10000045: character.CharacterName.Rosaria,
        10000046: character.CharacterName.HuTao,
        10000047: character.CharacterName.KaedeharaKazuha,
        10000048: character.CharacterName.Yanfei,
        10000049: character.CharacterName.Yoimiya,
        10000050: character.CharacterName.Thoma,
        10000051: character.CharacterName.Eula,
        10000052: character.CharacterName.RaidenShogun,
        10000053: character.CharacterName.Sayu,
        10000054: character.CharacterName.SangonomiyaKokomi,
        10000055: character.CharacterName.Gorou,
        10000056: character.CharacterName.KujouSara,
        10000057: character.CharacterName.AratakiItto,
        10000058: character.CharacterName.YaeMiko,
        10000059: character.CharacterName.ShikanoinHeizo,
        10000060: character.CharacterName.Yelan,
        10000062: character.CharacterName.Aloy,
        10000063: character.CharacterName.Shenhe,
        10000064: character.CharacterName.YunJin,
        10000065: character.CharacterName.KukiShinobu,
        10000066: character.CharacterName.KamisatoAyato,
        10000067: character.CharacterName.Collei,
        10000072: character.CharacterName.Candace,
    }

    def __init__(
        self, artifacts: Dict[int, artifact.Artifact], weapons: Dict[int, weapon.Weapon]
    ) -> None:
        self._artifacts = artifacts
        self._weapons = weapons

        self._skill_depot_info_map = {
            e["id"]: e
            for e in _read_raw_excel_data("AvatarSkillDepotExcelConfigData.json")
        }

    def parse_character(self, a: AvatarInfo) -> Optional[character.Character]:
        skill_depot_info = self._skill_depot_info_map[a.skill_depot_id]

        talent_level_a = a.skill_level_map[skill_depot_info["skills"][0]]
        talent_level_e = a.skill_level_map[skill_depot_info["skills"][1]]
        talent_level_q = a.skill_level_map[skill_depot_info["energySkill"]]

        equipped_weapon: Optional[weapon.Weapon] = None
        equipped_artifacts: List[Optional[artifact.Artifact]] = [
            None,
            None,
            None,
            None,
            None,
        ]

        for equipment_guid in a.equip_guid_list:
            if equipment_guid in self._weapons:
                assert equipped_weapon is None
                equipped_weapon = self._weapons[equipment_guid]
            else:
                af = self._artifacts[equipment_guid]
                assert equipped_artifacts[af.artifact_slot.value - 1] is None
                equipped_artifacts[af.artifact_slot.value - 1] = af

        if any(eaf is None for eaf in equipped_artifacts) or (equipped_weapon is None):
            logger.warning(
                "Skipping %s due to missing weapon/artifact",
                self._CHARACTER_NAME_MAPPING[a.avatar_id].name,
            )
            return None

        return character.Character(
            name=self._CHARACTER_NAME_MAPPING[a.avatar_id],
            ascension=a.prop_map[1002].val,
            level=a.prop_map[4001].val,
            constellations=len(a.talent_id_list),
            talent_level_a=talent_level_a,
            talent_level_e=talent_level_e,
            talent_level_q=talent_level_q,
            weapon=equipped_weapon,
            artifacts=tuple(equipped_artifacts),
        )
