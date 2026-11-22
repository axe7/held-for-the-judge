"""Held for the Judge.

Writes one short text to entry.txt: a slow, concrete, sensory scene of
lying in a hammock between two old trees, with nothing asked of the
reader. The calm comes from the scene itself rather than any instruction
to relax: the rope creaking once and then going still, sunlight falling
through leaves in slow coins, a dog sighing in its sleep. The closing
image lingers -- the trees do the holding, so the reader only has to lie
in it.

Before writing, the entry is checked: it must be non-blank and between
1 and 280 Unicode code points, so a bad edit fails loudly instead of
producing a malformed entry.
"""

import os

TEXT = (
    "Late afternoon, a hammock holds you between two old trees, "
    "the rope creaking once, then still. "
    "Sun comes through the leaves in slow coins of light. "
    "Below, a dog sighs in its sleep. "
    "Nothing is wanted of you here. "
    "The trees do the holding; you only lie in it."
)


def main() -> None:
    if not TEXT.strip():
        raise ValueError("entry text must be non-blank")
    if not 1 <= len(TEXT) <= 280:
        raise ValueError(
            f"entry text must be 1-280 Unicode code points, got {len(TEXT)}"
        )
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
