#!/usr/bin/env python3

import json
import pathlib

import click

from genshin import account, artifact


@click.group()
def main():
    pass


@main.command("print-json")
def do_print_json():
    artifacts = account.Account.load(pathlib.Path("data")).artifacts
    print(json.dumps(artifact.to_dict(artifacts)))


if __name__ == "__main__":
    main()
