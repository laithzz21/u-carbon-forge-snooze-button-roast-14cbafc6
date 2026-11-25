#!/usr/bin/env python3
"""Snooze Button Roast — make.fun bounty u-carbon-forge-snooze-button-roast-14cbafc6.

One line (<=200 chars) roasting an alarm clock for ringing at 6 AM
on a Saturday morning. Prints the roast to stdout and writes it to a
unique output path so concurrent sweep entries never collide.

The roast stays a single line on purpose: the bounty brief asks for
exactly one line, so no extra lines, no trailing jokes, no hashtags.
"""

import os

ENTRY = (
    "Dear alarm clock: it's 6 AM on a Saturday. The only thing you "
    "should be waking is your own sense of shame. Snooze, traitor."
)

OUTPUT_PATH = "/tmp/sweep27-u-carbon-forge-snooze-button-roast-14cbafc6/entry.txt"


def main() -> None:
    # Sanity-check the brief's hard limit before producing any output.
    assert len(ENTRY) <= 200, f"entry is {len(ENTRY)} chars, limit is 200"
    print(ENTRY)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
