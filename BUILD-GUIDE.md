# BUILD GUIDE — DevOps Space v2 (click-by-click, ~90 minutes)

Read this once top-to-bottom, then execute. Every step says exactly where to click and what to type. Files marked **PASTE** are complete — paste and Publish, edit nothing. The only thing you ever fill in is the **Link Registry** and the **two databases** (Contacts, Decisions) — by design, every other page points to those, so the pages themselves never need editing. (That's "low coupling": one socket, many plugs.)

---

## PART 1 — Create the space and folders (5 min)

1. Confluence → **Create** (top bar) → **Space** → choose **Blank space**.
2. Name: `DevOps Hub` · Key: `DEVOPS` → **Create**.
3. In the left sidebar, hover **Content** → click **+** → **Folder**. Create these five folders, in this order:
   - `🚀 01 — Start Here`
   - `🔁 02 — How We Work`
   - `📐 03 — Standards & Reference`
   - `🗂 04 — Records & Live Data`
   - `👥 05 — Team Hub`

> Why folders: each folder is one "layer" with one job (like stations in a restaurant kitchen — grill cooks, pastry bakes; nobody does both). A reader always knows which layer answers their question. If your Confluence doesn't show Folders (older plan), create five plain pages with these names and nest content under them — everything else works identically.

## PART 2 — Paste the pages into folders (40 min)

For each file below: open the folder → **+ Create** → **Page** → type the title → click into the body → **paste the file content as plain text** (`Ctrl/Cmd + Shift + V`) → check it rendered → **Publish**.

| Folder | Page title | File |
|---|---|---|
| 01 Start Here | Welcome — Start Here | A1 |
| 01 Start Here | How This Documentation Works | A2 |
| 01 Start Here | FAQ / How to Engage DevOps | 20 (existing) |
| 02 How We Work | Team Operating Model & Working Agreement | 10 |
| 02 How We Work | Intake & Planning Process | 02 |
| 02 How We Work | Sprint Ceremonies & Three Amigos | 13 |
| 02 How We Work | Show & Tell — Demo Accountability | A4 |
| 02 How We Work | Bug, Spike & Timebox Policy | 14 |
| 02 How We Work | Story Sizing & Estimation Guide | 12 |
| 03 Standards & Reference | DevOps Charter | 01 |
| 03 Standards & Reference | Backlog Taxonomy & Azure Boards Usage | 03 |
| 03 Standards & Reference | GitHub / Work Item Traceability | 04 |
| 03 Standards & Reference | Repository & Pipeline Governance Standards | 05 |
| 03 Standards & Reference | S.C.A.L.E.D. Communication Framework | 06 |
| 03 Standards & Reference | Engineering Handbook | 15 |
| 03 Standards & Reference | Documentation & Evidence Standard | 16 |
| 03 Standards & Reference | Measurement Framework (KPI · OKR · NPS) | 18 |
| 04 Records & Live Data | Link Registry | A3 |
| 04 Records & Live Data | Health Check — Gap Finder | A5 |
| 04 Records & Live Data | Implementation Plan | 17 |
| 04 Records & Live Data | DevOps Governance Backlog | 08 |
| 04 Records & Live Data | Work Item Template | 07 |
| 05 Team Hub | Roles, Goals & KPIs | 11 |
| 05 Team Hub | Extended Roles | 19 (child of Roles page) |
| 05 Team Hub | CoP Agenda & Launch Kit | 21 |

(Pages 00 and 09 are replaced by A1 and the Decisions database below — don't paste them in v2.)

## PART 3 — Create the two databases (10 min)

Databases beat tables because they're filterable, sortable, and embeddable on any page while living in ONE place (single source of truth — like a library catalogue: one catalogue, many readers).

**Database 1 — 📇 Contacts**
1. Folder `05 Team Hub` → **+ Create** → **Database** → name `Contacts`.
2. Add fields (click **+** next to the last column header for each): `Area` (Select: Business spec, Architecture, Implementation, DevOps, Security, SRE, Infra/Cloud, Network, IAM, Platform, Frontend, Backend, Mobile, QA, CX, Data, DBA, BA, Leadership) · `Name` (User type — picks real Confluence users) · `Channel` (Text) · `Escalation` (Text).
3. Add one row per person now (this is your only data-entry job besides links).

**Database 2 — 🧭 Decisions**
1. Folder `04 Records & Live Data` → **+ Create** → **Database** → name `Decisions`.
2. Fields: `ID` (Text) · `Date` (Date) · `Decision` (Text) · `Options considered` (Text) · `Owner` (User) · `Status` (Select: Proposed, Accepted, Superseded, Rejected) · `Link` (Link).
3. Add starter rows D-001 to D-005 from the CoP Agenda & Launch Kit page.

**Embed them where needed:** on the Roles page and Welcome page, type `/Database` → pick Contacts; on any page that mentions decisions, `/Database` → Decisions. One source, many views — edits propagate everywhere automatically.

## PART 4 — Create the two whiteboards (10 min)

1. Folder `02 How We Work` → **+ Create** → **Whiteboard** → name `🗺 Work Lifecycle Map`. Draw the flow using sticky notes + arrows: `Idea → Backlog → Refined(Ready) → Amigos-passed → In Progress → In Review → In Test → Done-ready → Done`, and under each state add a small note of WHO moves it (from the Bug & Spike page table). Link each sticky to its governing page (select sticky → link icon).
2. Folder `02 How We Work` → **+ Create** → **Whiteboard** → name `🔄 Retro Board` — three columns: Went well / Didn't / Change next. Duplicate it each sprint (… menu → Copy).

> Why a whiteboard: a novice grasps the flow in 10 seconds visually before reading a word — like the map at a mall entrance ("you are here").

## PART 5 — Live docs (5 min)

1. Folder `02 How We Work` → **+ Create** → **Live doc** → name `📝 CoP Session Notes — Running`. Paste the agenda block from the CoP Agenda & Launch Kit page once; each session, duplicate the block at the top with the new date.
2. Same for `📝 Sprint Planning Notes — Running`.

> Pages = published law (edit rarely, deliberately). Live docs = collaborative scratchpads (no publish step, everyone types together). Don't mix the two: notes never live in standards pages, standards never live in notes. (Encapsulation: the messy kitchen stays behind the kitchen door.)

## PART 6 — Smart links (5 min)

Anywhere you paste a URL from Azure Boards, GitHub, or another Confluence page, Confluence offers **Display as: Inline / Card / Embed**:
- **Inline** for in-sentence references (default).
- **Card** for "go look at this" callouts (shows title + preview).
- **Embed** for live views — paste an Azure Boards query URL on the Health Check page and choose Embed: the page now shows live work items, so the documentation literally displays where the gaps are without anyone updating it.

Put smart links ONLY via the Link Registry's URLs — never invent new copies of a link inside pages.

## PART 7 — Smart design pass (10 min)

For each pasted page:
1. **Emoji in title** — click the page title → add the emoji shown in the tables above (visual scanning beats reading).
2. **Cover image** — hover top of page → **Add cover image** (pick one calm color per folder so layers are visually distinct).
3. **Status lozenge** — top of each standards page, type `/Status` → `CURRENT` (green). When a page is being revised, switch it to `UNDER REVIEW` (yellow). Readers instantly see trustworthiness.
4. **Collapse the depth** — wrap long detail sections: select the section → type `/Expand` → title it "Details — open if you need the why". The top of every page stays a 30-second read (the page's "public interface"); depth is one click away (its "private implementation").
5. **Table of contents** — `/Table of Contents` at the top of any page longer than two screens.
6. **Panels** — wrap rules in `/Info` (blue = guidance), warnings in `/Warning` (red = will bounce your item), tips in `/Note`.

## PART 8 — Wire the registry and verify (5 min)

1. Open **Link Registry** (A3) and fill the URL column — the ONLY link-filling you'll ever do.
2. Open the Engineering Handbook → replace its link-hub table with one line: "All links: see the **Link Registry**" + a smart link to it. (This is dependency inversion: pages depend on the registry, not on concrete URLs.)
3. Verification walk (5 checks): a brand-new person can (a) find where to start in <10 seconds (Welcome page), (b) reach any contact in <30 seconds (Contacts database), (c) find any tool in <30 seconds (Link Registry), (d) see the work flow visually (Lifecycle whiteboard), (e) see current gaps (Health Check page). If any check fails, that's the gap to fix — nothing else.

Done. Total ≈ 90 minutes, and after Part 8 the system maintains itself: data changes happen in databases and the registry; pages stay frozen.
