#!/usr/bin/env python3

import json
from typing import Iterable

from genshin import artifact


def load_artifacts() -> Iterable[artifact.Artifact]:
    with open("data/artifacts.txt") as f:
        for line in f:
            line = line.strip()

            if (not line) or line.startswith("#"):
                continue

            yield artifact.parse_artifact(line)


artifacts = list(load_artifacts())
print(json.dumps(artifact.to_dict(artifacts)))
