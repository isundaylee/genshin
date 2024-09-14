#!/usr/bin/env python3
import pathlib
import logging

import click

from genshin.packet import session


@click.group()
def main() -> None:
    logging.basicConfig(
        format="%(asctime)s %(levelname)-10s %(name)-60s %(message)s",
        level=logging.INFO,
    )


@main.command()
@click.argument("path")
@click.argument("output", type=pathlib.Path)
def dump_decrypted(path: str, output: pathlib.Path) -> None:
    for i, p in enumerate(session.Session(path).get_decrypted_packets()):
        try:
            name = p.opcode.name
        except ValueError:
            name = f"opcode{p.raw_opcode}"

        fn = f"{i:05d}-{name}.packet"
        (output / fn).write_bytes(p.content)


@main.command()
@click.argument("path")
def print_decrypted(path: str) -> None:
    for p in session.Session(path).get_decrypted_packets():
        print(
            "{:10s} | len {:5d} | {}".format(
                p.direction.name,
                len(p.content),
                session.format_bytes(p.content, start=len(p.content)),
            )
        )


if __name__ == "__main__":
    main()
