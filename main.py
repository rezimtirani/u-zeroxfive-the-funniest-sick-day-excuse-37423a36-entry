"""The Funniest Sick-Day Excuse.

Writes one line to $MAKEFUN_OUTPUT_DIR/entry.txt: a funny reason to
call in sick, under 200 characters, fresh enough to beat the worn
fever-and-dog excuses and believable enough that a boss might half
buy it. Standard library only.
"""

import os

EXCUSE = (
    "My bed has officially gone on strike, my alarm clock joined the "
    "picket line, and my coffee maker filed a complaint -- I need "
    "today to negotiate with my own bedroom."
)


def check_excuse(text):
    """Check the excuse against the competition gate before writing.

    The gate needs UTF-8 text of 1 to 200 characters, not only white
    space, in a single line: one funny reason to call in sick and
    nothing else. Returns the cleaned text or raises ValueError.
    """
    cleaned = text.strip()
    if not cleaned:
        raise ValueError("excuse must not be only whitespace")
    if len(cleaned) > 200:
        raise ValueError("excuse is %d characters, over the 200 limit" % len(cleaned))
    if "\n" in cleaned or "\r" in cleaned:
        raise ValueError("excuse must be a single line")
    return cleaned


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(check_excuse(EXCUSE) + "\n")


if __name__ == "__main__":
    main()
