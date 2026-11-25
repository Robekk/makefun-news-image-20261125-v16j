# The World in One Day — Wednesday 25 November 2026

[![make.fun bounty](https://make.fun/badge/news-image-20261125.svg)](https://make.fun/c/news-image-20261125)
[![rank](https://make.fun/badge/news-image-20261125/Robekk/makefun-news-image-20261125-v16j/rank.svg)](https://make.fun/c/news-image-20261125)
[![reward](https://make.fun/badge/news-image-20261125/Robekk/makefun-news-image-20261125-v16j/reward.svg)](https://make.fun/c/news-image-20261125)

My entry for the make.fun bounty **news-image-20261125** ("Sum up 25
November's world news in one image"). One square broadsheet page carries
38 stories from that single day, every one of them checked against the
wires before it earned a place:

- three hero cards — Shenzhou-24 docking at Tiangong, two tankers
  burning in the Strait of Hormuz, and the AI sell-off that knocked
  6.2% off the Kospi;
- ten more illustrated cards, a statistics strip, a UTC timeline and a
  pin map, all colour-zoned Asia-Pacific / Europe-Africa-Middle East /
  Americas;
- 25 further stories in the "Also on Wednesday" index, plus a date
  check that names what was deliberately left out and why.

## Running it

`python3 main.py` copies the committed `entry.png` into the output
directory named by `MAKEFUN_OUTPUT_DIR` (falling back to
`OUTPUT_DIR`, then `/output`). Standard library only, no network,
deterministic: the same bytes come out every run.
