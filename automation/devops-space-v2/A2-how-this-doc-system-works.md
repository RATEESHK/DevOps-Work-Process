# 🧩 How This Documentation Works

This page explains the design of the documentation itself, so you can use it, trust it, and extend it without breaking it. The space is built like good software — and you don't need to be a programmer to follow the four ideas below.

## 1. One page, one job (high cohesion)

Every page answers exactly one question, completely. Sizing questions → Story Sizing page, all of it, nothing else. Like a well-organised toolbox 🧰: all screwdrivers in one tray — you never check three trays for one tool, and adding a new screwdriver never disturbs the hammers.

**What this means for you:** if a page only half-answers your question, don't search five other pages — the missing half is a documentation gap. Report it (Health Check page) instead of asking in chat.

## 2. Pages link, never copy (low coupling)

No page repeats another page's content; it links instead. Like LEGO bricks 🧱: each brick is complete, and bricks connect through standard studs — you can swap one brick without rebuilding the castle. When the sizing rules change, we edit ONE page and every link to it is automatically current. If we'd copied those rules onto six pages, we'd update one and forget five — and you'd be following stale rules without knowing.

**What this means for you:** trust links over memory, and if you spot the same content in two places, one of them is already wrong or soon will be — report it.

## 3. Quick answer on top, depth behind a click (encapsulation)

Each page opens with the 30-second answer; the long "why" sits inside collapsible *Expand* sections. Like a TV remote 📺: you press one button; the circuit diagram exists, but it's inside the case, available only when you choose to open it.

**What this means for you:** skim the top of any page with confidence — it's the official answer. Open the expands only when you need to argue the why.

## 4. Live data lives in one registry (dependency inversion)

Pages never hard-code things that change — names, URLs, decisions. Those live in three single sources: the **Contacts** database, the **Decisions** database, and the **Link Registry**. Pages point at them, like every appliance in your house plugging into standard wall sockets 🔌 rather than being wired directly into the mains. Rewire the house (a tool URL changes), and every appliance still works — you updated one socket.

**What this means for you:** never write a tool URL or a person's name into a page. Point to the registry/databases. That's the entire maintenance burden of this space, concentrated into three editable spots.

## 5. The layers (why the five folders exist)

Start Here (orientation) → How We Work (processes) → Standards (rules) → Records (live data) → Team Hub (people). A question travels down the layers like an order through a restaurant kitchen 🍳: front-of-house seats you, the station cooks your dish, the recipe book defines the dish, the inventory holds the ingredients. Stations don't raid each other's counters — and our folders don't duplicate each other's content.

## 6. Rules for changing this documentation

1. Correct content is never rewritten for taste — change only what is wrong, and say *what/why/where* in the page comment when you do (small change surface, like a surgeon making the smallest possible incision).
2. New content goes to the page that owns the topic; if no page owns it, propose a new page at the CoP — don't bolt unrelated sections onto an existing page (that's how toolboxes turn into junk drawers).
3. Standards pages change only via CoP agreement + a Decisions row. Process pages change via retro outcomes. Databases/registry change freely — that's what they're for.
4. Every change keeps the page's "top = quick answer, expands = depth" shape.

## 7. How you'll know something is going wrong

The system is designed to *show* its gaps, not hide them: the Health Check page lists the symptoms (stale lozenges, duplicate content, items missing evidence, unanswered FAQ entries) and routes each symptom to its fix. A healthy documentation system is like a smoke detector 🔔 — silence means safe, and when it beeps, it tells you which room.
