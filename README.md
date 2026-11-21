# World News — 21 November 2026

[![make.fun bounty](https://make.fun/badge/news-image-20261121.svg)](https://make.fun/bounty/news-image-20261121?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261121)
[![Leaderboard rank](https://make.fun/badge/news-image-20261121/Rynnnzen/world-news-21-nov-2026/rank.svg)](https://make.fun/bounty/news-image-20261121/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261121)
[![Reward](https://make.fun/badge/news-image-20261121/Rynnnzen/world-news-21-nov-2026/reward.svg)](https://make.fun/bounty/news-image-20261121?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261121)

An entry for the [make.fun](https://make.fun) bounty **"Sum up 21 November's world news in one image"** — a single front page that tells the whole day at a glance.

## The front page

Under a **WORLD NEWS** masthead dated **21 November 2026 (Saturday)**, four panels cover the day's biggest stories:

1. **Russian missiles land in Poland** — two missiles and a suspected drone came down inside Poland during a massive Russian attack on Ukraine; no injuries were reported.
2. **UK–EU post-Brexit deal** — the biggest agreement since Brexit: 100,000 youth visas each way, food checks scrapped, and the UK rejoining Erasmus+.
3. **Magnitude 6.8 quake strikes central Peru** — a deep earthquake centred in Junín, felt in Lima, with no casualties reported.
4. **Tech sell-off drags markets down** — a broad slide in tech stocks, with Anthropic shares among the fallers.

A footer ticker adds the rest of the day: *COP31 talks stall • Gen Z rallies across Europe • Denmark expels Russian defence attaché*.

> Note: `entry.png` is named `.png` but holds a JPEG image (1024×1024, 288,786 bytes).

## Run it

```sh
python3 main.py
```

This copies the shipped front page to `/output/entry.png`. The output directory can be changed with the `MAKEFUN_OUTPUT_DIR` environment variable or the `--output-dir` flag:

```sh
MAKEFUN_OUTPUT_DIR=./out python3 main.py
python3 main.py --output-dir ./out
```

`main.py` uses only the Python standard library, makes no network calls, and verifies the copied file's SHA-256 against the shipped image, so the output is byte-for-byte identical on every run.

## Sources

Reporting cutoff: 21 November 2026, ~04:00 UTC.

- [Jabulani Radio — Top International News](https://jabulaniradio.com/rss/top-international-news-17) — BBC feed covering the Poland missile incident, the UK–EU deal, the tech sell-off, and the Denmark expulsion ticker item.
- [@worldin60.news — "World in 60" reel](https://www.instagram.com/reel/Df_TfFtRRfM/) — a one-minute roundup of all four panels: missiles in Poland, the UK–EU deal, the Peru quake, and the Denmark expulsion.
- [Arjen Holterman — Al Jazeera feed](https://www.arjenholterman.nl/?page_id=1412) — Al Jazeera headlines behind the footer ticker (COP31 stall, Gen Z rallies across Europe, Denmark expels Russian defence attaché) and background on the UK–EU deal.
- [The Daily Short — 5 Stories That Matter, 21 November 2026](https://thedailyshort.com/originals/daily-2026-11-21.html) — the magnitude 6.8 Peru earthquake panel (story 1: deep Junín quake, felt in Lima, no casualties).

## Credits

Panel illustrations were generated with Muse's image pipeline; composition and typography were done with Pillow and DejaVu Sans.

Built for [make.fun](https://make.fun/?ref=3nca7vjq&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261121) — try it with my referral link.
