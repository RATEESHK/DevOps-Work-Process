> Type `/Table of Contents` here after pasting.

This page defines how DevOps work is raised, refined, and admitted into a sprint. The goal is that every item entering a sprint is well understood, owned, estimated, and traceable — so the team spends sprint time delivering rather than clarifying.

## 1. How to raise DevOps work

1. Create a work item in **Azure Boards** using the **DevOps Work Item Template**.
2. Set the work-item type per the hierarchy (see *Backlog Taxonomy & Azure Boards Usage*).
3. Fill in all mandatory fields below.
4. Link any supporting context (Confluence pages, repo, pipeline, assessment finding).
5. Leave the item in the **product backlog** — do **not** self-assign it to an active sprint.

Items that are not sufficiently defined remain in refinement and must not be committed to a sprint.

## 2. Mandatory fields for a refined ticket

- problem / objective
- impacted environment(s)
- impacted repository / pipeline / service
- business or engineering value
- dependencies
- acceptance criteria
- links to supporting Confluence content
- effort estimate
- priority
- owner
- target backlog / sprint

## 3. Definition of Ready (DoR)

A DevOps item is **ready** only when:

- the objective is clear;
- the impacted area is known;
- the business or engineering value is understood;
- dependencies and assumptions are captured;
- acceptance criteria are defined;
- ownership is known;
- the item is estimated;
- the item is documented sufficiently for team discussion.

Items that do not meet these conditions stay in backlog / refinement and are not actioned.

## 4. Definition of Done (DoD)

**For planning / governance items**

- the deliverable (charter section, standard, template, page) is published in the correct location;
- it has been reviewed and agreed in the CoP / governance forum;
- any decision is recorded in the Decision Log;
- linked from the relevant Confluence page and work item.

**For execution / technical items**

- change implemented and merged via a compliant PR;
- acceptance criteria met and evidenced;
- traceability in place (branch / commit / PR linked to the work item);
- documentation updated where the change affects a standard or runbook.

## 5. Prioritisation rules

Order the backlog by: regulatory / security exposure, then risk-reduction value, then engineering enablement value, then effort (prefer high-value / low-effort first). Governance and foundation work is prioritised ahead of execution work until the operating model is agreed.

## 6. Backlog vs sprint

- Work that is still being **shaped** stays in the product backlog.
- An item enters a sprint **only** when it meets the Definition of Ready, has an owner, has agreed acceptance criteria, and can be meaningfully progressed within the sprint.
- The first planning cycle is a setup-only sprint (see *Backlog Taxonomy & Azure Boards Usage*).

## 7. Dependencies and blockers

- Capture dependencies on the work item at refinement.
- Use Azure Boards predecessor/successor links to make dependencies visible.
- Raise blockers in the item first, then at refinement or the CoP forum.
- If a blocker needs a decision, escalate per the charter and record the outcome in the Decision Log.