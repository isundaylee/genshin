#!/usr/bin/env python3
import collections
import pathlib
import re
from genshin import character, weapon
import logging
from typing import DefaultDict, Dict, List

import click

from genshin.packet import session, opcodes
from genshin.formats import official

from genshin.packet.proto.PlayerStoreNotify_pb2 import PlayerStoreNotify
from genshin.packet.proto.StoreType_pb2 import StoreType


@click.command()
@click.argument("path")
@click.argument("my_ip")
@click.argument("output", type=pathlib.Path)
def main(path: str, my_ip: str, output: pathlib.Path) -> None:
    logging.basicConfig(
        format="%(asctime)s %(levelname)-10s %(name)-60s %(message)s",
        level=logging.INFO,
    )

    s = session.Session(path, my_ip)

    for i, p in enumerate(s.get_decrypted_packets()):
        fn = f"{i:05d}-{p.opcode.name}.packet"
        (output / fn).write_bytes(p.content)

    # for i, p in enumerate(s.packets):
    #     print(i, len(p.content))


if __name__ == "__main__":
    main()
