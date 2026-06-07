#!/usr/bin/env python3
"""
Generate the 19 full-scale per-scene compositions for the Mark Hanna documentary.

Each scene is emitted as its own self-contained <template>-style HTML composition
under compositions/scene-NN-<slug>.html (suffix `-fs.html` to NOT clobber the
existing 5-min preview's scenes 1-4).

The keyframes encoded here are derived from research/visual/SHOT_BOARDS.md
(scene-relative seconds, never narration-aligned, per LEARNINGS line 13).

This is v1: all scenes use the same shell (background image OR typography plate,
chapter card, hero text plates, verdict line, vignette, grain) plus per-scene
GSAP keyframes. Scenes whose shot-board callouts include a custom motion graphic
(map, count-up scoreboard, ledger plate write-in, vote-tally crawl, etc.) get
those graphics implemented inline.
"""
from __future__ import annotations
import json, os, sys, html, textwrap, pathlib

PROJ = pathlib.Path("/Users/I548399/SAPDevelop/github.com/personal/hyperframe-test/mark-hanna")
COMP = PROJ / "compositions"
COMP.mkdir(exist_ok=True)

# --- Shared style block (palette + typography from DESIGN.md / STYLE_GUIDE.md) ---
SHARED_STYLE = """
@font-face { font-family: "Source Serif 4"; src: url("../assets/fonts/SourceSerif4-Regular.woff2") format("woff2"); font-weight: 400; font-style: normal; }
@font-face { font-family: "Playfair Display"; src: url("../assets/fonts/PlayfairDisplay-Bold.woff2") format("woff2"); font-weight: 700; font-style: normal; }
@font-face { font-family: "Playfair Display"; src: url("../assets/fonts/PlayfairDisplay-Black.woff2") format("woff2"); font-weight: 900; font-style: normal; }
@font-face { font-family: "Roboto Mono"; src: url("../assets/fonts/RobotoMono-Regular.woff2") format("woff2"); font-weight: 400 700; font-style: normal; }

.fs-stage { position:absolute; inset:0; background:#0E0B08; font-family:"Source Serif 4",serif; color:#E8DEC8; overflow:hidden; }
.fs-stage * { box-sizing:border-box; }

.fs-chapter { position:absolute; inset:0; display:flex; flex-direction:column; align-items:center; justify-content:center; opacity:0; z-index:30; }
.fs-chapter .roman { font-family:"Playfair Display",serif; font-weight:700; font-size:96px; color:#9A8E76; font-style:italic; letter-spacing:0.08em; }
.fs-chapter .title { margin-top:18px; font-family:"Source Serif 4",serif; font-style:italic; font-size:56px; color:#E8DEC8; letter-spacing:0.04em; }

.fs-bg-photo { position:absolute; top:50%; left:50%; transform:translate(-50%,-50%); max-width:1400px; max-height:880px; opacity:0; z-index:5; filter:sepia(0.22) contrast(1.05) brightness(0.92) saturate(0.85); box-shadow:0 30px 80px rgba(0,0,0,0.6); border:1px solid rgba(200,117,51,0.35); }
.fs-bg-photo.full { max-width:1920px; max-height:1080px; }
.fs-bg-photo.left { left:30%; }
.fs-bg-photo.right { left:70%; }

.fs-strap { position:absolute; top:120px; left:50%; transform:translateX(-50%); font-family:"Roboto Mono",monospace; font-size:22px; font-weight:500; color:#9A8E76; letter-spacing:0.18em; text-transform:uppercase; opacity:0; z-index:20; padding:12px 28px; border-top:1px solid #C87533; border-bottom:1px solid #C87533; }

.fs-year-strap { position:absolute; top:54px; left:64px; font-family:"Roboto Mono",monospace; font-size:28px; color:#9A8E76; letter-spacing:0.2em; opacity:0; z-index:20; }

.fs-name { position:absolute; top:48%; left:50%; transform:translate(-50%,-50%); text-align:center; font-family:"Playfair Display",serif; font-weight:900; line-height:0.95; letter-spacing:-0.02em; opacity:0; z-index:25; text-shadow:0 4px 20px rgba(0,0,0,0.5); }
.fs-name .accent { color:#C87533; }

.fs-hero { position:absolute; left:50%; transform:translateX(-50%); width:1600px; text-align:center; font-family:"Playfair Display",serif; font-weight:700; line-height:1.15; letter-spacing:-0.01em; color:#E8DEC8; opacity:0; z-index:22; }
.fs-hero.italic { font-family:"Source Serif 4",serif; font-style:italic; font-weight:400; }
.fs-hero.amber { color:#C87533; }
.fs-hero.blood { color:#C03A2C; }
.fs-hero.cream { color:#E8DEC8; }

.fs-verdict { position:absolute; bottom:200px; left:50%; transform:translateX(-50%); width:1700px; text-align:center; font-family:"Playfair Display",serif; font-weight:900; letter-spacing:-0.02em; opacity:0; z-index:26; }
.fs-verdict.amber { color:#C87533; }
.fs-verdict.cream { color:#E8DEC8; }
.fs-verdict.blood { color:#C03A2C; }
.fs-verdict.italic { font-family:"Source Serif 4",serif; font-style:italic; font-weight:400; }

.fs-mono { font-family:"Roboto Mono",monospace; font-variant-numeric:tabular-nums; }

.fs-ledger { position:absolute; left:50%; transform:translateX(-50%); width:1280px; padding:48px 64px; background:#E8DEC8; color:#0E0B08; font-family:"Roboto Mono",monospace; font-size:30px; line-height:1.7; opacity:0; z-index:24; box-shadow:0 30px 80px rgba(0,0,0,0.5); }
.fs-ledger .row { display:flex; justify-content:space-between; opacity:0; transform:translateY(8px); }
.fs-ledger .row .amt { font-weight:700; }
.fs-ledger .stamp { font-family:"Playfair Display",serif; font-weight:900; color:#C03A2C; font-size:42px; opacity:0; transform:scale(1.05); }
.fs-ledger hr { border:none; border-top:1px solid #0E0B08; margin:14px 0; opacity:0; }

.fs-vignette { position:absolute; inset:0; pointer-events:none; z-index:90; background:radial-gradient(ellipse at center, rgba(14,11,8,0) 38%, rgba(14,11,8,0.55) 88%, rgba(14,11,8,0.85) 100%); opacity:1; }
.fs-grain { position:absolute; inset:-10%; pointer-events:none; z-index:89; opacity:0.10; background-image:repeating-radial-gradient(circle at 20% 30%, rgba(232,222,200,0.20) 0, rgba(232,222,200,0.20) 1px, transparent 1px, transparent 3px), repeating-radial-gradient(circle at 70% 80%, rgba(200,117,51,0.12) 0, rgba(200,117,51,0.12) 1px, transparent 1px, transparent 4px); mix-blend-mode:overlay; }
"""

# Per-scene metadata. Each scene defines:
#   slug, title, duration, chapter (roman, title), bg (image/none), elements
# Elements is an ordered list of `(kind, kwargs)` tuples consumed by the renderer.
# Scene-relative second timing per SHOT_BOARDS.md.

