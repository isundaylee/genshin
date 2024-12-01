#!/usr/bin/env python3
import logging
from typing import Optional
import click

from genshin.packet import session, packet


@click.command()
@click.argument("path")
def main(path: str) -> None:
    logging.basicConfig(
        format="%(asctime)s %(levelname)-10s %(name)-60s %(message)s",
        level=logging.INFO,
    )

    s = session.Session(path)
    t0 = s.packets[0].timestamp
    for p in s.packets:
        print(
            "{:8.3f} | len {:6d} | {}".format(
                (p.timestamp - t0).total_seconds(),
                len(p.content),
                session.format_bytes(p.content[:30]),
            )
        )


if __name__ == "__main__":
    main()
