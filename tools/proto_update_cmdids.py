#!/usr/bin/env python3
import logging
import pathlib

logger = logging.getLogger(__name__)


def main() -> None:
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s.%(msecs)03d %(levelname)s %(name)-35s %(message)s",
        datefmt="%Y%m%d %H:%M:%S",
    )

    mapping = dict[str, int]()

    for child in pathlib.Path("resources/proto").iterdir():
        name = child.with_suffix("").name

        for l in child.read_text().splitlines():
            if "CmdId: " not in l:
                continue

            try:
                mapping[name] = int(l.strip().split()[-1])
            except ValueError:
                logger.warning("Skipping l %s", l)

            break
        else:
            logger.warning("No CmdId found for %s", name)

    with pathlib.Path("genshin/packet/opcodes.py").open("w") as f:
        f.write("import enum\n")
        f.write("\n")
        f.write("\n")
        f.write("class Opcode(enum.IntEnum):\n")
        for k, v in mapping.items():
            f.write(f"    {k} = {v}\n")


if __name__ == "__main__":
    main()
