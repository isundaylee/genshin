#!/usr/bin/env python3

import json
from typing import Any, Dict
import click
import pathlib


@click.group()
def main():
    pass


def format_event(e: Dict[str, Any], *, raw_data: Dict[str, Any]) -> str:
    event_type = e["event"]

    if event_type == "damage":
        return "{:15s} | {:30s} | {:5s} {:10s} | {:10.0f}".format(
            raw_data["char_names"][e["char_index"]],
            e["msg"],
            "crit" if e["logs"]["crit"] else "",
            e["logs"]["amp"],
            e["logs"]["damage"],
        )
    elif event_type == "energy":
        return "{:15s} | {:5} -> {:5.1f} from {}".format(
            raw_data["char_names"][e["char_index"]],
            "{:5.1f}".format(e["logs"]["pre_recovery"])
            if "pre_recovery" in e["logs"]
            else "???",
            e["logs"]["post_recovery"],
            e["logs"]["source"],
        )
    else:
        return "-"


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
            "T={:5.2f} | {}".format(
                e["frame"] / 60.0, format_event(e, raw_data=raw_data)
            )
        )


@main.command("show-events")
@click.argument("result-file", type=pathlib.Path)
def do_show_damages(result_file):
    with open(result_file) as f:
        raw_data = json.load(f)
        data = json.loads(raw_data["debug"])

    for e in data:
        print(
            "T={:5.2f} | {:10s} | {}".format(
                e["frame"] / 60.0, e["event"], format_event(e, raw_data=raw_data)
            )
        )


if __name__ == "__main__":
    main()
