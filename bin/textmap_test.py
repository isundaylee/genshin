#!/usr/bin/env python3

import json
import click
import pathlib
from typing import Any


_ROOT = pathlib.Path("/Users/jiahaoli/Programming/Git/AnimeGameData")


class RoleMapper:
    def __init__(
        self, npc_excel_config_data: list[dict[str, Any]], text_map: dict[str, str]
    ) -> None:
        self._npc_mapping = {
            str(e["uniqueBodyId"]): text_map.get(str(e["nameTextMapHash"]), "UNKNOWN")
            for e in npc_excel_config_data
        }

    def map_role(self, type: str, id: str) -> str:
        match type:
            case "TALK_ROLE_NPC":
                return self._npc_mapping.get(id, "UNKNOWN")
            case "TALK_ROLE_PLAYER":
                return "旅行者"
            case "TALK_ROLE_NEED_CLICK_BLACK_SCREEN":
                return "黑屏文本"
            case _:
                return f"UNKNOWN-{type}-{id}"


@click.group()
def main() -> None:
    pass


@main.command()
@click.argument("quest_path", type=pathlib.Path)
def quest(quest_path: pathlib.Path) -> None:
    textmap = json.loads((_ROOT / "TextMap/TextMapCHS.json").read_text())
    quest = json.loads((_ROOT / quest_path).read_text())
    role_mapper = RoleMapper(
        npc_excel_config_data=json.loads(
            (_ROOT / "ExcelBinOutput/NpcExcelConfigData.json").read_text()
        ),
        text_map=textmap,
    )

    for e in quest["dialogList"]:
        role = e["talkRole"]
        role_name = role_mapper.map_role(role["type"], role["_id"])
        text_id = str(e["talkContentTextMapHash"])

        try:
            print(f"{role_name}: {textmap[text_id]}")
        except KeyError:
            print(f"Missing text for {text_id}")


if __name__ == "__main__":
    main()
