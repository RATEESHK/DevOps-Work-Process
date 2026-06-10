> Type `/Table of Contents` here after pasting.

This page defines how unplanned work enters the system without derailing the sprint: bugs, spikes, and timeboxed external work — plus the board states and who may move items between them.

## 1. Raising a bug (anyone can raise; QA/CX triage)

Required fields — a bug without these goes back to the reporter:

```
Title:            [Component] short symptom
Environment:      prod / staging / dev + version/build
Steps to reproduce: 1. 2. 3.
Expected vs Actual:
Evidence:         screenshot / log link (Kibana query) / trace ID / video  ← mandatory
Severity:         S1 outage / S2 major function broken / S3 degraded / S4 cosmetic
Impacted users / business impact:
Related work item or release:
```

Handling: **S1** — page on-call, swarm, fix-forward or rollback now, postmortem within 48h. **S2** — enters the current sprint, displacing the lowest-priority item (PO decides what drops). **S3/S4** — backlog, sized and prioritised like stories. In-sprint defects on in-sprint stories are not bugs — they're unfinished work on that story.

## 2. Spikes (when something is not planned / not known)

If a task wasn't planned, or an approach is unknown, **do not start silently working on it** — create a spike.

- Spike = a question, not a deliverable. Title states the question: "Spike: can pipeline X reuse the central Vault module?"
- Always **timeboxed**: 1, 2, or max 3 days. The timebox is the estimate.
- Output is mandatory: a written answer on the item (and Decision Log if it sets direction) + the follow-up stories it unlocks, properly sized.
- When the timebox expires, the spike closes with whatever was learned — extensions need PO agreement and a new item.

## 3. Timeboxing external / cross-team / customer work

When a task depends on another team, a vendor, or a customer:

1. Create the item, mark dependency + the external contact (from the directory).
2. Timebox *our* effort for the sprint (e.g. 2 points: chase, prepare, integrate when received).
3. If the external party doesn't deliver within the sprint, the item returns to backlog with the dependency flagged — it does not silently roll and consume capacity.
4. Repeated external delays are raised at the governance forum, not absorbed by overtime.

## 4. Board states and who can move what

```
Backlog → Refined(Ready) → Amigos-passed → In Progress → In Review → In Test → Done-ready → Done
```

| Transition | Allowed mover |
|---|---|
| Backlog → Ready | PO (after DoR met at refinement) |
| Ready → Amigos-passed | Three Amigos session output |
| Amigos-passed → In Progress | The developer taking it (self-assign) |
| In Progress → In Review | Developer (PR open, evidence linked) |
| In Review → In Test | Reviewer (PR approved & merged to test env) |
| In Test → Done-ready | QA only (tests pass, evidence attached) |
| Done-ready → Done | PO only (AC accepted) |
| Any → Blocked flag | Anyone (must tag the unblocking owner) |

These restrictions mean each person does exactly their planned part, handoffs are explicit, and status is always truthful without a status call.

## 5. Proof / evidence requirements per state

In Review: PR link + pipeline run. In Test: test cases + results (link automated run or attach manual evidence). Done-ready: demo screenshot/recording + updated docs link. Done: PO acceptance comment. Items missing evidence get bounced back one state — by rule, not by argument.