SCENES = [
    {
        "idx": 1, "slug": "cartoon", "title": "THE CARTOON", "duration": 45,
        "chapter": None,  # cold open — no chapter card
        "elements": [
            {"k": "strap", "id": "s1-strap", "text": "A CAMPAIGN MANAGER · CLEVELAND, OHIO · EIGHTEEN NINETY-SIX",
             "fade_in": 0.5, "fade_out": 38.0},
            {"k": "img", "id": "s1-cartoon-1", "src": "../assets/cartoon-dollar-mark-hanna.jpg?v=2",
             "fade_in": 4.0, "ken_burns": (1.00, 1.04, 14.0), "fade_out": 18.0, "klass": "full"},
            {"k": "img", "id": "s1-cartoon-2", "src": "../assets/cartoon-shylock-hanna.jpg",
             "fade_in": 18.0, "ken_burns": (1.00, 1.03, 10.0), "fade_out": 28.0, "klass": "full"},
            {"k": "img", "id": "s1-cartoon-3", "src": "../assets/cartoon-boss-of-bosses.jpg",
             "fade_in": 28.0, "ken_burns": (1.00, 1.03, 10.0), "fade_out": 38.0, "klass": "full"},
            {"k": "img", "id": "s1-portrait", "src": "../assets/hanna-portrait.jpg",
             "fade_in": 38.6, "fade_out": 45.0, "scale": 0.55},
            {"k": "name", "id": "s1-name", "first": "MARK", "last": "HANNA",
             "fade_in": 39.2, "fade_out": 45.0, "size": "184px", "top": "60%"},
            {"k": "hero", "id": "s1-year", "text": "1 8 9 6", "klass": "amber",
             "fade_in": 42.0, "fade_out": 45.0, "size": "44px", "top": "78%",
             "letter_spacing": "0.5em", "font": "mono"},
        ],
    },
    {
        "idx": 2, "slug": "ledger", "title": "THE LEDGER", "duration": 165,
        "chapter": ("II", "THE LEDGER"),
        "elements": [
            {"k": "img", "id": "s2-newspaper", "src": "../assets/newspaper-eveningstar-1896-01-11.jpg",
             "fade_in": 1.5, "ken_burns": (1.06, 1.00, 14.0), "fade_out": 14.0},
            # number theatre
            {"k": "hero_at", "id": "s2-year", "text": "1896", "klass": "blood",
             "fade_in": 14.0, "fade_out": 16.5, "size": "280px", "top": "44%"},
            {"k": "count_up", "id": "s2-raised", "label": "RAISED · 1896",
             "value": "$3,500,000", "klass": "amber",
             "fade_in": 17.0, "fade_out": 60.0, "size": "184px", "top": "44%"},
            {"k": "hero_at", "id": "s2-stamp", "text": "20 ×", "klass": "blood",
             "fade_in": 20.0, "fade_out": 60.0, "size": "184px", "top": "62%"},
            {"k": "hero_at", "id": "s2-stamp-sub", "text": "over Bryan's campaign",
             "fade_in": 20.6, "fade_out": 60.0, "size": "32px", "top": "73%",
             "klass": "cream", "italic": True},
            {"k": "ledger", "id": "s2-donors", "title": "DONORS · 1896",
             "rows": [
                 ("BANKS", "1/4 % of paid-in capital"),
                 ("RAILROADS", "assessed by line-mile"),
                 ("STANDARD OIL", "$ 250,000"),
                 ("J P MORGAN", "$ 250,000"),
             ],
             "stamp": None,
             "fade_in": 60.0, "fade_out": 110.0, "top": "20%"},
            {"k": "hero_at", "id": "s2-counter1", "text": "500,000  voters by train",
             "fade_in": 80.0, "fade_out": 110.0, "size": "72px", "top": "78%",
             "klass": "amber", "font": "mono"},
            {"k": "hero_at", "id": "s2-counter2", "text": "200,000,000  pieces of mail",
             "fade_in": 84.0, "fade_out": 110.0, "size": "72px", "top": "88%",
             "klass": "amber", "font": "mono"},
            {"k": "verdict", "id": "s2-verdict",
             "text": "And when November came, the ledger won.",
             "klass": "amber", "size": "84px",
             "fade_in": 110.0, "fade_out": 138.0},
            {"k": "verdict", "id": "s2-transition",
             "text": "To understand how — we go back fifty-nine years.",
             "klass": "italic cream", "size": "44px",
             "fade_in": 140.0, "fade_out": 164.0},
        ],
    },
    {
        "idx": 3, "slug": "new-lisbon", "title": "NEW LISBON, OHIO. 1837.", "duration": 90,
        "chapter": ("IV", "THE COUNTRY GROCERY"),
        "year_strap": "YEAR  1837",
        "elements": [
            {"k": "img", "id": "s3-birthplace", "src": "../assets/hanna-birthplace.jpg",
             "fade_in": 1.7, "ken_burns": (1.00, 1.04, 28.0), "fade_out": 30.0},
            {"k": "img", "id": "s3-young", "src": "../assets/hanna-young.jpg",
             "fade_in": 30.0, "ken_burns": (1.00, 1.03, 30.0), "fade_out": 75.0},
            {"k": "strap", "id": "s3-cap", "text": "NEW LISBON, OHIO. 1837.",
             "fade_in": 4.0, "fade_out": 75.0},
            {"k": "verdict", "id": "s3-transition",
             "text": "And when he was fifteen, the family moved to Cleveland.",
             "klass": "italic cream", "size": "40px",
             "fade_in": 78.0, "fade_out": 90.0},
        ],
    },
    {
        "idx": 4, "slug": "rockefeller", "title": "THE BOY AT THE NEXT DESK", "duration": 60,
        "chapter": ("V", "THE BOY AT THE NEXT DESK"),
        "year_strap": "YEAR  1852",
        "elements": [
            {"k": "img", "id": "s4-young", "src": "../assets/hanna-young.jpg",
             "fade_in": 0.5, "ken_burns": (1.00, 1.02, 12.0), "fade_out": 60.0,
             "klass": "left", "scale": 0.55},
            {"k": "img", "id": "s4-rocky", "src": "../assets/rockefeller.jpg",
             "fade_in": 8.0, "ken_burns": (1.00, 1.02, 17.0), "fade_out": 60.0,
             "klass": "right", "scale": 0.55},
            {"k": "name", "id": "s4-name", "first": "JOHN D.", "last": "ROCKEFELLER",
             "fade_in": 14.0, "fade_out": 50.0, "size": "120px", "top": "78%"},
            {"k": "hero_at", "id": "s4-sub",
             "text": "90% of American oil refining capacity.",
             "fade_in": 14.5, "fade_out": 50.0, "size": "32px", "top": "88%",
             "klass": "cream", "italic": True},
            {"k": "verdict", "id": "s4-verdict",
             "text": "The two would orbit each other for the next forty years.",
             "klass": "amber", "size": "72px",
             "fade_in": 55.0, "fade_out": 60.0},
        ],
    },
    {
        "idx": 5, "slug": "price", "title": "THE PRICE OF THINGS", "duration": 90,
        "chapter": ("V", "THE COUNTER"),
        "elements": [
            {"k": "img", "id": "s5-cleveland", "src": "../assets/cleveland-1870.jpg",
             "fade_in": 1.7, "ken_burns": (1.00, 1.04, 60.0), "fade_out": 60.0},
            {"k": "hero_at", "id": "s5-quote",
             "text": "“the real education was in the price of things.”",
             "klass": "italic cream", "size": "56px", "top": "62%",
             "fade_in": 8.0, "fade_out": 55.0},
            {"k": "verdict", "id": "s5-transition",
             "text": "Then the Civil War came. He served briefly. Came home.",
             "klass": "italic cream", "size": "40px",
             "fade_in": 60.0, "fade_out": 90.0},
        ],
    },
    {
        "idx": 6, "slug": "charlotte", "title": "CHARLOTTE", "duration": 60,
        "chapter": ("VI", "CHARLOTTE"),
        "elements": [
            {"k": "hero_at", "id": "s6-plate",
             "text": "Charlotte Augusta Rhodes — married Mark Hanna, September 27, 1864.",
             "klass": "italic cream", "size": "56px", "top": "48%",
             "fade_in": 2.2, "fade_out": 55.0},
            {"k": "strap", "id": "s6-cap",
             "text": "CLEVELAND, OHIO · SEPTEMBER 27, 1864.",
             "fade_in": 10.2, "fade_out": 55.0},
        ],
    },
    {
        "idx": 7, "slug": "chokepoint", "title": "THE CHOKEPOINT", "duration": 90,
        "chapter": ("VII", "THE CHOKEPOINT"),
        "elements": [
            {"k": "img", "id": "s7-rhodes", "src": "../assets/rhodes-daniel.jpg",
             "fade_in": 1.2, "fade_out": 6.0, "scale": 0.55, "klass": "left"},
            {"k": "hero_at", "id": "s7-rhodes-tag",
             "text": "Daniel P. Rhodes — Cleveland coal-and-iron magnate. Father-in-law.",
             "klass": "cream", "size": "28px", "top": "75%",
             "fade_in": 1.5, "fade_out": 6.0, "italic": True},
            {"k": "map_chokepoint", "id": "s7-map",
             "fade_in": 8.0, "fade_out": 70.0},
            {"k": "verdict", "id": "s7-verdict",
             "text": "Cleveland was the chokepoint. And Hanna sat on it.",
             "klass": "amber", "size": "84px",
             "fade_in": 55.0, "fade_out": 70.0},
            {"k": "ledger", "id": "s7-acq", "title": "ACQUISITIONS",
             "rows": [
                 ("THE CLEVELAND HERALD", "Newspaper"),
                 ("AN OPERA HOUSE", "Theater"),
                 ("BANKING INTERESTS", "Finance"),
                 ("A STREETCAR LINE", "Transit"),
             ],
             "stamp": None,
             "fade_in": 70.0, "fade_out": 86.0, "top": "20%"},
            {"k": "verdict", "id": "s7-temp",
             "text": "When he walked into a room, the room changed temperature.",
             "klass": "italic cream", "size": "60px",
             "fade_in": 86.0, "fade_out": 90.0},
        ],
    },
    {
        "idx": 8, "slug": "thesis", "title": "THE THESIS", "duration": 90,
        "chapter": ("VIII", "THE THESIS"),
        "elements": [
            {"k": "img", "id": "s8-portrait", "src": "../assets/hanna-portrait.jpg",
             "fade_in": 1.2, "fade_out": 25.0, "scale": 0.65, "vignette": "tighten"},
            {"k": "hero_at", "id": "s8-q1",
             "text": "Money was the second most powerful thing in America.",
             "klass": "cream", "size": "76px", "top": "44%",
             "fade_in": 25.0, "fade_out": 40.0},
            {"k": "hero_at", "id": "s8-q2",
             "text": "The most powerful thing was who decided where the money went.",
             "klass": "blood", "size": "76px", "top": "44%",
             "fade_in": 41.0, "fade_out": 55.0},
            {"k": "verdict", "id": "s8-verdict",
             "text": "That was politics. And no one had ever run it like a business. Not yet.",
             "klass": "amber", "size": "60px",
             "fade_in": 55.0, "fade_out": 90.0},
        ],
    },
    {
        "idx": 9, "slug": "chicago-1888", "title": "CHICAGO, 1888", "duration": 150,
        "chapter": ("IX", "CHICAGO, 1888"),
        "elements": [
            {"k": "img", "id": "s9-conv", "src": "../assets/convention-1888.jpg",
             "fade_in": 1.2, "ken_burns": (1.00, 1.04, 30.0), "fade_out": 60.0},
            {"k": "strap", "id": "s9-strap",
             "text": "REPUBLICAN NATIONAL CONVENTION · CHICAGO · JUNE 1888",
             "fade_in": 4.0, "fade_out": 60.0},
            {"k": "name", "id": "s9-sherman", "first": "JOHN", "last": "SHERMAN",
             "fade_in": 10.0, "fade_out": 18.0, "size": "96px", "top": "30%"},
            {"k": "tally_crawl", "id": "s9-ballots",
             "rows": [
                 ("BALLOT 1", "229", "Sherman"),
                 ("BALLOT 2", "244", "Sherman"),
                 ("BALLOT 3", "230", "Sherman"),
                 ("BALLOT 4", "235", "Sherman"),
                 ("BALLOT 5", "244", "Sherman"),
                 ("BALLOT 6", "230", "Sherman"),
                 ("BALLOT 7", "231", "Sherman"),
                 ("BALLOT 8", "---", "Harrison nominated"),
             ],
             "fade_in": 28.0, "fade_out": 60.0},
            {"k": "name", "id": "s9-mck", "first": "WILLIAM", "last": "McKINLEY",
             "fade_in": 61.0, "fade_out": 130.0, "size": "120px", "top": "20%"},
            {"k": "hero_at", "id": "s9-mck-sub",
             "text": "Congressman, 17th District, Ohio. 45 years old.",
             "klass": "cream", "size": "32px", "top": "30%",
             "fade_in": 61.4, "fade_out": 130.0, "italic": True},
            {"k": "img", "id": "s9-mck-img", "src": "../assets/mckinley-1896.jpg",
             "fade_in": 67.0, "ken_burns": (1.00, 1.02, 35.0), "fade_out": 130.0,
             "scale": 0.55, "top": "60%"},
            {"k": "hero_at", "id": "s9-loyal",
             "text": "“That kind of loyalty was rare in eighteen eighty-eight politics. It was almost extinct.”",
             "klass": "italic cream", "size": "44px", "top": "82%",
             "fade_in": 100.0, "fade_out": 128.0},
            {"k": "verdict", "id": "s9-verdict",
             "text": "He had just found his president.",
             "klass": "amber", "size": "84px",
             "fade_in": 130.0, "fade_out": 150.0},
        ],
    },
    {
        "idx": 10, "slug": "panic", "title": "THE PANIC", "duration": 120,
        "chapter": ("X", "THE PANIC. 1893."),
        "elements": [
            {"k": "newspaper_plate", "id": "s10-news",
             "headline": "M'KINLEY FACING FINANCIAL RUIN",
             "sub": "LIABILITIES, $130,000.",
             "side": "1,500 BUSINESSES UNDER. 640 BANKS FAIL.",
             "fade_in": 1.2, "ken_burns": (1.00, 1.05, 25.0), "fade_out": 28.0},
            {"k": "hero_at", "id": "s10-beggar",
             "text": "“I am a beggar.”",
             "klass": "italic cream", "size": "84px", "top": "48%",
             "fade_in": 28.8, "fade_out": 37.0},
            {"k": "hero_at", "id": "s10-ida",
             "text": "Ida Saxton McKinley — chronically ill, often bedridden — kept off the campaign trail by her health.",
             "klass": "italic cream", "size": "36px", "top": "60%",
             "fade_in": 37.0, "fade_out": 50.0},
            {"k": "img", "id": "s10-mck", "src": "../assets/mckinley-1896.jpg",
             "fade_in": 37.0, "fade_out": 50.0, "scale": 0.45, "klass": "left"},
            {"k": "ledger", "id": "s10-rescue", "title": "RESCUE",
             "rows": [
                 ("WALKER NOTES", "absorbed by Cleveland/NY syndicate, March 1893"),
                 ("MCKINLEY signed", "nothing"),
                 ("MCKINLEY owed", "nothing"),
             ],
             "stamp": None,
             "fade_in": 50.0, "fade_out": 75.0, "top": "20%"},
            {"k": "hero_at", "id": "s10-v1",
             "text": "The candidate was now a debt.",
             "klass": "blood", "size": "84px", "top": "60%",
             "fade_in": 75.0, "fade_out": 119.0},
            {"k": "hero_at", "id": "s10-v2",
             "text": "And Hanna held the paper.",
             "klass": "amber", "size": "84px", "top": "72%",
             "fade_in": 76.0, "fade_out": 119.0},
        ],
    },
    {
        "idx": 11, "slug": "mechanism", "title": "THE MECHANISM", "duration": 105,
        "chapter": ("XI", "THE MECHANISM"),
        "elements": [
            {"k": "ledger", "id": "s11-mech", "title": "ASSESSMENTS · 1896",
             "rows": [
                 ("BANKS", "1/4 % of paid-in capital"),
                 ("RAILROADS", "assessed by line-mile"),
                 ("STANDARD OIL", "$ 250,000"),
                 ("J P MORGAN", "$ 250,000"),
                 ("NEW YORK LIFE", "$ 50,000"),
                 ("EQUITABLE", "$ 50,000"),
                 ("METROPOLITAN LIFE", "$ 50,000"),
             ],
             "stamp": ("TOTAL", "$ 3,500,000"),
             "compare": ("BRYAN, 1896", "$ 300,000 (estimated)"),
             "fade_in": 1.2, "fade_out": 100.0, "top": "10%"},
            {"k": "verdict", "id": "s11-v",
             "text": "Twenty times what William Jennings Bryan would raise.",
             "klass": "blood", "size": "72px",
             "fade_in": 27.0, "fade_out": 100.0},
        ],
    },
    {
        "idx": 12, "slug": "front-porch", "title": "THE FRONT PORCH", "duration": 45,
        "chapter": ("XII", "THE FRONT PORCH"),
        "elements": [
            {"k": "hero_at", "id": "s12-place",
             "text": "CANTON, OHIO · 1896",
             "klass": "cream", "size": "32px", "top": "12%",
             "fade_in": 1.2, "fade_out": 45.0, "font": "mono", "letter_spacing": "0.4em"},
            {"k": "counter_strip", "id": "s12-counter",
             "stamps": ["+12,400", "+74,000", "+218,000", "+501,200"],
             "stamp_times": [4.0, 12.0, 22.0, 32.0],
             "labels": ["JULY", "AUGUST", "SEPTEMBER", "OCTOBER"],
             "fade_in": 1.5, "fade_out": 45.0},
            {"k": "verdict", "id": "s12-v",
             "text": "Half a million voters. By train. To Canton.",
             "klass": "amber", "size": "60px",
             "fade_in": 38.0, "fade_out": 45.0},
        ],
    },
    {
        "idx": 13, "slug": "cross-of-gold", "title": "CROSS OF GOLD", "duration": 60,
        "chapter": ("XIII", "CROSS OF GOLD"),
        "elements": [
            {"k": "hero_at", "id": "s13-quote",
             "text": "“You shall not press down upon the brow of labor this crown of thorns. You shall not crucify mankind upon a cross of gold.”",
             "klass": "italic cream", "size": "60px", "top": "40%",
             "fade_in": 1.2, "fade_out": 30.0},
            {"k": "hero_at", "id": "s13-attr",
             "text": "WILLIAM JENNINGS BRYAN · DEMOCRATIC NATIONAL CONVENTION · CHICAGO · JULY 9, 1896.",
             "klass": "cream", "size": "26px", "top": "70%",
             "fade_in": 5.5, "fade_out": 30.0, "font": "mono"},
            {"k": "hero_at", "id": "s13-bryan",
             "text": "WILLIAM JENNINGS BRYAN",
             "klass": "cream", "size": "84px", "top": "44%",
             "fade_in": 30.0, "fade_out": 55.0},
            {"k": "hero_at", "id": "s13-bryan-sub",
             "text": "“The Boy Orator of the Platte.”  Age 36. Ran on silver.",
             "klass": "italic cream", "size": "32px", "top": "56%",
             "fade_in": 31.0, "fade_out": 55.0},
            {"k": "verdict", "id": "s13-v",
             "text": "Hanna read the speech in Cleveland that night, and went, the next morning, to the bank.",
             "klass": "italic cream", "size": "36px",
             "fade_in": 55.0, "fade_out": 60.0},
        ],
    },
    {
        "idx": 14, "slug": "two-hundred-million", "title": "TWO HUNDRED MILLION", "duration": 45,
        "chapter": ("XIV", "ASYMMETRY"),
        "elements": [
            {"k": "count_up", "id": "s14-mail",
             "label": "PIECES OF CAMPAIGN MAIL",
             "value": "200,000,000", "klass": "amber",
             "fade_in": 1.2, "fade_out": 45.0, "size": "184px", "top": "30%"},
            {"k": "hero_at", "id": "s14-rail",
             "text": "18,000 mi.   ·   Bryan's whistle-stop tour",
             "klass": "cream", "size": "44px", "top": "55%",
             "fade_in": 9.0, "fade_out": 45.0, "font": "mono"},
            {"k": "hero_at", "id": "s14-langs",
             "text": "German · Polish · Yiddish · Italian · Spanish · Norwegian · Swedish · Czech · Hungarian · Lithuanian · Slovak · Greek · Welsh · French",
             "klass": "cream", "size": "26px", "top": "65%",
             "fade_in": 18.0, "fade_out": 45.0, "font": "mono"},
            {"k": "verdict", "id": "s14-v",
             "text": "Hanna mailed a country.",
             "klass": "amber", "size": "84px",
             "fade_in": 38.0, "fade_out": 45.0},
        ],
    },
    {
        "idx": 15, "slug": "election-night", "title": "NOVEMBER 3, 1896", "duration": 30,
        "chapter": None,
        "elements": [
            {"k": "ledger_compact", "id": "s15-result",
             "rows": [("McKINLEY", "271 electoral votes"),
                      ("BRYAN", "176 electoral votes")],
             "fade_in": 1.5, "fade_out": 25.0, "top": "30%"},
            {"k": "verdict", "id": "s15-v",
             "text": "And when November came, the ledger won.",
             "klass": "amber", "size": "84px",
             "fade_in": 9.5, "fade_out": 25.0, "scale_in": True},
            {"k": "hero_at", "id": "s15-pop",
             "text": "7,108,480 — 6,511,495   ·   51% McKinley.",
             "klass": "cream", "size": "32px", "top": "78%",
             "fade_in": 14.0, "fade_out": 25.0, "font": "mono"},
        ],
    },
    {
        "idx": 16, "slug": "cowboy", "title": "SENATOR HANNA. AND THE COWBOY.", "duration": 75,
        "chapter": ("XVI", "THE COWBOY"),
        "elements": [
            {"k": "ledger", "id": "s16-timeline", "title": "TIMELINE · 1897–1900",
             "rows": [
                 ("1897", "Hanna takes the Senate seat, Ohio."),
                 ("1899", "Vice-President Hobart dies in office."),
                 ("1900", "Roosevelt forced onto McKinley's re-election ticket."),
             ],
             "stamp": None,
             "fade_in": 1.2, "fade_out": 28.0, "top": "25%"},
            {"k": "hero_at", "id": "s16-quote",
             "text": "“Don't any of you realize there's only one life between this madman and the Presidency?”",
             "klass": "italic amber", "size": "60px", "top": "44%",
             "fade_in": 28.0, "fade_out": 55.0},
            {"k": "name", "id": "s16-tr", "first": "THEODORE", "last": "ROOSEVELT",
             "fade_in": 58.0, "fade_out": 75.0, "size": "120px", "top": "40%"},
            {"k": "hero_at", "id": "s16-tr-sub",
             "text": "Governor of New York. War hero. Reformer. The madman.",
             "klass": "italic cream", "size": "32px", "top": "55%",
             "fade_in": 58.5, "fade_out": 75.0},
            {"k": "verdict", "id": "s16-v",
             "text": "They did not listen.",
             "klass": "blood", "size": "84px",
             "fade_in": 70.0, "fade_out": 75.0},
        ],
    },
    {
        "idx": 17, "slug": "buffalo", "title": "BUFFALO", "duration": 60,
        "chapter": None,  # full silence opens
        "elements": [
            {"k": "hero_at", "id": "s17-place",
             "text": "BUFFALO. SEPTEMBER 6, 1901.",
             "klass": "cream", "size": "120px", "top": "44%",
             "fade_in": 1.5, "fade_out": 7.0},
            {"k": "newspaper_plate", "id": "s17-news",
             "headline": "PRESIDENT SHOT AT EXPOSITION",
             "sub": "An anarchist's two shots at the Pan-American.",
             "side": "BUFFALO COURIER · SEPTEMBER 7, 1901",
             "fade_in": 7.0, "ken_burns": (1.00, 1.04, 20.0), "fade_out": 28.0},
            {"k": "hero_at", "id": "s17-czol",
             "text": "Leon Czolgosz, anarchist, of Cleveland.",
             "klass": "cream", "size": "32px", "top": "84%",
             "fade_in": 18.0, "fade_out": 19.0, "font": "mono"},
            {"k": "hero_at", "id": "s17-tod",
             "text": "2:15 a.m.   ·   SEPTEMBER 14, 1901.",
             "klass": "cream", "size": "60px", "top": "44%",
             "fade_in": 28.0, "fade_out": 45.0, "font": "mono"},
            {"k": "hero_at", "id": "s17-tr-sworn",
             "text": "THEODORE ROOSEVELT — sworn in, borrowed library, Delaware Avenue, Buffalo. September 14, 1901.",
             "klass": "cream", "size": "28px", "top": "60%",
             "fade_in": 45.0, "fade_out": 55.0, "font": "mono"},
            {"k": "verdict", "id": "s17-v",
             "text": "Mark Hanna's project ends — eight years before Mark Hanna does.",
             "klass": "blood", "size": "60px",
             "fade_in": 55.0, "fade_out": 60.0},
        ],
    },
    {
        "idx": 18, "slug": "typhoid", "title": "TYPHOID", "duration": 30,
        "chapter": ("XVIII", "TYPHOID. WASHINGTON, 1904."),
        "elements": [
            {"k": "obit_plate", "id": "s18-obit",
             "headline": "M. A. HANNA DEAD",
             "dateline": "WASHINGTON, FEB. 15.",
             "body": "United States Senator from Ohio, manager of the McKinley campaigns of 1896 and 1900, founder of the modern political subscription, dead this morning of typhoid fever, in his sixty-seventh year.",
             "fade_in": 1.2, "fade_out": 28.0, "top": "12%"},
            {"k": "hero_at", "id": "s18-strap",
             "text": "MARK HANNA · 1837–1904.   AGE SIXTY-SIX.",
             "klass": "cream", "size": "32px", "top": "82%",
             "fade_in": 18.0, "fade_out": 28.0, "font": "mono"},
        ],
    },
    {
        "idx": 19, "slug": "inheritance", "title": "THE INHERITANCE", "duration": 30,
        "chapter": ("XIX", "THE INHERITANCE"),
        "elements": [
            {"k": "inheritance_timeline", "id": "s19-tl",
             "rows": [
                 ("1896", "$ 3,500,000",       "Hanna · McKinley"),
                 ("1900", "$ 3,000,000",       ""),
                 ("1928", "$ 6,300,000",       ""),
                 ("1972", "$ 138,000,000",     ""),
                 ("2008", "$ 1,300,000,000",   ""),
                 ("2024", "$ 2,700,000,000",   ""),
             ],
             "fade_in": 1.2, "fade_out": 22.0},
            {"k": "img", "id": "s19-cartoon", "src": "../assets/cartoon-dollar-mark-hanna.jpg",
             "fade_in": 22.5, "fade_out": 30.0, "scale": 0.45, "opacity_max": 0.30, "klass": "left"},
            {"k": "hero_at", "id": "s19-name",
             "text": "His name was Mark Hanna.",
             "klass": "cream", "size": "84px", "top": "44%",
             "fade_in": 20.0, "fade_out": 24.5},
            {"k": "verdict", "id": "s19-close",
             "text": "The cartoon ran in every Hearst paper in America.",
             "klass": "amber", "size": "60px",
             "fade_in": 25.0, "fade_out": 30.0},
        ],
    },
]


