#!/usr/bin/env python3
import pathlib
import logging

import click

from genshin.packet import session


@click.group()
def main() -> None:
    pass


@main.command()
@click.argument("path")
@click.argument("my_ip")
@click.argument("output", type=pathlib.Path)
def dump_decrypted(path: str, my_ip: str, output: pathlib.Path) -> None:
    logging.basicConfig(
        format="%(asctime)s %(levelname)-10s %(name)-60s %(message)s",
        level=logging.INFO,
    )

    s = session.Session(path, my_ip)

    for i, p in enumerate(s.get_decrypted_packets()):
        try:
            name = p.opcode.name
        except ValueError:
            name = f"opcode{p.raw_opcode}"

        fn = f"{i:05d}-{name}.packet"
        (output / fn).write_bytes(p.content)


if __name__ == "__main__":
    main()
