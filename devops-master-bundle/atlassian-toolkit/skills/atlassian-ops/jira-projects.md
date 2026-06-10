# Jira Projects & Planning (with Azure Boards mapping)

## Hierarchy

Jira: **Epic → Story/Task → Sub-task** (Premium adds Initiatives above Epics; "Feature" needs Premium/custom hierarchy).
Azure Boards: **Epic → Feature → User Story/Requirement → Task/Bug** (order fixed).

When the user's model is Epic → Feature → Story (Azure-style) and the target is standard Jira: map **Feature → Epic** and **the original Epic → a label or component**, and say so explicitly. Don't silently flatten.

## Project setup sequence (Jira)

1. Project: company-managed for shared workflows/governance; team-managed for autonomy. Governance work → company-managed.
2. Issue types confirmed (Epic, Story, Task, Bug; add Spike as a Task-type or label — Spike isn't a default type anywhere, including Azure Boards).
3. Workflow: keep minimal (To Do → In Progress → In Review → Done). Add a `Blocked` flag, not a status.
4. Board: scrum board for sprint cadence; backlog enabled.
5. Filters/dashboards before launch: Ordered backlog · Not Ready (missing DoR fields) · Ready for sprint · Blocked · In current sprint · Traceability gaps.

## Bulk-loading a backlog

- **Jira CSV import** (Settings → System → External System Import). Columns: `Issue Type, Summary, Description, Epic Link/Parent, Labels, Priority`. Parent rows (Epics) must import before children, or use two passes.
- **Azure Boards:** CSV import from Boards → Queries, or paste the Epic/Feature/Story table and create top-down in the backlog view with the Mapping pane.
- Always generate the import file; never tell the user to hand-create 40 stories.

## Sprint 0 rule

First sprint = planning artifacts only (charter, space, templates, taxonomy, dashboards, traceability model, assessment decomposition). Technical/execution items stay in backlog until governance is approved and DoR is met.

## Useful JQL starters

```
project = DEVGOV AND status != Done ORDER BY priority DESC          -- ordered backlog
project = DEVGOV AND ("Acceptance Criteria" is EMPTY OR "Story Points" is EMPTY)  -- not ready (adjust field names)
project = DEVGOV AND flagged = Impediment                            -- blocked
project = DEVGOV AND sprint in openSprints()                         -- current sprint
project = DEVGOV AND status = "In Progress" AND development is EMPTY -- traceability gaps (dev panel empty)
```

## JSM (when intake should be a service desk)

If the team wants request-style intake (vs backlog grooming), create a JSM project with request types mapped to the work-item template fields, and automation to clone accepted requests into the delivery project. Don't run delivery inside JSM.
