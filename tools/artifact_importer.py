#!/usr/bin/env python3
import collections
import json
import logging
import os
from typing import Any, DefaultDict

import click

from genshin.packet import session, opcodes

from genshin.packet.proto.PlayerStoreNotify_pb2 import PlayerStoreNotify
from genshin.packet.proto.StoreType_pb2 import StoreType
from genshin.packet.proto.Reliquary_pb2 import Reliquary


class ArtifactTranslater:
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
        10004: "TM",
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
        "FIGHT_PROP_CRITICAL": "CR%",
        "FIGHT_PROP_CRITICAL_HURT": "CD%",
        "FIGHT_PROP_ATTACK": "ATK",
        "FIGHT_PROP_ATTACK_PERCENT": "ATK%",
        "FIGHT_PROP_ELEMENT_MASTERY": "EM",
        "FIGHT_PROP_CHARGE_EFFICIENCY": "ER%",
        "FIGHT_PROP_HP": "HP",
        "FIGHT_PROP_HP_PERCENT": "HP%",
        "FIGHT_PROP_DEFENSE": "DEF",
        "FIGHT_PROP_DEFENSE_PERCENT": "DEF%",
        "FIGHT_PROP_PHYSICAL_ADD_HURT": "PD%",
        "FIGHT_PROP_HEAL_ADD": "HB%",
        "FIGHT_PROP_ROCK_ADD_HURT": "EDG%",
        "FIGHT_PROP_WIND_ADD_HURT": "EDA%",
        "FIGHT_PROP_ICE_ADD_HURT": "EDC%",
        "FIGHT_PROP_WATER_ADD_HURT": "EDH%",
        "FIGHT_PROP_FIRE_ADD_HURT": "EDP%",
        "FIGHT_PROP_ELEC_ADD_HURT": "EDE%",
        "FIGHT_PROP_GRASS_ADD_HURT": "EDD%",
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
        with open(os.path.join(os.path.dirname(__file__), "../resources", name)) as f:
            return json.load(f)

    @staticmethod
    def _format_attr(name: str, v: float) -> str:
        if name.endswith("%"):
            return f"{name}={100.0*v:.1f}"
        else:
            return f"{name}={v:.0f}"

    def translate_artifact(self, item_id: int, r: Reliquary) -> str:
        item_info = self._item_info_map[item_id]

        numeric_slot = self._NUMERIC_SLOT_MAPPING[item_info["equipType"]]
        set_name = self._SET_NAME_MAPPING[item_info["setId"]]
        main_prop_type = self._main_stat_info_map[r.main_prop_id]["propType"]

        sub_stats: DefaultDict[str, float] = collections.defaultdict(float)

        for ss_id in r.append_prop_id_list:
            sub_stats[
                self._sub_stat_info_map[ss_id]["propType"]
            ] += self._sub_stat_info_map[ss_id]["propValue"]

        return "{}@{}@{} {} {}".format(
            set_name,
            numeric_slot,
            r.level - 1,
            self._format_attr(
                self._MAIN_STAT_MAPPING[main_prop_type],
                self._main_stat_attr_map[(item_info["rankLevel"], r.level)][
                    main_prop_type
                ],
            ),
            " ".join(
                self._format_attr(self._MAIN_STAT_MAPPING[k], v)
                for k, v in sub_stats.items()
            ),
        )


@click.command()
@click.argument("path")
@click.argument("my_ip")
def main(path: str, my_ip: str) -> None:
    logging.basicConfig(
        format="%(asctime)s %(levelname)-10s %(name)-60s %(message)s",
        level=logging.INFO,
    )

    s = session.Session(path, my_ip)
    translater = ArtifactTranslater()

    for p in s.get_decrypted_packets():
        if p.opcode != opcodes.Opcode.PlayerStoreNotify:
            continue

        psn = PlayerStoreNotify()
        psn.ParseFromString(p.data)

        assert psn.store_type == StoreType.STORE_TYPE_PACK

        for item in psn.item_list:
            if item.WhichOneof("detail") != "equip":
                continue

            equip = item.equip
            if equip.WhichOneof("detail") != "reliquary":
                continue

            print(translater.translate_artifact(item.item_id, equip.reliquary))


if __name__ == "__main__":
    main()
