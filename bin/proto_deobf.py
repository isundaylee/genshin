#!/usr/bin/env python3

import collections
import pathlib
import re
import click


@click.group
def main() -> None:
    pass


@main.command
@click.argument("proto_path", type=pathlib.Path)
def count_fields(proto_path: pathlib.Path) -> None:
    for f in proto_path.iterdir():
        field_types = list[str]()
        for l in f.read_text().splitlines():
            if (m := re.fullmatch(r"\s+([a-zA-Z0-9 ]+) [^ ]+ = \d+;", l)) is None:
                continue
            [t] = m.groups()
            field_types.append(t)

        print(
            f.name,
            " ".join(sorted(field_types)),
            "(",
            ", ".join(
                f"{k} x {v}" for k, v in collections.Counter(field_types).items()
            ),
            ")",
        )


if __name__ == "__main__":
    main()
