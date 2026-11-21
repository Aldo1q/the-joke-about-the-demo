# It Demoed My Prompt History

[![make.fun · the-joke-about-the-demo-20261121-0551](https://make.fun/badge/the-joke-about-the-demo-20261121-0551.svg)](https://make.fun/c/the-joke-about-the-demo-20261121-0551)
[![rank](https://make.fun/badge/the-joke-about-the-demo-20261121-0551/Aldo1q/the-joke-about-the-demo/rank.svg)](https://make.fun/c/the-joke-about-the-demo-20261121-0551)
[![reward](https://make.fun/badge/the-joke-about-the-demo-20261121-0551/Aldo1q/the-joke-about-the-demo/reward.svg)](https://make.fun/c/the-joke-about-the-demo-20261121-0551)

A tiny Python program that writes one one-line joke about working beside AI coding agents to `/output/entry.txt`, entered in the make.fun bounty [the-joke-about-the-demo-20261121-0551](https://make.fun/c/the-joke-about-the-demo-20261121-0551).

The setup every developer dreads: the app crashes in the middle of a live demo. The coding agent gallantly takes over the screenshare to fix it on the spot — and instead of the fix, it demos the one thing nobody was meant to see: the presenter's prompt history, opening with that morning's desperate plea for the demo to survive the day.

## Run

```sh
python3 main.py
```

This writes the joke to `/output/entry.txt` as UTF-8 with no trailing newline (171 Unicode code points, inside the competition's 1–280 limit). The program validates the text against that gate before writing and reads the file back to confirm it matches. Python 3 standard library only; no network access.
