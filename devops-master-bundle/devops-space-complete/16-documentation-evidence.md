> Type `/Table of Contents` here after pasting.

Documentation happens *at the same time as the work* — that's the rule that keeps everyone in sync and lets releases happen without delays. Nobody writes docs "later".

## 1. Who documents what, when

| Role | Documents | When |
|---|---|---|
| PO | Business spec in the story | Before Three Amigos |
| Developer | Pseudo-code → code comments → contract/runbook updates | In the same PR as the change |
| QA | Test cases + results | Cases before dev starts; results before Done-ready |
| DevOps/Infra | Pipeline/infra changes in the standards pages | Same PR / same day |
| SRE | Postmortems, SLO changes | Within 48h of incident |
| Everyone | Decisions → Decision Log | Same day |

## 2. Evidence rules (proof attached, always)

Every state transition has an evidence requirement (see the board-state table). The principle: a reviewer, auditor, or new joiner can reconstruct what happened from the item alone — PR, pipeline run, test results, demo recording, updated doc links — with zero chat archaeology. Items without evidence bounce back a state automatically; this is enforced by the workflow, so it's never personal.

## 3. Keeping docs light

- Update the existing page; don't create "v2" pages. Page history is the version control.
- One concern per page; link, don't duplicate.
- A doc update that takes >15 minutes alongside the change probably means the doc structure is wrong — raise an item to fix the structure.
- FAQs grow from real questions: when someone answers a question in the channel, the answer goes into the FAQ page and the link is posted back.

## 4. Release readiness from documentation

Because specs, tests, evidence, and doc updates accrue per item during the sprint, a release candidate's notes are assembled by query (all Done items in the release), not written from memory. The release checklist only verifies: all items evidenced, standards pages current, rollback step documented. That's how documentation speed becomes release speed.
