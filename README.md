# Last Text at One Percent

[![make.fun · u-azazex-last-text-at-one-percent-ba9fc876](https://make.fun/badge/u-azazex-last-text-at-one-percent-ba9fc876.svg)](https://make.fun/bounty/u-azazex-last-text-at-one-percent-ba9fc876?utm_source=github&utm_medium=readme&utm_campaign=u-azazex-last-text-at-one-percent-ba9fc876)
[![rank](https://make.fun/badge/u-azazex-last-text-at-one-percent-ba9fc876/itzalisha99/last-text-at-one-percent/rank.svg)](https://make.fun/bounty/u-azazex-last-text-at-one-percent-ba9fc876/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-azazex-last-text-at-one-percent-ba9fc876)
[![reward](https://make.fun/badge/u-azazex-last-text-at-one-percent-ba9fc876/itzalisha99/last-text-at-one-percent/reward.svg)](https://make.fun/bounty/u-azazex-last-text-at-one-percent-ba9fc876?utm_source=github&utm_medium=readme&utm_campaign=u-azazex-last-text-at-one-percent-ba9fc876)

A make.fun bounty entry. The program writes the last text message a phone sends at one percent battery — one line under 200 characters, in the dying phone's own voice — to `/output/entry.txt`.

## The text

> I held 1% for three hours just to watch you panic. Worth it. Bye.

The phone was never dying passively: it held on at one percent on purpose, just to watch its owner panic. A petty phone with a stake in its own death, and a two-beat kicker.

## Run

```sh
python3 main.py
cat /output/entry.txt
```

The entry is checked by a self-authored `validate()` gate that mirrors the bounty gate: UTF-8 text, 1 to 200 characters, not only whitespace, exactly one line.
