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


@main.command
@click.argument("proto_path", type=pathlib.Path)
@click.argument("a")
@click.argument("b")
def rename(proto_path: pathlib.Path, a: str, b: str) -> None:
    for f in proto_path.iterdir():
        if a in f.name:
            new_f = f.parent / f.name.replace(a, b)
            f.rename(new_f)
        else:
            new_f = f

        new_f.write_text(new_f.read_text().replace(a, b))

    with (proto_path / "renames.txt").open("a") as f:
        f.write(f"{a} {b}\n")


if __name__ == "__main__":
    main()
