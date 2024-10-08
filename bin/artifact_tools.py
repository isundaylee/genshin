#!/usr/bin/env python3

import json
import pathlib
from typing import Set, Dict, List

import click
import tabulate

from genshin import account, artifact, character


@click.group()
def main():
    pass


@main.command("print-json")
def do_print_json() -> None:
    artifacts = account.Account.load(pathlib.Path("data")).artifacts
    print(json.dumps(artifact.to_dict(artifacts)))


_USEFUL_SUBSTATS: Dict[
    character.CharacterName, Dict[artifact.ArtifactStatType, float]
] = {
    character.CharacterName.Yanfei: {
        artifact.ArtifactStatType.CR_PCT: 1.0,
        artifact.ArtifactStatType.CD_PCT: 1.0,
        artifact.ArtifactStatType.EM: 1.0,
        artifact.ArtifactStatType.ATK_PCT: 1.0,
    },
    character.CharacterName.Furina: {
        artifact.ArtifactStatType.CR_PCT: 1.0,
        artifact.ArtifactStatType.CD_PCT: 1.0,
        artifact.ArtifactStatType.HP_PCT: 1.0,
    },
}


@main.command("show-scores")
def do_show_scores() -> None:
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
    header.append("CV")

    rows: List[List[str]] = [header]

    for c in ac.characters.values():
        row: List[str] = []

        if c.name not in _USEFUL_SUBSTATS:
            continue

        # Compute artifact score

        scores: Dict[artifact.ArtifactStatType, float] = artifact.get_artifact_scores(
            c.artifacts,
            c,
            convert_nopct_stats=True,
        )

        score = 0.0
        for t, r in _USEFUL_SUBSTATS[c.name].items():
            if t in scores:
                score += r * scores[t]

        # Compute CV (crit-value)

        cv = sum(
            ss.stat_value
            * {
                artifact.ArtifactStatType.CR_PCT: 200.0,
                artifact.ArtifactStatType.CD_PCT: 100.0,
            }.get(ss.stat_type, 0.0)
            for a in c.artifacts
            for ss in [a.main_stat, *a.sub_stats]
        )

        # Display table

        row.append(c.name.name)
        for s in stat_order:
            if (s in scores) and (s in _USEFUL_SUBSTATS[c.name]):
                row.append(f"{scores[s]:.2f}")
            else:
                row.append("")
        row.append(f"{score:.2f}")
        row.append(f"{cv:.2f}")

        rows.append(row)

    print(tabulate.tabulate(rows))


if __name__ == "__main__":
    main()
