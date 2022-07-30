#!/usr/bin/env python3
import logging
from typing import Optional
import click

from genshin.packet import session, packet


@click.command()
@click.argument("path")
@click.argument("my_ip")
@click.option("--initial-pcap")
def main(path: str, my_ip: str, initial_pcap: Optional[str]) -> None:
    logging.basicConfig(
        format="%(asctime)s %(levelname)-10s %(name)-60s %(message)s",
        level=logging.INFO,
    )

    if initial_pcap is not None:
        initial_s = session.Session(initial_pcap, my_ip)
        s = session.Session(path, my_ip, copy_key_from=initial_s)
    else:
        s = session.Session(path, my_ip)

    last_time_interval: Optional[str] = None
    for p in s.get_decrypted_packets():
        time_interval = p.timestamp.strftime("%Y%m%d%H%M%S")

        if time_interval != last_time_interval:
            print("-" * 100)
            last_time_interval = time_interval

        print(
            "{} | {} {:5d} | {:50s} | {}".format(
                p.timestamp.strftime("%Y%m%d %H:%M:%S.%f"),
                "-->" if p.direction == packet.Direction.SENT else "<--",
                len(p.content),
                p.opcode.name,
                session.format_bytes(p.content),
            )
        )

        if not p.is_compound_packet:
            continue

        for sp in p.get_sub_packets():
            print(
                "{} |           | {:50s} | {}".format(
                    sp.timestamp.strftime("%Y%m%d %H:%M:%S.%f"),
                    sp.opcode.name,
                    session.format_bytes(sp.data),
                )
            )


if __name__ == "__main__":
    main()
