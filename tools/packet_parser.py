#!/usr/bin/env python3
import click

from genshin.packet import session


@click.command()
@click.argument("path")
@click.argument("my_ip")
def main(path: str, my_ip: str) -> None:
    s = session.Session(path, my_ip)


if __name__ == "__main__":
    main()
