> Type `/Table of Contents` here after pasting. Fill the Contacts table with real names — that table is what lets anyone reach the right person without a call.

This page defines who does what, the goal and KPIs for every role, and how to contact them. Each role's KPIs are visible so every contribution — even a small task — is measurable and credited.

## 1. Contact directory (fill in)

| Area | Role | Name | Channel / handle | Escalation |
|---|---|---|---|---|
| Business spec | Product Owner | | | Manager |
| Architecture | Solution Architect | | | Eng Lead |
| Implementation | Tech Lead | | | Eng Lead |
| DevOps / pipelines | DevOps Engineer | | | DevOps Lead |
| Security | DevSecOps Engineer | | | CISO delegate |
| Reliability | SRE | | | On-call manager |
| Infra / cloud | Infra / Cloud Engineer | | | Infra Lead |
| Network / hardware | Network Engineer | | | Infra Lead |
| Identity | IAM Engineer | | | Security Lead |
| Platform | Platform Engineer | | | Eng Lead |
| Frontend | FE Developer(s) | | | Tech Lead |
| Backend | BE Developer(s) | | | Tech Lead |
| Mobile | Android / iOS Developer(s) | | | Tech Lead |
| Quality | Tester / QA Engineer(s) | | | QA Lead |
| Customer experience | CX Engineer | | | Support Lead |
| Delivery | Engineering Manager | | | Head of Eng |

## 2. Role goals and KPIs

Each role below has: **Mission** (why the role exists), **Daily practice** (what they do in a sprint), and **KPIs** (how contribution is shown). KPIs measure outcomes, not hours — nobody is rewarded for overtime.

**Product Owner** — Mission: maximise value of the backlog. Practice: keep backlog ordered, write/approve business specs before Three Amigos, accept stories against AC, be available for same-day question turnaround in the channel. KPIs: % of sprint items meeting DoR at planning; acceptance turnaround time; backlog ordered ≥2 sprints ahead.

**Engineering Manager** — Mission: remove blockers and protect focus time. Practice: resolve escalations within a day, keep meeting load within the rules, run capacity planning, watch for overtime signals. KPIs: blocker resolution time; team meeting hours/week trend; zero unplanned overtime sprints.

**Solution Architect** — Mission: designs that pass risk/compliance the first time. Practice: produce/maintain architecture pages, review designs at Three Amigos for significant stories, keep ADRs (architecture decision records) in the Decision Log. KPIs: % designs passing review first time; ADR currency.

**Tech Lead** — Mission: implementation quality and unblocking developers. Practice: refinement input, PR reviews within SLA, pairing on hard problems. KPIs: PR review turnaround; escaped-defect trend.

**Frontend / Backend Developer** — Mission: deliver stories to DoD with tests and docs in the same PR. Practice: pick items from the sprint only, follow pseudo-code/AC from refinement, attach evidence (tests, screenshots, pipeline run) to the item, raise a spike when something is unknown rather than guessing. KPIs: stories completed to DoD; rework rate; PR cycle time.

**Android / iOS Developer** — Same as developer, plus: store/release checklist adherence, crash-free sessions %, app review pass rate.

**Tester / QA Engineer** — Mission: prevent defects, not just find them. Practice: join Three Amigos and write test cases *before* dev starts, automate regression for every story, raise bugs per the Bug Policy with evidence. KPIs: % stories with tests defined pre-development; automation coverage; escaped defects to production.

**DevOps Engineer** — Mission: paved-road pipelines so teams self-serve. Practice: maintain CI/CD templates, gates (lint, SAST, vulnerability), pipeline lifecycle hygiene. KPIs: pipeline success rate; lead time for change; deployment frequency.

**DevSecOps Engineer** — Mission: security as code, shifted left. Practice: maintain policy-as-code (e.g. OPA/Checkov), secret-scanning, dependency SLAs. KPIs: mean time to remediate by severity; % builds passing security gates first time; zero static credentials.

**SRE** — Mission: reliability within agreed error budgets. Practice: define SLI/SLO per service, own observability (logs/metrics/traces — see Engineering Handbook for the Kibana/ELK standard), run incident process and blameless postmortems. KPIs: SLO attainment; MTTR; postmortem actions closed.

**Platform Engineer** — Mission: internal developer platform — golden paths, templates, shared modules. KPIs: adoption of paved-road templates; time-to-first-deploy for a new service.

**Infra / Cloud Engineer** — Mission: provision and operate cloud, hybrid, and on-prem infrastructure as code. Practice: Terraform/IaC only (no console changes), capacity and cost reviews. KPIs: % infrastructure under IaC; drift incidents; cost variance.

**Hardware & Network Engineer** — Mission: connectivity, firewalls, load balancers, DNS for on-prem and hybrid links. Practice: change-controlled network changes with rollback plans. KPIs: change success rate; network-caused incident count.

**IAM Engineer** — Mission: least-privilege access that never blocks delivery. Practice: role mapping via the central modules, access reviews, JML (joiner/mover/leaver) automation. KPIs: access request turnaround; privileged-access review completion; zero shared accounts.

**CX Engineer** — Mission: voice of the customer inside the sprint. Practice: triage customer-reported issues into bugs/stories with evidence, feed insight to the PO. KPIs: triage turnaround; customer-found vs team-found defect ratio.

## 3. Who does what — quick RACI for a story's life

| Step | R (does) | A (accountable) | C (consulted) | I (informed) |
|---|---|---|---|---|
| Business spec | PO | PO | CX, Architect | Team |
| Three Amigos | PO + Dev + QA | Tech Lead | Architect, Security | Team |
| Implementation | Developer | Tech Lead | DevOps, IAM as needed | PO |
| Testing | QA | QA Lead | Developer | PO |
| Pipeline / deploy | DevOps | DevOps Lead | SRE, DevSecOps | Team |
| Release decision | PO + Tech Lead | EM | SRE | Stakeholders |
| Production health | SRE | SRE | DevOps | Team |

## 4. Access and permission boundaries (restrict by working process)

People can only perform the actions of their role state: developers cannot approve their own PRs or deploy to production; only DevOps/SRE roles hold deploy permissions; only the PO accepts stories; only leads close decisions. Board states are restricted the same way — e.g. only QA moves an item from *In Test* to *Done-ready*, only the PO from *Done-ready* to *Done*. This means everyone does exactly what is planned, and anything unplanned must enter as a new item, spike, or timebox (see Bug, Spike & Timebox Policy).
