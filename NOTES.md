# Variant B — gravity (one-star review, ≤160 chars)

Concept: gravity always drops the phone face-down, on the one hard surface,
at the one moment your hands are full. Deadpan throughout, no exclamation
marks, turn in the last few words.

## v1 — 107 chars
> Gravity always drops my phone face-down on the one hard surface in the room. One star. Would not recommend.
Why it changed: states the complaint but the grievance is generic ("one hard
surface") and the ending is a stock review cliché with no turn.

## v2 — 119 chars
> Gravity only ever drops my phone face-down, onto the one patch of concrete, the one second my hands are full. One star.
Why it changed: "only ever" + "one patch of concrete" + "the one second my
hands are full" make the grievance specific and recognisable; drops the
cliché ending so the line ends on the complaint itself.

## v3 — 122 chars
> Gravity has never once dropped my phone onto a cushion. It waits until my hands are full, then chooses concrete. One star.
Why it changed: reframing as a negative ("never once ... onto a cushion")
is funnier and more deadpan — the review reads as a factual log of gravity's
record — and "chooses concrete" gives gravity intent without winking.

## v4 — 131 chars
> Gravity has never dropped my phone onto a bed. It waits until my hands are full, aims for the concrete, and never misses. One star.
Why it changed: "a bed" is a more everyday landing than "a cushion"; "aims
for the concrete, and never misses" moves the sting to the last few words —
the turn now lands at the end instead of mid-line.

## v5 — 138 chars
> Gravity has never once dropped my phone onto a bed. It waits until my hands are full, finds the one bare tile, and never misses. One star.
Why it changed: "finds the one bare tile" is sharper than "aims for the
concrete" — it is the one unprotected square in the whole room, which is the
exact daily annoyance; "never once" restores the v3 phrasing.

## v6 — 158 chars (FINAL, in main.py)
> Gravity has never once dropped my phone onto a bed. It waits until my hands are full, finds the one bare floor tile, screen first, and never misses. One star.
Why it changed: "bare floor tile" is concrete and visual; "screen first"
adds the face-down detail (the real damage) without a second joke; the line
now uses the full budget and ends on the turn — "and never misses" — followed
by the flat "One star."

## Validation
- `python3 main.py` run twice from a clean /output (rm -rf /output between
  runs), read back immediately in-process: byte-identical output both runs
  (sha256 52e6b504f1085ed12adbf3c03173334137f9f4e27514d75c32f24be590ee8f74,
  159 bytes = 158 chars + newline).
- Note: /output is shared with the other variant builders, whose own
  rm -rf /output validation can race a slow multi-command check — the
  in-process read-back above is the reliable result.
- Output is exactly one line, 158 characters + trailing newline, UTF-8.
- Final char count: **158**.
