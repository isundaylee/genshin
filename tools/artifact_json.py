#!/usr/bin/env python3

import json
from typing import Iterable

import click

from genshin import artifact


def load_artifacts() -> Iterable[artifact.Artifact]:
    with open("data/artifacts.txt") as f:
        for line in f:
            line = line.strip()

            if (not line) or line.startswith("#"):
                continue

            yield artifact.parse_artifact(line)


@click.group()
def main():
    pass


@main.command("print-json")
def do_print_json():
    artifacts = list(load_artifacts())
    print(json.dumps(artifact.to_dict(artifacts)))


if __name__ == "__main__":
    main()
