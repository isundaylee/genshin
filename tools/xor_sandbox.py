#!/usr/bin/env python3

import click

import collections
import pathlib


@click.group()
def main() -> None:
    pass


@main.command()
def sandbox() -> None:
    for b in range(0, 256):
        if (
            ((0x52 ^ b) - 1 == (0x5D ^ b))
            and ((0x53 ^ b) - 2 == (0x5D ^ b))
            and ((0x50 ^ b) - 3 == (0x5D ^ b))
            and ((0x57 ^ b) - 6 == (0x5D ^ b))
            and ((0x54 ^ b) - 7 == (0x5D ^ b))
            and ((0x5D ^ b) <= 19 - 10)
            and ((0x52 ^ b) <= 20 - 10)
            and ((0x53 ^ b) <= 21 - 10)
            and ((0x50 ^ b) <= 22 - 10)
            and ((0x57 ^ b) <= 25 - 10)
            and ((0x54 ^ b) <= 26 - 10)
        ):
            print(hex(b))
            print(0x5D ^ b)
            print(0x52 ^ b)
            print(0x53 ^ b)
            print(0x50 ^ b)
            print(0x57 ^ b)
            print(0x54 ^ b)


@main.command
@click.argument("path", type=pathlib.Path)
@click.option("--group-len", type=int, default=1)
def count_frequency(path: pathlib.Path, *, group_len: int) -> None:
    content = path.read_bytes()
    c = collections.Counter(
        content[i : i + group_len] for i in range(len(content) - group_len + 1)
    )

    print(c)


if __name__ == "__main__":
    main()
