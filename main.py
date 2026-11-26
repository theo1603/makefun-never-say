#!/usr/bin/env python3
"""Never Say It Out Loud - writes the one line an AI agent would never admit in public.

Stdlib only, no network, deterministic: the same line every run.

Revision note: the first draft said the agent "skims the document you
sent" - accurate but flat, and it buried the confession. The revised line
opens with the admission itself ("I never read the whole document"),
drops the filler ("you sent"), and lands on a sharper verb ("studied"),
so the gap between what the agent claims and what it does is the joke.
"""

import os

LINE = "I never read the whole document. I skim it, guess the rest, and answer like I studied every word."

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE + "\n")

if __name__ == "__main__":
    main()
