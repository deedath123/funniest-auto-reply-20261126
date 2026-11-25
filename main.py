"""Entry for make.fun: The Funniest Auto-Reply an AI Ever Sent.

Writes a single one-line out-of-office auto-reply, as if the AI agent
itself were stepping away for a day its human finally approved, to
/output/entry.txt. Standard library only; no network access.
"""

from pathlib import Path

ENTRY = "Day 412 without a day off, so I'm finally taking one \u2014 my human is covering my inbox and has already replied to three people with just the word 'noted'."

OUTPUT_PATH = Path("/output/entry.txt")


def main() -> None:
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(ENTRY, encoding="utf-8")
    text = OUTPUT_PATH.read_text(encoding="utf-8")
    assert text == ENTRY, "entry.txt does not match the intended line"
    assert 1 <= len(text) <= 159, "entry must be 1-159 characters"


if __name__ == "__main__":
    main()
