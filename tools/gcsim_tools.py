#!/usr/bin/env python3

from sys import stdout
import tempfile
from genshin import account, gcsim, weapon, character
import gzip
import json
from typing import Any, Dict, List, Optional
import click
import pathlib
import subprocess

GCSIM_PATH = pathlib.Path("/Users/jiahaoli/Programming/Git/gcsim/cmd/gcsim/gcsim")


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
        return "{:15s} | {:50s} | {:5s} {:10s} | {:10.0f}".format(
            raw_data["char_names"][e["char_index"]],
            e["msg"],
            "crit" if e["logs"]["crit"] else "",
            e["logs"]["amp"],
            e["logs"]["damage"],
        )
    elif event_type == "energy" and (not e["msg"].startswith("energy queued")):
        print(e)
        return "{:15s} | {:5} -> {:5.1f} from {}".format(
            raw_data["char_names"][e["char_index"]],
            "{:5.1f}".format(e["logs"]["pre_recovery"])
            if "pre_recovery" in e["logs"]
            else "???",
            e["logs"]["post_recovery"],
            e["logs"]["source"],
        )
    elif event_type == "element":
        if e["msg"].startswith("infusion check picked up"):
            return e["msg"]
        if e["msg"] in {"ec wane", "ec expired"}:
            return e["msg"]

        assert e["msg"] == "application", e
        assert e["logs"]["target"] == 0, e["logs"]["target"]

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
    elif event_type == "action":
        return "{:15s} | {}".format(
            raw_data["char_names"][e["char_index"]],
            e["msg"],
        )
    else:
        return "-"


@main.command("show-damages")
@click.argument("result-file", type=pathlib.Path)
@click.option("--debug-log-flavor", default="debug")
def do_show_damages(result_file: pathlib.Path, debug_log_flavor: str) -> None:
    raw_data = load_result(result_file)
    data = json.loads(raw_data[debug_log_flavor])

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
@click.option("--debug-log-flavor", default="debug")
def do_show_events(result_file: pathlib.Path, debug_log_flavor: str) -> None:
    raw_data = load_result(result_file)
    data = json.loads(raw_data[debug_log_flavor])

    for e in data:
        print(
            "T={:5.2f} | {:10s} | {}".format(
                e["frame"] / 60.0, e["event"], format_event(e, raw_data=raw_data)
            )
        )


def _generate_gcsim_config(
    rotation_file: pathlib.Path, *, overrides: Optional[str], target: str
) -> str:
    ac = account.Account.load(pathlib.Path("data"))
    if overrides is not None:
        ac.apply_overrides(overrides)

    with open(rotation_file) as f:
        header = next(f)
        _, team_str = header.strip().split("# team=")
        team = [character.CharacterName[c] for c in team_str.split(",")]

        rotation = f.read()

    return gcsim.generate_gcsim_config(
        [ac.characters[c] for c in team],
        actions=[rotation],
        target=target,
    )


@main.command("generate-config")
@click.argument("rotation_file", type=pathlib.Path)
@click.option("--target", default="target lvl=90 resist=0.1;")
def do_generate_config(rotation_file: pathlib.Path, target: str) -> None:
    print(_generate_gcsim_config(rotation_file, overrides=None, target=target))


@main.command("run-sim")
@click.argument("rotation_file", type=pathlib.Path)
@click.option("--baseline-overrides")
@click.option("--variant", multiple=True)
@click.option("--details", is_flag=True)
@click.option("--working-dir", type=pathlib.Path)
@click.option("--target", default="target lvl=90 resist=0.1;")
def do_run_sim(
    rotation_file: pathlib.Path,
    details: bool,
    baseline_overrides: Optional[str],
    variant: List[str],
    working_dir: Optional[pathlib.Path],
    target: str,
) -> None:
    if working_dir is None:
        working_dir = pathlib.Path(tempfile.mkdtemp(prefix="gcsim-"))

    def run_variant(
        output_dir: pathlib.Path, overrides: Optional[str]
    ) -> gcsim.GcsimSummary:
        conf_path = output_dir / "config.txt"
        stdout_path = output_dir / "stdout.txt"
        result_path = output_dir / "result.json"

        with open(conf_path, "w") as f:
            f.write(
                _generate_gcsim_config(
                    rotation_file, overrides=overrides, target=target
                )
            )

        output = subprocess.check_output(
            [GCSIM_PATH, "-c", conf_path, "-out", result_path, "-debugMinMax"]
        )

        with open(stdout_path, "wb") as f:
            f.write(output)

        if details:
            print(f"Stdout at: {stdout_path}")
            print(f"Result at: {result_path}")

        return gcsim.GcsimSummary.from_gcsim_output(output.decode())

    variants = {"baseline": None if baseline_overrides is None else baseline_overrides}
    for v in variant:
        k, v = v.split(":")
        if baseline_overrides is None:
            variants[k] = v
        else:
            variants[k] = baseline_overrides + "," + v

    baseline_summary: Optional[gcsim.GcsimSummary] = None

    for k, v in variants.items():
        variant_working_dir = working_dir / k
        variant_working_dir.mkdir(parents=True, exist_ok=True)
        summary = run_variant(variant_working_dir, v)

        if k == "baseline":
            baseline_summary = summary

        print(
            "{:15s} | duration {:5.1f}s | avg {:10.0f} ({:5.1f}%) | span {:10.0f} - {:10.0f} std {:10.0f}".format(
                k,
                summary.duration,
                summary.dps_avg,
                100.0 * (summary.dps_avg / baseline_summary.dps_avg - 1.0),
                summary.dps_min,
                summary.dps_max,
                summary.dps_std,
            )
        )


if __name__ == "__main__":
    main()
