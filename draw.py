#!/usr/bin/env python3
"""Render the news-image entry for Thursday 26 November 2026.

PIL infographic, 1024x1024, deterministic: same input -> same bytes.
Run:  python3 draw.py   (writes entry.png next to this file)
"""
import os
from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
FONT_DIR = "/usr/share/fonts/truetype/dejavu"

# Palette: deep navy, gold accents, off-white text.
BG = (13, 27, 46)
CARD = (22, 39, 62)
LEAD_CARD = (29, 53, 87)
GOLD = (232, 184, 75)
GOLD_DIM = (201, 158, 58)
INK = (242, 240, 233)
MUTED = (169, 184, 204)
RULE = (46, 74, 107)

MARGIN = 36


def font(name, size):
    return ImageFont.truetype(os.path.join(FONT_DIR, name), size)


F_KICKER = font("DejaVuSans-Bold.ttf", 26)
F_TITLE = font("DejaVuSans-Bold.ttf", 62)
F_LABEL = font("DejaVuSans-Bold.ttf", 19)
F_FOOT = font("DejaVuSans.ttf", 16)
F_CREDIT = font("DejaVuSans.ttf", 15)


def wrap(d, text, f, max_w):
    """Greedy word wrap; returns list of lines that fit max_w."""
    lines, cur = [], ""
    for word in text.split():
        trial = (cur + " " + word).strip()
        if d.textlength(trial, font=f) <= max_w:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = word
    if cur:
        lines.append(cur)
    return lines


def fit_one_line(d, text, name, size, max_w, min_size=24):
    """Shrink a bold font until the text fits on one line."""
    while size > min_size:
        f = font(name, size)
        if d.textlength(text, font=f) <= max_w:
            return f
        size -= 1
    return font(name, min_size)


def card_height(head_lines, body_lines, head_f, body_f):
    """Vertical space a card's text needs, including label + padding."""
    return (16 + 30 + 12          # top pad + label + gold rule
            + head_lines * (head_f.size + 6)
            + 2
            + body_lines * (body_f.size + 7)
            + 12)                  # bottom pad


def draw_card(d, x, y, w, h, label, headline, body, fill,
              head_size, body_size, head_lines=2, body_lines=3,
              single_line_head=False):
    d.rounded_rectangle([x, y, x + w, y + h], radius=14, fill=fill)
    pad = 20
    cx = x + pad
    inner = w - 2 * pad
    head_f = font("DejaVuSans-Bold.ttf", head_size)
    body_f = font("DejaVuSans.ttf", body_size)

    if single_line_head:
        head_f = fit_one_line(d, headline, "DejaVuSans-Bold.ttf",
                              head_size, inner)
        head_wrapped = [headline]
    else:
        head_wrapped = wrap(d, headline, head_f, inner)[:head_lines]

    body_wrapped = wrap(d, body, body_f, inner)[:body_lines]
    # Auto-shrink: never let text spill past the card's bottom edge.
    while (card_height(len(head_wrapped), len(body_wrapped), head_f, body_f)
           > h and body_f.size > 15):
        body_f = font("DejaVuSans.ttf", body_f.size - 1)
        body_wrapped = wrap(d, body, body_f, inner)[:body_lines]
    while (card_height(len(head_wrapped), len(body_wrapped), head_f, body_f)
           > h and head_f.size > 20 and not single_line_head):
        head_f = font("DejaVuSans-Bold.ttf", head_f.size - 1)
        head_wrapped = wrap(d, headline, head_f, inner)[:head_lines]
    assert card_height(len(head_wrapped), len(body_wrapped),
                       head_f, body_f) <= h, (label, "card text overflows")

    cy = y + 16
    d.text((cx, cy), label, font=F_LABEL, fill=GOLD)
    cy += 30
    d.rectangle([cx, cy, cx + 44, cy + 3], fill=GOLD)
    cy += 12
    for line in head_wrapped:
        d.text((cx, cy), line, font=head_f, fill=INK)
        cy += head_f.size + 6
    cy += 2
    for line in body_wrapped:
        d.text((cx, cy), line, font=body_f, fill=MUTED)
        cy += body_f.size + 7
    return cy


def main():
    img = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(img)

    # ---- Header ----
    d.text((MARGIN, 30), "THE WORLD IN ONE DAY", font=F_KICKER, fill=GOLD)
    d.text((MARGIN, 62), "26 November 2026", font=F_TITLE, fill=INK)
    d.rectangle([MARGIN, 140, W - MARGIN, 143], fill=GOLD_DIM)

    # ---- Lead story: markets ----
    draw_card(
        d, MARGIN, 156, W - 2 * MARGIN, 158,
        "MARKETS  \u00b7  LEAD STORY",
        "Asia shares bounce back",
        "Nikkei +1.6%, South Korea +1.9% as Wall Street fights back from "
        "deep lows. S&P futures +0.5%. Nvidia ends down 3.9% at $149.30.",
        LEAD_CARD, 33, 21, head_lines=1, body_lines=2,
        single_line_head=True)

    # ---- 2x2 grid ----
    grid_y = 330
    card_w = (W - 2 * MARGIN - 16) // 2
    card_h = 196
    grid = [
        ("NORTH KOREA",
         "Kim urges wider nuclear deployment",
         "Kim inspects nuclear plants and orders tactical nuclear weapons "
         "spread across multiple domains."),
        ("TAIWAN  \u00b7  TRADE",
         "Taiwan confident of 15% US tariff",
         "Taipei says it will keep its 15% rate after Trump proposes "
         "20\u201340% caps on 14 partners. Chips are 70%+ of US exports."),
        ("WEATHER  \u00b7  CALIFORNIA",
         "King tides flood California",
         "Flood warnings run through Thanksgiving Day as tides top 8ft. "
         "A pier collapses in Pacifica; San Diego tide hits 8ft 11in."),
        ("JAPAN",
         "Tokyo revolts against data centres",
         "Residents near Tokyo fight a data-centre boom: 60% of Japan\u2019s "
         "centres crowd the metro area. Market to hit $33.4B by 2030."),
    ]
    for i, (label, head, body) in enumerate(grid):
        x = MARGIN + (i % 2) * (card_w + 16)
        y = grid_y + (i // 2) * (card_h + 16)
        draw_card(d, x, y, card_w, card_h, label, head, body,
                  CARD, 25, 20)

    # ---- Bottom story: nor'easter ----
    draw_card(
        d, MARGIN, 754, W - 2 * MARGIN, 158,
        "WEATHER  \u00b7  EAST COAST",
        "Nor\u2019easter slams East Coast on Thanksgiving",
        "Peak impact Thursday: gusts to 70 mph, major coastal flooding from "
        "Georgia to New York, 80 million+ under wind alerts. New Jersey "
        "declares a state of emergency.",
        CARD, 33, 21, head_lines=1, body_lines=2,
        single_line_head=True)

    # ---- Footer ----
    d.rectangle([MARGIN, 926, W - MARGIN, 927], fill=RULE)
    d.text((MARGIN, 938),
           "Sources: Reuters  \u00b7  BBC  \u00b7  The Weather Channel / "
           "National Weather Service",
           font=F_FOOT, fill=MUTED)
    d.text((MARGIN, 962),
           "Every story first reported on 26 November 2026  \u00b7  "
           "Built with Python + Pillow",
           font=F_CREDIT, fill=MUTED)

    out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.png")
    img.save(out, "PNG")
    print("wrote", out, os.path.getsize(out), "bytes")


if __name__ == "__main__":
    main()
