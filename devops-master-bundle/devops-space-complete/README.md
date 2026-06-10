# DevOps Governance Space — COMPLETE bundle (pages 0–19 + backlog import)

One paste-ready `.md` file per Confluence page, plus an import-ready CSV for the board.

## Copy-paste process (Confluence Cloud)
1. Create the space (e.g. key `DEVGOV`) if not already done.
2. For each file: create the page → set title from the table → click in body → **paste as plain text** (`Ctrl/Cmd+Shift+V`) → verify → Publish. Files are body-only (no title line).
3. Add `/Table of Contents` to long pages, `/Children Display` to the home page.
4. Data Center instead: Insert → Markup → Markdown.

## File → page map
| File | Page title |
|---|---|
| 00 | DevOps Governance & Planning (space home) |
| 01 | DevOps Charter |
| 02 | Intake & Planning Process |
| 03 | Backlog Taxonomy & Azure Boards Usage |
| 04 | GitHub / Work Item Traceability |
| 05 | Repository & Pipeline Governance Standards |
| 06 | S.C.A.L.E.D. Communication Framework |
| 07 | DevOps Work Item Template |
| 08 | DevOps Governance Backlog |
| 09 | DevOps Decision Log |
| 10 | Team Operating Model & Working Agreement |
| 11 | Roles, Goals & KPIs |
| 12 | Story Sizing & Estimation Guide |
| 13 | Sprint Ceremonies & Three Amigos |
| 14 | Bug, Spike & Timebox Policy |
| 15 | Engineering Handbook (Platforms, Pseudo-code, Kibana) |
| 16 | Documentation & Evidence Standard |
| 17 | Implementation Plan (Sprints, Points, Days) |
| 18 | Measurement Framework (KPI, OKR, Metrics, NPS) |
| 19 | Extended Roles (Leadership, BA, Data Eng, DBA, Security Eng) — child of 11 |
| 20 | FAQ / How to Engage DevOps |
| 21 | CoP Forum Agenda & Launch Kit |

## Importing the backlog (backlog-import.csv → Azure Boards)
1. Boards → Queries → **Import Work Items** → choose the CSV.
2. Hierarchy comes from Title 1/2/3 columns (Epic → Feature → User Story). Review the preview, then Save items.
3. Sprint assignment: items are tagged `Sprint0` / `Sprint1` — bulk-select by tag and set the Iteration Path after import (iteration paths must exist first; setting them via tag avoids import errors on missing paths).
4. Verify: parents created before children automatically; spot-check 2–3 stories for points and description.
Jira instead: keep the same rows but map Feature→Epic and Epic→label before importing (standard Jira has no Feature level).

## Fill-ins before announcing
Page 11 + 19 contact directories (names/handles) · page 15 `{{link}}` placeholders · KPI targets on page 18 if your baselines differ.
