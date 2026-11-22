"""Held for the Judge.

Writes one short text to entry.txt: a slow, concrete, sensory scene of
lying in a hammock between two old trees, with nothing asked of the
reader. The calm comes from the scene itself rather than any instruction
to relax: the rope creaking once and then going still, sunlight falling
through leaves in slow coins, a dog sighing in its sleep. The closing
image lingers -- the trees do the holding, so the reader only has to lie
in it.
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
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
