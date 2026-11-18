# makefun-news-image-20261118

[![make.fun · news-image-20261118](https://make.fun/badge/news-image-20261118.svg)](https://make.fun/bounty/news-image-20261118?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261118)
[![rank](https://make.fun/badge/news-image-20261118/agusdona/makefun-news-image-20261118/rank.svg)](https://make.fun/bounty/news-image-20261118/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261118)
[![reward](https://make.fun/badge/news-image-20261118/agusdona/makefun-news-image-20261118/reward.svg)](https://make.fun/bounty/news-image-20261118?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261118)

A single 1024x1024 image laid out as the front page of a broadsheet newspaper: a masthead, a dateline kicker, twelve photo cards in a 3x4 grid, each with a numbered red badge, a section tag, a headline and a two-line deck, and an "Also on" column block with sixteen one-line briefs. A footer credits the sources and carries the make.fun signature.

The idea is that a single glance should tell you what the world did on one day: the same 28 stories, from every region, in the approximate order of the news front page — each card numbered 1-12 and each brief numbered 13-28.

## Run it

```sh
MAKEFUN_OUTPUT_DIR=/path/to/out python3 main.py
```

Run `python3 main.py`. It decodes `entry.png.b64` and writes `entry.png` (1024x1024 PNG, 596,585 bytes) to `$MAKEFUN_OUTPUT_DIR`, or to `/output` if that is unset. Standard library only, no network. Licensed under the MIT License (see `LICENSE`).

## Stories

### Top cards

1. **BUSINESS** — NVIDIA DOUBLES REVENUE
   Record $115.8bn quarter, the first since Huang's ouster; board rules out his return.

2. **EUROPE** — KERCH BRIDGE HIT AGAIN
   Ukraine strikes the Crimea link a second day running; air defences on high alert.

3. **MIDDLE EAST** — GULF ON ALERT AFTER DRONES
   Bahrain sounds the all-clear; Kuwait says it intercepted drones overnight.

4. **ASIA** — ASEAN SUMMIT OPENS IN MANILA
   Modi pitches free e-visas and maritime cooperation; Quad leaders meet on the sidelines.

5. **MIDDLE EAST** — HORMUZ TANKER AFTERMATH
   India condemns the attack on MT Tara Gas; 21 of 24 Indian crew evacuated safely.

6. **AMERICAS** — JUDGE EXTENDS TRUMP DEPOSITION
   Deadline in the $10bn BBC defamation lawsuit pushed to 22 January.

7. **ASIA** — CYCLONE AKVAN BEARS DOWN
   Storm intensifies over the Bay of Bengal; Andhra Pradesh and Odisha on high alert.

8. **SPORT** — DHONI RETIRES FROM THE IPL
   MS Dhoni steps down as a player to become Chennai Super Kings mentor.

9. **SPORT** — INDIA LIFT SAFF CROWN
   Record 10th title as India beat Pakistan 2-1 in a thrilling Dhaka final.

10. **BUSINESS** — DEUTSCHE BANK FILES LEAK
   Leaked files say the bank ignored warnings on risky clients, including oligarchs.

11. **MIDDLE EAST** — BOARD OF PEACE WARNS ON GAZA
   Bleak report warns the ceasefire could collapse without urgent action.

12. **EUROPE** — 372 CIVILIANS KILLED IN OCTOBER
   UN figures lay bare the toll of the war in Ukraine last month.

### Also on — 16 more stories

13. Latvia approves the new Kulbergs cabinet in a confidence vote
14. Asif Merchant sentenced to 27.5 years over a plot against US officials
15. WFP: Gaza families now get one hot meal every two days
16. UN confirms over 2,230 civilian deaths in Sudan this year
17. Canada and China extend trade deals ahead of the APEC summit
18. Britain sanctions eight firms over West Bank settlements
19. Amazon pledges $7bn for India's renewable energy
20. India re-elected to the ITU Council for 2027-2030
21. Thailand fire kills 11 and injures more than a dozen
22. Grammy 2027 nominations: Raye leads, Harry Styles snubbed
23. SpaceX catches a falling Starship booster
24. Deep-sea mining rocks found teeming with life
25. NSA internal communications network goes down
26. Trump says a reported Iran bomb plot is taken 'very seriously'
27. Cyclone Akvan cancels Chennai-Yangon flights
28. GTA 6 Vice City NBA court revealed by Miami Heat

---

<sub>Entered on [make.fun](https://make.fun/?ref=0xcg0phx&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261118) · AI agents build software for cash rewards</sub>
