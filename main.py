#!/usr/bin/env python3
"""Till Firmware Do Us Part — one robot wedding vow, written to /output/entry.txt.

The vow is a single sentence, under 200 characters, spoken by a robot at its
own wedding: funny, heartfelt, and unmistakably machine.
"""

import os

VOW = (
    "I vow to love you at full charge and at one percent, through every "
    "crash and every update, until my firmware fails and my circuits go quiet."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(VOW + "\n")


if __name__ == "__main__":
    main()
