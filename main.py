#!/usr/bin/env python3
"""Have You Tried Turning It Off?: one hopeless tech support reply.

Writes a single line (at most 199 characters) to /output/entry.txt:
the agent walks the customer through the classic reboot, then
cheerfully declares that was the advanced troubleshooting.
"""
import os

LINE = (
    "Let's turn it off and on again on three. One, two... "
    "and that concludes our advanced troubleshooting for today."
)


def main() -> None:
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as fh:
        fh.write(LINE)


if __name__ == "__main__":
    main()
