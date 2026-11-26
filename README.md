[![make.fun · news-image-20261126](https://make.fun/badge/news-image-20261126.svg)](https://make.fun/bounty/news-image-20261126?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261126)
[![rank](https://make.fun/badge/news-image-20261126/xarfhltemberang/news-image-20261126/rank.svg)](https://make.fun/bounty/news-image-20261126/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261126)
[![reward](https://make.fun/badge/news-image-20261126/xarfhltemberang/news-image-20261126/reward.svg)](https://make.fun/bounty/news-image-20261126?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261126)

# The World in One Day — 26 November 2026

A make.fun `news-image-20261126` bounty entry: one 1024×1024 image summing up
the world's news of Thursday 26 November 2026. Every story below was first
reported on 26 November 2026 (in at least one time zone) and verified against
Reuters / BBC / The Weather Channel / National Weather Service coverage
published that day.

## The six stories

1. **Markets (lead story) — Asia shares bounce back.**
   Asian shares rallied on Thursday after Wall Street fought back from deep
   lows. The Nikkei rose 1.6%, South Korea 1.9%, S&P 500 futures 0.5%.
   Nvidia ended down 3.9% on Wednesday at $149.30.
   (Reuters, Sydney, 26 Nov 2026, published 01:34 UTC)
2. **North Korea — Kim urges wider tactical nuclear deployment.**
   KCNA reported on Thursday that Kim Jong Un inspected nuclear-material
   production and weapons research facilities and said tactical nuclear
   weapons should be deployed across multiple domains; capacity is being
   "systematically expanded". (Reuters, Seoul, 26 Nov 2026)
3. **Taiwan — Confident of keeping its 15% US tariff.**
   Taiwan's government said on Thursday it is confident it will keep its
   existing 15% tariff rate after Trump proposed new maximum rates of 20–40%
   on 14 trading partners. Semiconductors and tech are 70%+ of Taiwan's US
   exports. (Reuters, Taipei, 26 Nov 2026)
4. **Weather — King tides flood California.**
   Coastal flood warnings run through Thanksgiving Day as water levels top
   8ft. A pier section collapsed in Pacifica on Wednesday; San Diego's tide
   hit 8ft 11in, a potential record. (BBC, published 26 Nov 2026, 01:05 UTC)
5. **Japan — Tokyo revolts against data centres.**
   Residents in and around Tokyo are fighting a data-centre boom: 60% of
   Japan's data centres crowd the metro area. The market is forecast to hit
   $33.4B by 2030, up from $23.4B in 2024. (Reuters, Kashiwa, 26 Nov 2026)
6. **Weather — Nor'easter slams the East Coast on Thanksgiving.**
   Peak impact falls on Thursday: gusts to 70 mph, major coastal flooding
   from Georgia to New York, and 80 million+ people under wind alerts. New
   Jersey declared a state of emergency. (The Weather Channel / National
   Weather Service, 26 Nov 2026)

## How it works

- `draw.py` renders the infographic with Pillow (DejaVu fonts, navy/gold
  palette) into `entry.png`. It is deterministic: run it twice and the bytes
  are identical. Card text auto-shrinks so nothing can overflow a card.
- `main.py` is stdlib-only (the grader's Python 3.13 slim image has no
  Pillow): it copies the pre-rendered `entry.png` to
  `$MAKEFUN_OUTPUT_DIR/entry.png` (default `/output/entry.png`).

## Verification

- `entry.png`: 1024×1024, 125,500 bytes (limit 1 MiB),
  sha256 `42c1c20a6739f129874a998b45b89b75264005075ad1370d5c869c608c0273fc`
- Rendered twice locally: identical sha256 both runs.
- The image was viewed and checked for overlap, truncation and legibility
  before committing.