# ---------- HTML/JS emitters ----------

def emit_element(scene_idx, e):
    """Return (html, js) tuple for an element."""
    k = e["k"]
    eid = e["id"]
    fi = e.get("fade_in", 0)
    fo = e.get("fade_out", None)

    if k == "strap":
        h = f'<div class="fs-strap" id="{eid}">{html.escape(e["text"])}</div>'
        j = f'tl.to("#{eid}", {{ opacity: 1, duration: 0.6, ease: "power3.out" }}, {fi});'
        if fo is not None:
            j += f'\n        tl.to("#{eid}", {{ opacity: 0, duration: 0.5, ease: "power2.in" }}, {fo});'
        return h, j

    if k == "year_strap_value":
        h = f'<div class="fs-year-strap" id="{eid}">{html.escape(e["text"])}</div>'
        j = f'tl.to("#{eid}", {{ opacity: 1, duration: 0.5, ease: "power3.out" }}, {fi});'
        if fo is not None:
            j += f'\n        tl.to("#{eid}", {{ opacity: 0, duration: 0.5, ease: "power2.in" }}, {fo});'
        return h, j

    if k == "img":
        klass = e.get("klass", "")
        scale = e.get("scale", 1.0)
        top = e.get("top", "50%")
        src = e["src"]
        # opacity max
        op_max = e.get("opacity_max", 1.0)
        # base style override for scale + top
        style_extra = f"top:{top}; transform:translate(-50%,-50%) scale({scale});"
        if "left" in klass: style_extra = f"top:{top}; left:30%; transform:translate(-50%,-50%) scale({scale});"
        elif "right" in klass: style_extra = f"top:{top}; left:70%; transform:translate(-50%,-50%) scale({scale});"
        h = f'<img class="fs-bg-photo {klass}" id="{eid}" src="{src}" alt="" style="{style_extra}">'
        j = f'tl.to("#{eid}", {{ opacity: {op_max}, duration: 0.8, ease: "power3.out" }}, {fi});'
        if "ken_burns" in e:
            s0, s1, dur = e["ken_burns"]
            # Ken Burns by transform-origin scale, but we already use transform for centering — use filter? Use scale via gsap transform composition:
            j += f'\n        tl.fromTo("#{eid}", {{ scale: {s0*scale} }}, {{ scale: {s1*scale}, duration: {dur}, ease: "none" }}, {fi});'
        if fo is not None:
            j += f'\n        tl.to("#{eid}", {{ opacity: 0, duration: 0.6, ease: "power2.in" }}, {fo});'
        return h, j

    if k == "name":
        size = e.get("size", "184px")
        top = e.get("top", "44%")
        h = f'<div class="fs-name" id="{eid}" style="top:{top}; font-size:{size};"><span class="first">{html.escape(e["first"])}</span> <span class="last accent">{html.escape(e["last"])}</span></div>'
        j = (
            f'tl.set("#{eid}", {{ opacity: 1 }}, {fi});\n'
            f'        tl.fromTo("#{eid} .first", {{ opacity: 0, y: 40 }}, {{ opacity: 1, y: 0, duration: 0.7, ease: "power3.out" }}, {fi});\n'
            f'        tl.fromTo("#{eid} .last", {{ opacity: 0, y: 40 }}, {{ opacity: 1, y: 0, duration: 0.7, ease: "power3.out" }}, {fi+0.4});'
        )
        if fo is not None:
            j += f'\n        tl.to("#{eid}", {{ opacity: 0, duration: 0.6, ease: "power2.in" }}, {fo});'
        return h, j

    if k == "hero" or k == "hero_at":
        size = e.get("size", "60px")
        top = e.get("top", "44%")
        klass_extra = e.get("klass", "cream")
        if e.get("italic"): klass_extra += " italic"
        font = e.get("font", "")
        ls = e.get("letter_spacing", "")
        font_style = "font-family:'Roboto Mono',monospace;" if font == "mono" else ""
        ls_style = f"letter-spacing:{ls};" if ls else ""
        h = f'<div class="fs-hero {klass_extra}" id="{eid}" style="top:{top}; font-size:{size}; {font_style} {ls_style}">{html.escape(e["text"])}</div>'
        j = f'tl.fromTo("#{eid}", {{ opacity: 0, y: 30 }}, {{ opacity: 1, y: 0, duration: 0.8, ease: "power3.out" }}, {fi});'
        if fo is not None:
            j += f'\n        tl.to("#{eid}", {{ opacity: 0, duration: 0.5, ease: "power2.in" }}, {fo});'
        return h, j

    if k == "verdict":
        size = e.get("size", "84px")
        klass = e.get("klass", "amber")
        h = f'<div class="fs-verdict {klass}" id="{eid}" style="font-size:{size};">{html.escape(e["text"])}</div>'
        if e.get("scale_in"):
            j = f'tl.fromTo("#{eid}", {{ opacity: 0, scale: 1.05 }}, {{ opacity: 1, scale: 1, duration: 1.0, ease: "expo.out" }}, {fi});'
        else:
            j = f'tl.fromTo("#{eid}", {{ opacity: 0, y: 30 }}, {{ opacity: 1, y: 0, duration: 0.8, ease: "power3.out" }}, {fi});'
        if fo is not None:
            j += f'\n        tl.to("#{eid}", {{ opacity: 0, duration: 0.5, ease: "power2.in" }}, {fo});'
        return h, j

    if k == "count_up":
        # static label + value (count animation is decorative; we just stamp it in)
        size = e.get("size", "184px")
        top = e.get("top", "40%")
        klass = e.get("klass", "amber")
        h = (
            f'<div class="fs-hero" id="{eid}" style="top:{top};">'
            f'<div class="fs-mono" style="font-size:24px; color:#9A8E76; letter-spacing:0.2em; margin-bottom:18px;">{html.escape(e["label"])}</div>'
            f'<div class="{klass}" style="font-family:Playfair Display,serif; font-weight:900; font-size:{size}; color: var(--c, #C87533);">{html.escape(e["value"])}</div>'
            f'</div>'
        )
        # Replace var(--c) with literal color via class application (already on parent)
        h = h.replace('color: var(--c, #C87533);', '')
        h = h.replace(f'<div class="{klass}"', f'<div class="fs-hero {klass}" style="display:inline-block;"')
        # Simpler form:
        color = {"amber": "#C87533", "blood": "#C03A2C", "cream": "#E8DEC8"}.get(klass, "#C87533")
        h = (
            f'<div class="fs-hero" id="{eid}" style="top:{top};">'
            f'<div class="fs-mono" style="font-size:24px; color:#9A8E76; letter-spacing:0.2em; margin-bottom:18px;">{html.escape(e["label"])}</div>'
            f'<div style="font-family:\'Playfair Display\',serif; font-weight:900; font-size:{size}; color:{color};">{html.escape(e["value"])}</div>'
            f'</div>'
        )
        j = f'tl.fromTo("#{eid}", {{ opacity: 0, scale: 0.95 }}, {{ opacity: 1, scale: 1, duration: 1.0, ease: "expo.out" }}, {fi});'
        if fo is not None:
            j += f'\n        tl.to("#{eid}", {{ opacity: 0, duration: 0.5, ease: "power2.in" }}, {fo});'
        return h, j

    if k == "ledger":
        # cream plate with rows + optional stamp & compare
        rows_html = ""
        for label, val in e["rows"]:
            rows_html += f'<div class="row"><span>{html.escape(label)}</span><span class="amt">{html.escape(val)}</span></div>'
        stamp_html = ""
        if e.get("stamp"):
            label, val = e["stamp"]
            stamp_html = f'<hr><div class="row stamp-row"><span>{html.escape(label)}</span><span class="stamp">{html.escape(val)}</span></div>'
        compare_html = ""
        if e.get("compare"):
            label, val = e["compare"]
            compare_html = f'<div class="row" style="opacity:0.7; margin-top:10px;"><span>{html.escape(label)}</span><span>{html.escape(val)}</span></div>'
        title_html = f'<div style="font-family:Roboto Mono,monospace; font-size:22px; color:#9A8E76; letter-spacing:0.2em; margin-bottom:24px;">{html.escape(e["title"])}</div>'
        top = e.get("top", "20%")
        h = f'<div class="fs-ledger" id="{eid}" style="top:{top};">{title_html}{rows_html}{stamp_html}{compare_html}</div>'
        j = f'tl.fromTo("#{eid}", {{ opacity: 0, y: 60 }}, {{ opacity: 1, y: 0, duration: 1.0, ease: "power3.out" }}, {fi});'
        # row stagger
        j += f'\n        tl.to("#{eid} .row", {{ opacity: 1, y: 0, duration: 0.5, ease: "power2.out", stagger: 0.4 }}, {fi+0.6});'
        if e.get("stamp"):
            j += f'\n        tl.to("#{eid} hr", {{ opacity: 1, duration: 0.6, ease: "expo.out" }}, {fi+1.5+0.4*len(e["rows"])});'
            j += f'\n        tl.to("#{eid} .stamp", {{ opacity: 1, scale: 1.0, duration: 0.5, ease: "expo.out" }}, {fi+2.0+0.4*len(e["rows"])});'
        if fo is not None:
            j += f'\n        tl.to("#{eid}", {{ opacity: 0, y: 60, duration: 0.8, ease: "power2.in" }}, {fo});'
        return h, j

    if k == "ledger_compact":
        rows_html = ""
        for label, val in e["rows"]:
            rows_html += f'<div class="row"><span>{html.escape(label)}</span><span class="amt">{html.escape(val)}</span></div>'
        top = e.get("top", "30%")
        h = f'<div class="fs-ledger" id="{eid}" style="top:{top}; background:#0E0B08; color:#E8DEC8; box-shadow:none;">{rows_html}</div>'
        j = f'tl.fromTo("#{eid}", {{ opacity: 0 }}, {{ opacity: 1, duration: 0.8 }}, {fi});'
        j += f'\n        tl.to("#{eid} .row", {{ opacity: 1, y: 0, duration: 0.6, ease: "power3.out", stagger: 0.5 }}, {fi+0.3});'
        if fo is not None:
            j += f'\n        tl.to("#{eid}", {{ opacity: 0, duration: 0.6 }}, {fo});'
        return h, j

    if k == "tally_crawl":
        rows_html = ""
        for ballot, votes, who in e["rows"]:
            cls = "amt" if "Harrison" in who else ""
            color = "#C03A2C" if "Harrison" in who else "#E8DEC8"
            rows_html += f'<div class="row" style="color:{color};"><span>{html.escape(ballot)}</span><span class="fs-mono">{html.escape(votes)}  {html.escape(who)}</span></div>'
        h = f'<div class="fs-ledger" id="{eid}" style="top:20%; left:8%; transform:none; width:480px; background:#0E0B08; color:#E8DEC8; border:1px solid #C87533; box-shadow:none;">{rows_html}</div>'
        j = f'tl.fromTo("#{eid}", {{ opacity: 0 }}, {{ opacity: 1, duration: 0.6 }}, {fi});'
        j += f'\n        tl.to("#{eid} .row", {{ opacity: 1, y: 0, duration: 0.4, ease: "power2.out", stagger: 1.4 }}, {fi+0.3});'
        if fo is not None:
            j += f'\n        tl.to("#{eid}", {{ opacity: 0, duration: 0.6 }}, {fo});'
        return h, j

    if k == "newspaper_plate":
        # cream front-page composite
        h = (
            f'<div class="fs-ledger" id="{eid}" style="top:8%; padding:64px 80px; width:1500px;">'
            f'<div style="font-family:Roboto Mono,monospace; font-size:18px; color:#9A8E76; letter-spacing:0.3em; margin-bottom:14px;">{html.escape(e.get("side", "CLEVELAND PLAIN DEALER"))}</div>'
            f'<div style="font-family:Playfair Display,serif; font-weight:900; font-size:120px; line-height:1.05; color:#0E0B08; margin-bottom:18px;">{html.escape(e["headline"])}</div>'
            f'<div style="font-family:Source Serif 4,serif; font-style:italic; font-size:36px; color:#0E0B08;">{html.escape(e["sub"])}</div>'
            f'</div>'
        )
        j = f'tl.fromTo("#{eid}", {{ opacity: 0, y: -60 }}, {{ opacity: 1, y: 0, duration: 1.0, ease: "power3.out" }}, {fi});'
        if "ken_burns" in e:
            s0, s1, dur = e["ken_burns"]
            j += f'\n        tl.fromTo("#{eid}", {{ scale: {s0} }}, {{ scale: {s1}, duration: {dur}, ease: "none" }}, {fi+1.1});'
        if fo is not None:
            j += f'\n        tl.to("#{eid}", {{ opacity: 0, duration: 0.6 }}, {fo});'
        return h, j

    if k == "obit_plate":
        h = (
            f'<div class="fs-ledger" id="{eid}" style="top:{e.get("top","12%")}; padding:64px 80px; width:1500px;">'
            f'<div style="font-family:Roboto Mono,monospace; font-size:24px; color:#9A8E76; letter-spacing:0.2em; margin-bottom:18px;">{html.escape(e["dateline"])}</div>'
            f'<div style="font-family:Playfair Display,serif; font-weight:900; font-size:124px; color:#0E0B08; margin-bottom:36px;">{html.escape(e["headline"])}</div>'
            f'<div style="column-count:2; column-gap:48px; font-family:Source Serif 4,serif; font-size:22px; color:#3a2f22; line-height:1.5; opacity:0.85;">{html.escape(e["body"])}</div>'
            f'</div>'
        )
        j = f'tl.fromTo("#{eid}", {{ opacity: 0, y: 100 }}, {{ opacity: 1, y: 0, duration: 1.2, ease: "power3.out" }}, {fi});'
        if fo is not None:
            j += f'\n        tl.to("#{eid}", {{ opacity: 0, duration: 0.7 }}, {fo});'
        return h, j

    if k == "counter_strip":
        # Stop-motion stamping counter
        stamp_html = "".join(
            f'<div class="counter-cell" id="{eid}-{i}" style="opacity:0;">'
            f'<div class="fs-mono" style="font-size:18px; color:#9A8E76; letter-spacing:0.2em; margin-bottom:8px;">{html.escape(label)}</div>'
            f'<div style="font-family:Playfair Display,serif; font-weight:900; font-size:84px; color:#C87533;">{html.escape(stamp)}</div>'
            f'</div>'
            for i, (stamp, label) in enumerate(zip(e["stamps"], e["labels"]))
        )
        h = (
            f'<div id="{eid}" style="position:absolute; top:30%; left:50%; transform:translateX(-50%); width:1700px; display:grid; grid-template-columns:repeat(4,1fr); gap:32px; text-align:center; z-index:24;">'
            f'{stamp_html}</div>'
        )
        js_lines = []
        for i, t in enumerate(e["stamp_times"]):
            js_lines.append(f'        tl.fromTo("#{eid}-{i}", {{ opacity: 0, scale: 1.05 }}, {{ opacity: 1, scale: 1, duration: 0.4, ease: "expo.out" }}, {t});')
        j = "\n".join(js_lines)
        if fo is not None:
            j += f'\n        tl.to("#{eid}", {{ opacity: 0, duration: 0.6 }}, {fo});'
        return h, j

    if k == "map_chokepoint":
        # SVG map graphic
        h = (
            f'<svg id="{eid}" viewBox="0 0 1920 1080" xmlns="http://www.w3.org/2000/svg" style="position:absolute; inset:0; opacity:0; z-index:18;">'
            f'<text x="960" y="120" text-anchor="middle" fill="#9A8E76" font-family="Roboto Mono" font-size="22" letter-spacing="3">CLEVELAND — THE CHOKEPOINT</text>'
            # Lake Erie polygon
            f'<polygon points="380,260 1540,260 1500,360 420,360" fill="none" stroke="#E8DEC8" stroke-width="2"/>'
            f'<text x="960" y="320" text-anchor="middle" fill="#E8DEC8" font-family="Source Serif 4" font-style="italic" font-size="32">Lake Erie  ·  iron ore from Mesabi</text>'
            # Pittsburgh polygon
            f'<polygon points="1280,720 1540,720 1540,820 1280,820" fill="none" stroke="#9A8E76" stroke-width="1"/>'
            f'<text x="1410" y="780" text-anchor="middle" fill="#9A8E76" font-family="Source Serif 4" font-size="24">Pittsburgh mills</text>'
            # Cleveland node + dollar glyph
            f'<circle cx="960" cy="500" r="14" fill="#C87533"/>'
            f'<text x="960" y="475" text-anchor="middle" fill="#C87533" font-family="Playfair Display" font-weight="900" font-size="48">$</text>'
            f'<text x="960" y="540" text-anchor="middle" fill="#E8DEC8" font-family="Roboto Mono" font-size="22" letter-spacing="2">CLEVELAND</text>'
            # ore-boat traces (animated by GSAP — drawn lines)
            f'<line x1="960" y1="320" x2="960" y2="500" stroke="#7A8A6E" stroke-width="2" stroke-dasharray="800" stroke-dashoffset="800" id="{eid}-l1"/>'
            f'<line x1="960" y1="500" x2="1410" y2="720" stroke="#7A8A6E" stroke-width="2" stroke-dasharray="800" stroke-dashoffset="800" id="{eid}-l2"/>'
            f'</svg>'
        )
        j = (
            f'tl.to("#{eid}", {{ opacity: 1, duration: 0.8 }}, {fi});\n'
            f'        tl.to("#{eid}-l1", {{ strokeDashoffset: 0, duration: 2.0, ease: "none" }}, {fi+1.5});\n'
            f'        tl.to("#{eid}-l2", {{ strokeDashoffset: 0, duration: 2.0, ease: "none" }}, {fi+12.0});'
        )
        if fo is not None:
            j += f'\n        tl.to("#{eid}", {{ opacity: 0.4, duration: 0.6 }}, {fo});'
        return h, j

    if k == "inheritance_timeline":
        rows_html = ""
        for i, (yr, amt, sub) in enumerate(e["rows"]):
            sub_html = f'<span style="color:#9A8E76; font-size:20px; margin-left:24px;">{html.escape(sub)}</span>' if sub else ""
            rows_html += (
                f'<div class="row inh-row" id="{eid}-r{i}" style="display:flex; align-items:baseline; opacity:0; margin-bottom:14px;">'
                f'<span style="font-family:Roboto Mono,monospace; font-size:36px; color:#C87533; min-width:120px;">{html.escape(yr)}</span>'
                f'<span style="font-family:Playfair Display,serif; font-weight:700; font-size:42px; color:#C87533; min-width:380px;">{html.escape(amt)}</span>'
                f'<span style="display:inline-block; width:14px; height:14px; border-radius:50%; background:#7A8A6E; margin:0 16px;"></span>'
                f'{sub_html}'
                f'</div>'
            )
        h = f'<div id="{eid}" style="position:absolute; top:22%; left:50%; transform:translateX(-50%); width:1100px; opacity:0; z-index:24;">{rows_html}</div>'
        j = f'tl.to("#{eid}", {{ opacity: 1, duration: 0.5 }}, {fi});'
        for i in range(len(e["rows"])):
            j += f'\n        tl.fromTo("#{eid}-r{i}", {{ opacity: 0, y: 8 }}, {{ opacity: 1, y: 0, duration: 0.5, ease: "power2.out" }}, {fi+0.5*i});'
        if fo is not None:
            j += f'\n        tl.to("#{eid}", {{ opacity: 0, duration: 0.6 }}, {fo});'
        return h, j

    return f'<!-- unsupported element: {k} -->', '// unsupported'


