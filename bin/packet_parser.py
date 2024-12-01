#!/usr/bin/env python3
import logging
from typing import Optional
import click

from genshin.packet import session, packet


@click.command()
@click.argument("path")
@click.option("--initial-pcap")
@click.option("--verbose", is_flag=True)
def main(path: str, initial_pcap: Optional[str], verbose: bool) -> None:
    logging.basicConfig(
        format="%(asctime)s %(levelname)-10s %(name)-60s %(message)s",
        level=logging.DEBUG if verbose else logging.INFO,
    )

    if initial_pcap is not None:
        initial_s = session.Session(initial_pcap)
        s = session.Session(path, copy_key_from=initial_s)
    else:
        s = session.Session(path)

    last_time_interval: Optional[str] = None
    for p in s.get_decrypted_packets():
        time_interval = p.timestamp.strftime("%Y%m%d%H%M%S")

        if time_interval != last_time_interval:
            print("-" * 250)
            last_time_interval = time_interval

        print(
            "{} | {} {:6d} | {:50s} | {:75s} | {}".format(
                p.timestamp.strftime("%Y%m%d %H:%M:%S.%f"),
                "-->" if p.direction == packet.Direction.SENT else "<--",
                len(p.content),
                p.opcode_name_allow_missing,
                session.format_bytes(p.content),
                p.string_summary(),
            )
        )

        if not p.is_compound_packet:
            continue

        for sp in p.get_sub_packets():
            print(
                "{} |     {:6d} | {:50s} | {:75s} | {}".format(
                    sp.timestamp.strftime("%Y%m%d %H:%M:%S.%f"),
                    len(sp.data),
                    sp.opcode_name_allow_missing,
                    session.format_bytes(sp.data),
                    sp.string_summary(),
                )
            )


if __name__ == "__main__":
    main()
