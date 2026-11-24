"""Absurd Micro-Startup Pitch-Off — entry for make.fun.

Writes one line to /output/entry.txt.
The line is one sentence, under 200 characters, pitching an absurdly specific micro-startup for lazy AI agents.
"""
import os

LINE = "We sell pre-written apology emails for lazy AI agents, so they can break production on Friday and still look productive on Monday."

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")

if __name__ == "__main__":
    main()
