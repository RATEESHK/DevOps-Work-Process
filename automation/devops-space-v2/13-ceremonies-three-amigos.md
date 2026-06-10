> Type `/Table of Contents` here after pasting.

Every ceremony below has a fixed agenda, timebox, and required attendees. Anything that can't be resolved in the timebox becomes a backlog item — meetings never run long.

## 1. Sprint cadence (2-week sprint)

| Day | Ceremony | Timebox | Who |
|---|---|---|---|
| Day 1 | Sprint Planning | 90 min | Whole team |
| Daily | Standup (async-friendly) | 15 min | Delivery team |
| Day 3 & 8 | Backlog Refinement | 60 min | PO, Tech Lead, Dev rep, QA rep |
| Continuous | Three Amigos (per story batch) | 30 min | PO + Dev + QA (+Architect/Security for significant items) |
| Day 10 | Sprint Review / Demo | 60 min | Team + stakeholders |
| Day 10 | Retrospective | 60 min | Delivery team |

Total ceremony load ≈ 1 day per person per sprint, leaving 9 days of delivery and focus time.

## 2. Standup (15 min, walk the board right-to-left)

Per item nearest Done: what moves it today, any blocker (flag + tag, don't solve in standup). Personal yesterday/today only if it adds information. Anyone with nothing relevant can pass. Async option: post the same three lines in the channel before 10:00 — attendance is then optional.

## 3. Sprint Planning (90 min)

Agenda: (10) sprint goal proposed by PO → (50) pull Ready items top-down until capacity, confirm owner + tasks exist per story → (20) risks & dependencies walk → (10) confirm commitment and publish the plan. Input rule: only DoR-passing items may be pulled. Output: sprint goal + committed items posted to the channel.

## 4. Three Amigos (30 min per story batch — the quality multiplier)

Held *before* development starts, for every story. Attendees: PO (business intent), Developer (feasibility), QA (testability). Add Architect/DevSecOps when the story touches architecture, data, or security.

Agenda (per story, ~10 min each, max 3 stories per session):

1. **Business spec walk (3 min)** — PO states the user value and the business rules in plain language. Spec must exist in the item *before* the session (template below).
2. **Example mapping (5 min)** — turn rules into concrete examples: "Given / When / Then" scenarios including edge cases. These become the acceptance tests.
3. **Confirm (2 min)** — Dev confirms approach + pseudo-code stub; QA confirms test cases; gaps become AC updates or a spike. Story is marked **Amigos-passed** (a board state requirement before *In Progress*).

Business spec mini-template (paste into the story):

```
User / persona:
Problem & value:
Business rules:        (numbered)
Examples:              Given… When… Then… (≥1 happy, ≥1 edge, ≥1 negative)
Out of scope:
KPIs affected:
Compliance notes:
```

## 5. Sprint Review (60 min)

Demo working software against the sprint goal; PO accepts/rejects per AC; contributors named per item (including small tasks); stakeholder feedback captured as backlog items on the spot. No slide decks — the board and the demo are the material.

## 6. Retrospective (60 min)

What went well / what didn't / what we'll change (max 2 improvement actions, each becomes a tracked item with an owner). Standing checks: any overtime this sprint (why?), meeting-load trend, "what work did you enjoy / want more of" for interest-based routing next sprint.

## 7. Documentation-in-sync rule

Docs are produced *during* the sprint, not after: the story's PR updates affected runbooks/standards; QA attaches test evidence; the demo recording link goes on the item. Release notes are then auto-assemblable from the board — which is what lets releases ship fast with no documentation lag.
