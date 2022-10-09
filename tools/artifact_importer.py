#!/usr/bin/env python3
import logging

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

    for a in account_data.artifacts.values():
        print(a.to_string())


if __name__ == "__main__":
    main()
