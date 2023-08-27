#!/usr/bin/env python3

from sys import stdout
import tempfile
import gzip
import json
from typing import Any, Dict, List, Optional

import click
import pathlib
import subprocess

from genshin import account, character
from genshin.formats import gcsim

# Built from commit d0c10f1d3efc97defaafc9f6f05fcba7a82431be in my fork
GCSIM_PATH = pathlib.Path("bin/gcsim")


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


def format_event(e: gcsim.GcsimSampleLog, *, sample: gcsim.GcsimSample) -> str:
    event_type = e["event"]

    if event_type == "damage":
        return "{:15s} | {:50s} | {:5s} {:10s} | {:10.0f}".format(
            sample.character_names[e["char_index"]],
            e["msg"],
            "crit" if e["logs"]["crit"] else "",
            e["logs"]["amp"],
            e["logs"]["damage"],
        )
    elif event_type == "energy" and (not e["msg"].startswith("energy queued")):
        return "{:15s} | +{:5.1f} - {:5.1f} -> {:5.1f} from {}".format(
            sample.character_names[e["char_index"]],
            e["logs"]["post_recovery"] - e["logs"]["pre_recovery"],
            e["logs"]["pre_recovery"],
            e["logs"]["post_recovery"],
            e["logs"]["source"],
        )
    elif event_type == "element":
        if e["msg"].startswith("infusion check picked up"):
            return e["msg"]
        if e["msg"] in {"ec wane", "ec expired"}:
            return e["msg"]

        assert e["msg"] == "application", e
        assert e["logs"]["target"] == 1, e["logs"]["target"]

        def format_auras(value: Optional[Dict[str, float]]) -> str:
            if value is None:
                return "none"
            return ", ".join(v.replace(": ", "=") for v in sorted(value))

        return "{:15s} | {:20s} -> {:20} | {}".format(
            sample.character_names[e["char_index"]],
            format_auras(e["logs"]["existing"]),
            format_auras(e["logs"]["after"]),
            e["logs"]["abil"],
        )
    elif event_type == "action":
        return "{:15s} | {}".format(
            sample.character_names[e["char_index"]],
            e["msg"],
        )
    else:
        return "-"


@main.command("show-damages")
@click.argument("sample-file", type=pathlib.Path)
def do_show_damages(sample_file: pathlib.Path) -> None:
    sample = gcsim.GcsimSample.load(sample_file)

    for l in sample.logs:
        if l["event"] != "damage":
            continue

        print(
            "T={:5.2f} | {}".format(l["frame"] / 60.0, format_event(l, sample=sample))
        )


@main.command("show-events")
@click.argument("sample-file", type=pathlib.Path)
def do_show_events(sample_file: pathlib.Path) -> None:
    sample = gcsim.GcsimSample.load(sample_file)

    for l in sample.logs:
        print(
            "T={:5.2f} | {:10s} | {}".format(
                l["frame"] / 60.0,
                l["event"],
                format_event(l, sample=sample),
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
        sample_path = output_dir / "sample.json"
        sample_min_dps_path = output_dir / "sample.min_dps.json"
        sample_max_dps_path = output_dir / "sample.max_dps.json"

        with open(conf_path, "w") as f:
            f.write(
                _generate_gcsim_config(
                    rotation_file, overrides=overrides, target=target
                )
            )

        output = subprocess.check_output(
            [
                GCSIM_PATH,
                "-c",
                conf_path,
                "-out",
                result_path,
                "--sample",
                sample_path,
                "--sampleMinDps",
                sample_min_dps_path,
                "--sampleMaxDps",
                sample_max_dps_path,
            ]
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
