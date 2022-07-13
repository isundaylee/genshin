#!/usr/bin/env python3

from collections import Set
import json
import pathlib
from typing import DefaultDict, Dict, List

import click
import tabulate

from genshin import account, artifact, character


@click.group()
def main():
    pass


@main.command("print-json")
def do_print_json():
    artifacts = account.Account.load(pathlib.Path("data")).artifacts
    print(json.dumps(artifact.to_dict(artifacts)))


USEFUL_SUBSTATS: Dict[
    character.CharacterName, Dict[artifact.ArtifactStatType, float]
] = {
    character.CharacterName.Yanfei: {
        artifact.ArtifactStatType.CR_PCT: 1.0,
        artifact.ArtifactStatType.CD_PCT: 1.0,
        artifact.ArtifactStatType.EM: 1.0,
        artifact.ArtifactStatType.ATK_PCT: 0.4,
    }
}


@main.command("show-scores")
def do_show_scores():
    ac = account.Account.load(pathlib.Path("data"))
    stat_order: List[artifact.ArtifactStatType] = [
        artifact.ArtifactStatType.CR_PCT,
        artifact.ArtifactStatType.CD_PCT,
        artifact.ArtifactStatType.ATK_PCT,
        artifact.ArtifactStatType.EM,
        artifact.ArtifactStatType.ER_PCT,
        artifact.ArtifactStatType.HP_PCT,
        artifact.ArtifactStatType.DEF_PCT,
    ]

    header: List[str] = []
    header.append("Character")
    for s in stat_order:
        header.append(s.name)
    header.append("Score")

    rows: List[List[str]] = [header]

    for c in ac.characters.values():
        row: List[str] = []

        if c.name != character.CharacterName.Yanfei:
            continue

        scores: Dict[artifact.ArtifactStatType, float] = artifact.get_artifact_scores(
            c.artifacts,
            c,
            convert_nopct_stats=True,
        )

        score = 0.0
        for t, r in USEFUL_SUBSTATS[c.name].items():
            if t in scores:
                score += r * scores[t]

        row.append(c.name.name)
        for s in stat_order:
            if s in scores:
                row.append(f"{scores[s]:.2f}")
            else:
                row.append("")
        row.append(f"{score:.2f}")

        rows.append(row)

    print(tabulate.tabulate(rows))


if __name__ == "__main__":
    main()
