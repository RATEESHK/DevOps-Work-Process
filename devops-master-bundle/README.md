# DevOps Master Bundle — everything from this build, final state

One download containing the full DevOps governance operating model (Confluence + Azure Boards + GitHub) and the Claude toolkit for operating it.

```
devops-master-bundle/
├── README.md                      ← this file
├── devops-space-complete/         ← THE MAIN DELIVERABLE
│   ├── README.md                  ← paste process + file→page map + CSV import steps
│   ├── 00…21 (.md)                ← 22 paste-ready Confluence page bodies
│   └── backlog-import.csv         ← ~45 work items: Epics→Features→Stories, points, Sprint0/1 tags
└── atlassian-toolkit/             ← Claude assets for ongoing operation
    ├── prompts/atlassian-master-prompt.md   ← reusable PLAN/BUILD/AUDIT prompt
    ├── skills/atlassian-ops/                ← Claude Code skill (hub + spokes + gotchas + templates)
    ├── agents/                              ← architect / publisher / auditor agents
    ├── hooks/hooks-guide.md                 ← guardrail hooks (destructive-action block, paste lint, decision reminder)
    └── CLAUDE.md                            ← project instructions snippet
```

## What's already done (nothing left to generate)
- 22 Confluence pages: charter, intake, taxonomy, traceability, standards, S.C.A.L.E.D., templates, decision log, operating model, all roles (incl. Leadership/BA/Data/DBA/Security), sizing, ceremonies + Three Amigos, bugs/spikes/timeboxing + board states, engineering handbook (pseudo-code, Kibana), documentation/evidence, implementation plan (3 sprints, ~100 pts), KPI/OKR/Metrics/NPS framework, FAQ, CoP agenda + launch announcement + starter decisions D-001–D-005.
- Backlog as import-ready CSV matching the plan.
- Claude toolkit for future Atlassian work.

## Your adoption checklist (the only remaining work — in your tenant)
1. Create the space and paste the 22 pages (see devops-space-complete/README.md; ~1–2 h). Cloud: paste-as-plain-text; tables that mangle → paste rendered preview.
2. Fill placeholders: contacts (pages 11/19), {{links}} (page 15), KPI targets if baselines differ (page 18), {{space/board links + date}} in the launch announcement (page 21).
3. Import backlog-import.csv (Boards → Queries → Import Work Items); bulk-set iteration paths by Sprint0/Sprint1 tags. Do not re-sort the file — parents precede children.
4. Connect GitHub ↔ Azure Boards (Project settings → GitHub connections); verify one AB# link.
5. Configure board states + movers and the six queries/dashboard (pages 14/03).
6. Book the ceremony calendar with agendas; protect focus blocks (pages 10/13).
7. First CoP: use the page-21 agenda, post the announcement, confirm D-001–D-005 in the Decision Log. Sprint 0 starts.

## Support loop
Any paste/import error → bring the error or screenshot back to Claude with this bundle's file name; fix the file, not the process. Every new failure learned goes into atlassian-toolkit/skills/atlassian-ops/gotchas.md.
