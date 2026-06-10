This page defines the DevOps governance and planning model for the team. The immediate objective is **not** to action DevOps changes directly, but to establish a proper charter, communication channel, backlog structure, refinement model, and planning standards so that future DevOps work is visible, governed, and traceable.

All DevOps work should move through documented backlog and planning channels rather than informal personal chats, with **Confluence** used for standards, **Azure Boards** used for prioritisation and sprint planning, and **GitHub** used for code and technical implementation.

## How this space is organised

> Tip: type `/Children Display` here to auto-list the child pages, and `/Table of Contents` at the top of any long page to auto-generate a contents box from its headings.

| # | Page | What it is for |
|---|---|---|
| 1 | **DevOps Charter** | Purpose, scope, roles, principles, cadence, escalation, decision-log approach. |
| 2 | **Intake & Planning Process** | How work is raised, refined, and admitted to a sprint. DoR / DoD. |
| 3 | **Backlog Taxonomy & Azure Boards Usage** | Hierarchy, item types, sprint rules, dashboards/queries. |
| 4 | **GitHub / Work Item Traceability** | Branch naming, PR template, commit convention, AB# linking, evidence. |
| 5 | **Repository & Pipeline Governance Standards** | Branch policy, PR control, README, secrets, dependencies, lifecycle. |
| 6 | **S.C.A.L.E.D. Communication Framework** | Standard format for pitches, RCAs, tickets, PR descriptions. |
| 7 | **DevOps Work Item Template** | Copy-paste template for every refined ticket. |
| 8 | **DevOps Governance Backlog** | The Epic → Feature → Story plan (also import-ready as CSV). |
| 9 | **DevOps Decision Log** | Where decisions are recorded — never chat-only. |
| 10 | **Team Operating Model & Working Agreement** | Async-first, meeting rules, focus blocks, no-overtime, freedom of choice. |
| 11 | **Roles, Goals & KPIs** | Mission/practice/KPIs per role, contact directory, RACI, permission boundaries. |
| 12 | **Story Sizing & Estimation Guide** | Fibonacci scale, days mapping, poker rules, capacity caps. |
| 13 | **Sprint Ceremonies & Three Amigos** | Cadence, timeboxed agendas, business-spec template, Amigos gate. |
| 14 | **Bug, Spike & Timebox Policy** | Bug template + severities, spikes for unknowns, dependency timeboxing, board states & movers. |
| 15 | **Engineering Handbook** | DevOps/DevSecOps/SRE/cloud/hybrid/on-prem definitions, dev & tester pseudo-code, Kibana logging standard, link hub. |
| 16 | **Documentation & Evidence Standard** | Doc-as-you-go, evidence per state, release-from-the-board. |
| 17 | **Implementation Plan** | 3 sprints, story points, approximate days, verified task breakdowns. |
| 18 | **Measurement Framework** | KPI vs OKR vs Metrics vs NPS, standing KPI set, anti-gaming rules. |
| 19 | **Extended Roles** | Leadership, BA, Data Engineer, DBA, Security Engineer (child of page 11). |
| 20 | **FAQ / How to Engage DevOps** | Seeded answers; grows from real channel questions. |
| 21 | **CoP Agenda & Launch Kit** | Recurring forum agenda, launch announcement, starter decisions D-001–D-005. |

## Operating principles (the short version)

- **No untracked work** — every change maps to a backlog item before action.
- **Governance before execution** — standards, ownership and planning rules come first.
- **Confluence is the knowledge source**; **Azure Boards is the planning source**; **GitHub is the engineering source**.
- **No decision lives only in a personal chat** — it is copied into the work item or the Decision Log.
- **Transparency** — work is visible to the wider team through shared backlog views and this space.

## How to engage DevOps

1. Read the **Intake & Planning Process** page.
2. Raise a work item in Azure Boards using the **DevOps Work Item Template**.
3. Bring it to refinement; it must meet the **Definition of Ready** before it enters a sprint.
4. Link any branch, commit, or PR back to the work item (see **GitHub / Work Item Traceability**).
5. Record any decision in the **Decision Log**.