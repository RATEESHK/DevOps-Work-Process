> Type `/Table of Contents` here after pasting.

This page defines the work-item hierarchy, what each item type is used for, how items move into a sprint, and the dashboards/queries the team relies on.

## 1. Work-item hierarchy

```
Epic
└── Feature
    └── User Story / Requirement
        └── Task / Bug / Spike
```

In Azure Boards the order of this hierarchy is fixed; teams can customise which types appear and add portfolio backlogs, but the hierarchy order itself does not change.

## 2. Item-type definitions

| Type | Used for | Backlog level |
|---|---|---|
| **Epic** | A major DevOps governance or enablement theme. | Portfolio |
| **Feature** | A grouped outcome under a theme. | Portfolio |
| **User Story / Requirement** | A planned deliverable or work package. | Product (team) |
| **Task** | Implementation detail under a story. | Sprint |
| **Bug** | A defect to correct. | Product / Sprint |
| **Spike** | A time-boxed investigation. Usually tracked as a Task (or a tagged Story/PBI) since Spike is not a default Azure Boards type. | Product / Sprint |

## 3. Governance vs execution

- **Epics and Features** describe governance themes and grouped outcomes.
- **Stories / Requirements** are the planned deliverables (a charter section, a standard, a template).
- **Tasks / Bugs / Spikes** carry implementation detail, defects, and investigations.
- Governance and structure are created **first**; backlog items are defined and refined **next**; sprint assignment happens **only** when an item is ready.

## 4. Backlog model (Azure Boards)

- The **product backlog** is the day-to-day plan of stories, requirements, and bugs the team works through.
- The **portfolio backlog** groups that work under Features and Epics for larger initiatives.
- The **sprint backlog** is a filtered subset of the product backlog assigned to a specific iteration path.
- Work moves from intake → product backlog → sprint once it is defined, refined, and owned.

## 5. Sprint planning rules

Only refined and ready items may enter a sprint. Sprint planning must confirm:

- the item meets the Definition of Ready;
- dependencies are visible;
- the owner is known;
- scope is realistic;
- acceptance criteria are agreed;
- it can be meaningfully progressed within the sprint.

### First planning cycle (setup-only)

The first sprint, **"DevOps Governance & Backlog Setup,"** includes only:

- governance definition and charter drafting
- Confluence space and page creation
- ticket-template creation
- backlog taxonomy definition
- query / dashboard setup
- GitHub traceability model definition
- decomposition of assessment findings into backlog items

Once governance is approved, technical items move into later delivery sprints.

## 6. Queries and dashboards

Create and pin these so planning status is self-serve:

- **DevOps backlog (ordered)** — all items not yet Done, by priority.
- **Not Ready** — items missing DoR fields (objective, AC, estimate, owner).
- **Ready for sprint** — items meeting DoR and not yet assigned to a sprint.
- **In current sprint** — items in the active iteration path.
- **Blocked** — items tagged `blocked`.
- **Traceability gaps** — items in progress with no linked branch/PR.

Surface these on a shared Azure Boards dashboard reviewed at the CoP forum.