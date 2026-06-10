# 🩺 Health Check — Gap Finder

This page makes problems visible before they become incidents. It's the smoke detector of the operating model: each symptom below routes to its owner and its fix, so "something feels off" becomes "row 4, here's the page, here's the owner." Embed the Azure Boards queries (smart link → Embed) so the gaps display themselves, live.

## 1. Live gap views (embed these from the Link Registry URLs)

- **Not-Ready items in a sprint** (L-03 embedded) — should always be zero. Anything listed was admitted without Definition of Ready.
- **Blocked items** (L-04 embedded) — each must show a tagged unblocking owner and an age < 5 days.
- **Traceability gaps** (L-05 embedded) — in-progress items with no linked PR. Should be zero after day 2 of any item.

## 2. Symptom → diagnosis → fix routing

| # | Symptom you notice | What it actually means | Fix page | Owner |
|---|---|---|---|---|
| 1 | "I'll just quickly do this" work happening | Untracked work — invisible, uncreditable, unauditable | Intake & Planning | Backlog Owner |
| 2 | Decision exists only in a chat thread | Single point of knowledge failure | Decisions database + Charter | Whoever decided |
| 3 | Same answer written on two pages | Documentation rot starting (one copy will go stale) | How This Documentation Works §2 | Page owners |
| 4 | Item bounced between states repeatedly | Missing evidence or unclear AC at Three Amigos | Bug & Spike Policy §5; Ceremonies §4 | Item owner |
| 5 | Sprint overruns / overtime appears | Capacity cap ignored or mid-sprint scope added | Story Sizing §3; Operating Model | EM |
| 6 | Story dragging > 5 days | Mis-sized (should have been split) or hidden blocker | Story Sizing §2 | Tech Lead |
| 7 | Demo prep feels hard | Evidence skipped during the work | Show & Tell §2 | Item owner |
| 8 | New joiner asks "where do I find X" | Start-Here path or Link Registry gap | Welcome page; Link Registry | DevOps Lead |
| 9 | Page lozenge stale / content doubted | Standard changed without page update | Documentation & Evidence | Page owner |
| 10 | Question answered in channel, not in FAQ | Knowledge leaked into chat | FAQ page (add it) | Whoever answered |

## 3. Weekly 10-minute health walk (rotating owner)

Once a week, one person (rotate alphabetically — everyone owns health): glance at the three embeds (should be empty), scan pages edited this week for the CURRENT lozenge, check the FAQ got this week's channel answers, and post a one-line result in the team channel: `Health: ✅ clean` or `Health: ⚠️ rows 4, 10 — items created: AB#…`. Findings become backlog items immediately — the walk never turns into a meeting.

## 4. The honesty rule

This page only works if symptoms are reported without blame. Row entries describe the *system* failing (a gate too loose, a page unclear), never a person failing. The person who reports a gap did the team a favour — say so.