def emit_scene(s):
    idx = s["idx"]
    slug = s["slug"]
    duration = s["duration"]
    title = s["title"]
    chapter = s.get("chapter")
    year_strap = s.get("year_strap")

    body_parts = []
    js_parts = []

    # Chapter card
    if chapter:
        roman, ctitle = chapter
        body_parts.append(
            f'<div class="fs-chapter" id="s{idx}-chap"><div class="roman">{html.escape(roman)}</div><div class="title">{html.escape(ctitle)}</div></div>'
        )
        js_parts.append(
            f'tl.fromTo("#s{idx}-chap", {{ opacity: 0 }}, {{ opacity: 1, duration: 0.6, ease: "power2.out" }}, 0);\n'
            f'        tl.to("#s{idx}-chap", {{ opacity: 0, duration: 0.5, ease: "power2.in" }}, 1.2);'
        )

    if year_strap:
        body_parts.append(f'<div class="fs-year-strap" id="s{idx}-ys">{html.escape(year_strap)}</div>')
        js_parts.append(f'tl.to("#s{idx}-ys", {{ opacity: 1, duration: 0.5 }}, 1.7);\n        tl.to("#s{idx}-ys", {{ opacity: 0, duration: 0.5 }}, {duration-2});')

    # Elements
    for e in s["elements"]:
        h, j = emit_element(idx, e)
        body_parts.append(h)
        js_parts.append(j)

    body = "\n      ".join(body_parts)
    js = "\n        ".join(js_parts)

    composition_id = f"scene-{idx:02d}-{slug}-fs"

    out = f"""<template id="{composition_id}-template">
  <div data-composition-id="{composition_id}" data-width="1920" data-height="1080" data-duration="{duration}" style="position:absolute; top:0; left:0; width:1920px; height:1080px; overflow:hidden; background-color:#0E0B08;">
    <style>{SHARED_STYLE}</style>
    <div class="fs-stage">
      {body}
      <div class="fs-grain"></div>
      <div class="fs-vignette"></div>
    </div>
    <script>
      window.__timelines = window.__timelines || {{}};
      const tl = gsap.timeline({{ paused: true }});

      // Scene {idx} — {title}  ({duration} s)
      {js}

      window.__timelines["{composition_id}"] = tl;
    </script>
  </div>
</template>
"""
    return out, composition_id, duration


