#!/usr/bin/env python3

import gzip
import json
from typing import Any, Dict, Optional
import click
import pathlib


@click.group()
def main():
    pass


def load_result(result_file: pathlib.Path) -> Dict[str, Any]:
    if result_file.name.endswith(".gz"):
        with gzip.open(result_file) as f:
            return json.load(f)
    else:
        with open(result_file) as f:
            return json.load(f)


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
    elif event_type == "element":

        print(e)
        if e["msg"].startswith("infusion check picked up"):
            return e["msg"]

        assert e["msg"] == "application"
        assert e["logs"]["target"] == 1

        def format_auras(value: Optional[Dict[str, float]]) -> str:
            if value is None:
                return "none"
            return ", ".join(v.replace(": ", "=") for v in sorted(value))

        return "{:15s} | {:20s} -> {:20} | {}".format(
            raw_data["char_names"][e["char_index"]],
            format_auras(e["logs"]["existing"]),
            format_auras(e["logs"]["after"]),
            e["logs"]["abil"],
        )
    else:
        return "-"


@main.command("show-damages")
@click.argument("result-file", type=pathlib.Path)
def do_show_damages(result_file):
    raw_data = load_result(result_file)
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
    raw_data = load_result(result_file)
    data = json.loads(raw_data["debug"])

    for e in data:
        print(
            "T={:5.2f} | {:10s} | {}".format(
                e["frame"] / 60.0, e["event"], format_event(e, raw_data=raw_data)
            )
        )


if __name__ == "__main__":
    main()
