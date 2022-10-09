#!/usr/bin/env python3
import collections
import re
from genshin import weapon
import logging
from typing import DefaultDict, List

import click

from genshin.packet import session, opcodes
from genshin.formats import official

from genshin.packet.proto.PlayerStoreNotify_pb2 import PlayerStoreNotify
from genshin.packet.proto.StoreType_pb2 import StoreType


@click.command()
@click.argument("path")
@click.argument("my_ip")
def main(path: str, my_ip: str) -> None:
    logging.basicConfig(
        format="%(asctime)s %(levelname)-10s %(name)-60s %(message)s",
        level=logging.INFO,
    )

    s = session.Session(path, my_ip)
    account_data = official.AccountData(s)

    lines = [a.to_string() for a in account_data.artifacts.values() if a.level == 20]
    with open("data/artifacts.txt", "w") as f:
        for l in sorted(lines):
            f.write(l + "\n")

    weapons_by_name: DefaultDict[str, List[weapon.Weapon]] = collections.defaultdict(
        list
    )
    splitter = re.compile(r"([A-Z][a-z]*)")
    for w in account_data.weapons.values():
        name = "_".join(s.lower() for s in splitter.split(w.name.name)[1::2])
        weapons_by_name[name].append(w)

    lines = []
    for name, ws in weapons_by_name.items():
        ws = sorted(
            ws, key=lambda w: (w.refinements, w.ascension, w.level), reverse=True
        )

        lines.append(f"{name}={ws[0].to_string()}")

        for i in range(1, len(ws)):
            lines.append(f"{name}_{i+1}={ws[i].to_string()}")
    with open("data/weapons.txt", "w") as f:
        for l in sorted(lines):
            f.write(l + "\n")


if __name__ == "__main__":
    main()
