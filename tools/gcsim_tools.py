#!/usr/bin/env python3

import json
import click
import pathlib


@click.group()
def main():
    pass


@main.command("show-damages")
@click.argument("result-file", type=pathlib.Path)
def do_show_damages(result_file):
    with open(result_file) as f:
        raw_data = json.load(f)
        character_names = raw_data["char_names"]
        data = json.loads(raw_data["debug"])

    for e in data:
        if e["event"] != "damage":
            continue

        print(
            "T={:5.2f} | {:15s} | {:30s} | {:5s} {:10s} | {:10.0f}".format(
                e["frame"] / 60.0,
                character_names[e["char_index"]],
                e["msg"],
                "crit" if e["logs"]["crit"] else "",
                e["logs"]["amp"],
                e["logs"]["damage"],
            )
        )


if __name__ == "__main__":
    main()