def main():
    # Scenes 4, 9, 10 have been HAND-TUNED beyond the generator's vocabulary
    # (custom Ken Burns push+pull, hairline draw-ins, Sherman corner-pin shrink,
    # 2-pane Ida/McKinley layout, hard-cut blackout flashes). Re-emitting them
    # would clobber the bespoke keyframes — see LEARNINGS.md "Hand-tuning vs
    # generator" entries and SHOT_BOARDS.md §scene 4/9/10.
    #
    # Scenes 6, 12, 13, 16, 17 were ADDED to this skip-set by t_45e599b6
    # (image-procurement v2). They were re-edited in place to wire procured
    # PD images (charlotte-hanna.jpg, ida-mckinley.jpg via scene 10's plate,
    # mckinley-front-porch-1896.jpg, bryan-1896.jpg, mckinley-roosevelt-1900.jpg,
    # temple-of-music-1901.jpg) as Ken-Burns / held-still plates with the
    # caption text moved out of the way. The generator's hero_at-only emit
    # would put the typographic fallback back on top of the image. See
    # PROVENANCE.md for source URLs.
    HAND_TUNED_SKIP = {4, 6, 9, 10, 12, 13, 16, 17}

    out_index = []
    for s in SCENES:
        if s["idx"] in HAND_TUNED_SKIP:
            print(f"skip   scene-{s['idx']:02d}-{s['slug']}-fs.html  (hand-tuned)")
            # Still record in manifest so index.html can resolve composition_id + duration.
            out_index.append((s["idx"],
                              f"scene-{s['idx']:02d}-{s['slug']}-fs",
                              s["duration"],
                              f"scene-{s['idx']:02d}-{s['slug']}-fs.html"))
            continue
        content, cid, dur = emit_scene(s)
        path = COMP / f"scene-{s['idx']:02d}-{s['slug']}-fs.html"
        path.write_text(content)
        out_index.append((s["idx"], cid, dur, path.name))
        print(f"wrote {path.name}  ({dur} s)")

    # Write a small manifest so index-fullscale.html builder can read it
    manifest = [
        {"idx": idx, "composition_id": cid, "duration": dur, "file": fname}
        for (idx, cid, dur, fname) in out_index
    ]
    (PROJ / "research/full-scale/SCENES_INDEX.json").write_text(json.dumps(manifest, indent=2))
    print(f"wrote SCENES_INDEX.json  ({len(manifest)} scenes)")


if __name__ == "__main__":
    main()
