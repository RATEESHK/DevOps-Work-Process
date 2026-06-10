> Type `/Table of Contents` here after pasting to generate a contents box.

## 1. Purpose

This charter establishes a clear DevOps governance model for the team so that DevOps-related work is planned, prioritised, documented, and communicated in a consistent and transparent manner.

At present, DevOps work is **not** actioned immediately. It is actioned only after it has been refined, documented, prioritised, and brought through the agreed planning process. The immediate focus is therefore on governance, backlog structure, communication standards, and readiness of future DevOps work.

This charter:

- defines how DevOps work is raised, refined, governed, and planned;
- creates a consistent planning model for backlog and sprint readiness;
- provides a documented, visible channel of communication;
- reduces reliance on personal chats for decisions and planning;
- improves traceability between planning, engineering activity, and repository/pipeline changes;
- supports better governance, collaboration, and auditability.

## 2. Why this is needed

Recent CI/CD assessment findings show that while foundational DevOps practices exist, the operating model is not yet standardised across repositories. There are gaps across governance, documentation, PR controls, security discipline, dependency remediation, repository hygiene, and pipeline efficiency.

The team therefore requires a formal charter, a structured backlog and planning model, improved documentation and communication channels, clear standards for how items are created and progressed, and stronger linkage between planning items and GitHub engineering activity.

## 3. Scope

**In scope**

- repository governance
- CI/CD pipeline governance
- branch and PR standards
- documentation standards
- dependency and vulnerability remediation planning
- pipeline lifecycle and clean-up planning
- environment-related DevOps enablement
- backlog and sprint planning for DevOps items
- communication and collaboration for DevOps work
- integration of planning tasks with GitHub activity

**Out of scope** (unless separately approved through the planning process)

- ad hoc implementation work without a refined item
- undocumented technical changes
- work progressed only via chat or verbal agreement
- direct production or environment changes without proper planning and change controls

Use this distinction to decide when something is a **DevOps governance item** (raised here) versus a **squad delivery item** (raised in the owning team's backlog).

## 4. Objectives

- Move from informal, inconsistent DevOps planning to a structured operating model.
- Make all DevOps work visible, governed, and auditable.
- Reduce rework and stalled tickets through clear readiness criteria.
- Cut time spent locating information by maintaining a single source of truth.
- Strengthen the link between planning intent and engineering activity.

## 5. Guiding principles

- **No untracked work** — all DevOps work must be represented by an agreed backlog item before action is taken.
- **Governance before execution** — standards, ownership, and planning rules are defined before implementation work is progressed.
- **Confluence is the knowledge source** — standards, process guidance, and decisions are recorded here.
- **Azure Boards is the planning source** — all planning, prioritisation, refinement, sprint assignment, and status tracking is maintained there.
- **GitHub is the engineering source** — branches, commits, and pull requests link back to the relevant planning item.
- **No dependency on personal chats** — chats may be used for quick discussion, but no decision, requirement, or governance outcome lives only in chat.
- **Transparency and team visibility** — work is visible through shared backlog views, this space, and regular governance reviews.

## 6. Roles and decision rights

| Role | Responsibilities | Decision rights |
|---|---|---|
| **DevOps Lead / Engineering Owner** | Owns the governance model; reviews priorities and readiness; keeps standards current; supports escalation. | Final say on standards and governance exceptions. |
| **Backlog / Planning Owner** | Ensures items are captured correctly; validates ticket quality and refinement; manages backlog ordering and sprint readiness; tracks dependencies. | Owns backlog order and sprint admission. |
| **Repository / Pipeline Owner** | Provides technical input to refinement; validates implementation considerations; supports estimation and acceptance criteria. | Approves technical approach for owned repos/pipelines. |
| **Approvers / Reviewers** | Review PRs and changes against the standards. | Approve/decline changes. |
| **Contributors / Engineers** | Raise needs through the agreed intake model; avoid progressing undocumented requests; link engineering activity to items; update items with progress and evidence. | Propose work and approaches. |

## 7. Governance cadence

- **Intake** — continuous; new items raised via the template.
- **Refinement** — regular session to move items toward Definition of Ready.
- **Sprint planning** — only refined, ready items are admitted.
- **Review / closure** — items closed against Definition of Done with evidence linked.
- **Governance health review** — periodic review in the DevOps / CoP forum to assess backlog quality, upcoming priorities, fitness of standards, blockers, and currency of documentation.

## 8. Escalation path

1. Raise the blocker in the work item and tag the relevant owner.
2. If unresolved, raise at the next refinement or CoP forum.
3. If still unresolved or time-critical, escalate to the DevOps Lead / Engineering Owner for a decision.
4. Record the outcome in the **Decision Log** and link it from the work item.

## 9. Decision-log approach

Any decision that affects standards, scope, ownership, or governance is recorded in the **DevOps Decision Log** with: date, the decision, the options considered, the owner, the status, and a link to the relevant item. Decisions made verbally or in chat are copied into the log within the same day. This removes reliance on un-auditable personal chats and gives a durable, searchable record.

## 10. Expected outcome

Clearer governance, better documentation, improved backlog quality, stronger communication channels, better visibility across the team, improved linkage between planning items and engineering activity, and reduced dependency on personal chat-based decisions.