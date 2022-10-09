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
    translater = official.ArtifactTranslater()

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
