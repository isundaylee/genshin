import os
import json
import collections
from typing import Any, DefaultDict, Dict, List

from genshin import artifact, character, weapon
from genshin.packet import session, opcodes

from genshin.packet.proto.Reliquary_pb2 import Reliquary
from genshin.packet.proto.Weapon_pb2 import Weapon
from genshin.packet.proto.PlayerStoreNotify_pb2 import PlayerStoreNotify
from genshin.packet.proto.AvatarDataNotify_pb2 import AvatarDataNotify
from genshin.packet.proto.StoreType_pb2 import StoreType


class AccountData:
    def __init__(self, s: session.Session) -> None:
        self.artifacts: Dict[int, artifact.Artifact] = {}
        self.weapons: Dict[int, weapon.Weapon] = {}
        self.characters: List[character.Character] = []

        self._parse(s)

    def _parse(self, s: session.Session) -> None:
        for p in s.get_decrypted_packets():
            if p.opcode == opcodes.Opcode.PlayerStoreNotify:
                psn = PlayerStoreNotify()
                psn.ParseFromString(p.data)
                self._parse_artifacts_and_weapons(psn)

            if p.opcode == opcodes.Opcode.AvatarDataNotify:
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
        pass


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
            e["id"]: e for e in self._read_raw("ReliquaryExcelConfigData.json")
        }
        self._set_info_map = {
            e["setId"]: e for e in self._read_raw("ReliquarySetExcelConfigData.json")
        }
        self._main_stat_info_map = {
            e["id"]: e for e in self._read_raw("ReliquaryMainPropExcelConfigData.json")
        }
        self._main_stat_attr_map = {
            (e.get("rank"), e["level"]): {
                ape["propType"]: ape["value"] for ape in e["addProps"]
            }
            for e in self._read_raw("ReliquaryLevelExcelConfigData.json")
        }
        self._sub_stat_info_map = {
            e["id"]: e for e in self._read_raw("ReliquaryAffixExcelConfigData.json")
        }

    @staticmethod
    def _read_raw(name: str) -> Any:
        with open(
            os.path.join(os.path.dirname(__file__), "../../resources", name)
        ) as f:
            return json.load(f)

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
    def __init__(self, artifacts: Dict[int, artifact.Artifact]) -> None:
        self._artifacts = artifacts
