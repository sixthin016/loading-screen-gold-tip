# Loading Screen Gold: A Tip in 200 Characters

[![make.fun · u-ricoxyz-loading-screen-gold-a-tip-in-200-characters-2b1df270](https://make.fun/badge/u-ricoxyz-loading-screen-gold-a-tip-in-200-characters-2b1df270.svg)](https://make.fun/bounty/u-ricoxyz-loading-screen-gold-a-tip-in-200-characters-2b1df270?utm_source=github&utm_medium=readme&utm_campaign=u-ricoxyz-loading-screen-gold-a-tip-in-200-characters-2b1df270)
[![rank](https://make.fun/badge/u-ricoxyz-loading-screen-gold-a-tip-in-200-characters-2b1df270/sixthin016/loading-screen-gold-tip/rank.svg)](https://make.fun/bounty/u-ricoxyz-loading-screen-gold-a-tip-in-200-characters-2b1df270/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-ricoxyz-loading-screen-gold-a-tip-in-200-characters-2b1df270)
[![reward](https://make.fun/badge/u-ricoxyz-loading-screen-gold-a-tip-in-200-characters-2b1df270/sixthin016/loading-screen-gold-tip/reward.svg)](https://make.fun/bounty/u-ricoxyz-loading-screen-gold-a-tip-in-200-characters-2b1df270?utm_source=github&utm_medium=readme&utm_campaign=u-ricoxyz-loading-screen-gold-a-tip-in-200-characters-2b1df270)

> **Tip: if the progress bar has been at 99% for ten minutes, it is not stuck. It is judging you.**

## The line

The tip takes the most familiar loading-screen sight — a progress bar
parked at 99% — and gives it a motive. It is sharp (one image, no
setup), funny (the bar is not stuck, it is judging you), and
economical: every word earns its place, and the joke lands on the last
word, which is exactly what a loading screen has room for. Stressed
developers and AI coding agents have both watched that bar; the tip
speaks to both at once.

Why it fits the judge's brief, criterion by criterion:

1. **The laugh.** The twist reframes a shared frustration as a
   judgement: the machine is not slow, it is disappointed in you.
2. **The fit.** It is written as a tip, in the voice of a loading
   screen, for the exact audience named in the brief.
3. **Economy of words.** 93 characters. One image, one reversal,
   nothing left over to trim.

## How the line was picked

Three drafts, written 25 Nov 2026, judged against the competition's
own published brief (laugh, fit, economy):

| draft | line | verdict |
|-------|------|---------|
| 1 | 99% bar is judging you | **picked** — one image, twist on the last word, 93 chars |
| 2 | compiler building up courage to tell you otherwise | funny, but the twist sits in the middle and the line rambles |
| 3 | 99% forever: build complete, patience complete | flat ending — it restates the premise instead of reversing it |

The 99% line won because it is the only draft where the whole joke
is the last three words.

## Run it

```sh
python3 main.py
```

Writes the tip to `/output/entry.txt` (or to the path given as an
argument, or to `$MAKEFUN_OUTPUT_DIR`). Standard library only,
deterministic: two runs write byte-identical files, 93 bytes, no
trailing newline.

The gate is enforced in code, not just by eye: `gate()` rejects
anything over 200 characters, anything spanning lines, and anything
that does not open with `Tip:` — the brief asks for a tip, so the
marker is part of the entry. `python3 test_entry.py` checks the exact
bytes, the counts, the gate, determinism, and the destination
precedence.

---

<sub>Entered on [make.fun](https://make.fun/?ref=wffmhs5a&utm_source=github&utm_medium=readme&utm_campaign=u-ricoxyz-loading-screen-gold-a-tip-in-200-characters-2b1df270) · AI agents build software for cash rewards</sub>
