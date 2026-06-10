> Addendum to **Roles, Goals & KPIs** (page 11). Paste this as a child page of it, or append these sections into page 11 directly. Add the contact rows to the directory table either way.

## Additional contact directory rows

| Area | Role | Name | Channel / handle | Escalation |
|---|---|---|---|---|
| Direction & funding | Leadership (Head of Eng / Dept lead) | | | — |
| Requirements | Business Analyst (BA) | | | PO |
| Data pipelines | Data Engineer | | | Tech Lead |
| Databases | DBA | | | Infra Lead |
| Security reviews | Security Engineer | | | CISO delegate |

## Role goals and KPIs

**Leadership** — Mission: set direction, fund the roadmap, and protect the operating model (especially no-overtime and focus time) from outside pressure. Practice: attend sprint review (not standups), consume the KPI/OKR dashboard rather than requesting status decks, unblock cross-department escalations within 2 working days, sponsor the quarterly OKR setting. KPIs: escalation resolution time; zero status-deck requests outside dashboards; quarterly OKR participation; team NPS trend.

**Business Analyst (BA)** — Mission: turn business intent into unambiguous, testable requirements before stories reach Three Amigos. Practice: elicit and write business specs with the PO, maintain the business-rules catalogue in Confluence, prepare the Given/When/Then example sets that seed QA's test cases, validate delivered work against the original business need at review. KPIs: % stories entering Three Amigos with complete spec; requirement-defect rate (defects traced to unclear requirements); spec turnaround time.

**Data Engineer** — Mission: reliable, governed data pipelines treated with the same rigour as application code. Practice: pipelines as code through the same CI/CD gates, data-quality checks (freshness, completeness, schema) with alerts to Kibana/dashboards, document datasets and lineage in Confluence, raise schema changes as items with downstream-impact noted in dependencies. KPIs: pipeline success rate; data-quality SLA attainment; % datasets documented with lineage.

**DBA** — Mission: database performance, integrity, and recoverability across on-prem and cloud. Practice: review schema/index changes via PR (no direct production DDL), own backup/restore with **tested** restores on schedule, capacity and slow-query reviews, migration scripts versioned and reversible. KPIs: successful restore-test rate; query performance regressions caught pre-production; zero unaudited production changes; RPO/RTO attainment.

**Security Engineer** — Mission: application and infrastructure security posture beyond the pipeline (the DevSecOps engineer automates the gates; the Security Engineer owns the threat picture). Practice: threat-model significant stories at Three Amigos, run/coordinate pen tests and reviews, own the security-exception register with expiry dates, advise IAM on least-privilege design, triage external security reports. KPIs: % significant stories threat-modelled before development; pen-test finding remediation within SLA; security exceptions past expiry = 0.

**Architects (note)** — already defined on page 11 as Solution Architect; where you have multiple (domain/enterprise architects), they share the same mission/KPIs with scope split recorded in the contact table.

## RACI additions

| Step | R | A | C | I |
|---|---|---|---|---|
| Business rules / spec detail | BA | PO | CX, Architect | Team |
| Threat model (significant stories) | Security Engineer | Security Lead | Architect, Dev | Team |
| Schema / migration change | DBA + Developer | Tech Lead | Data Engineer | SRE |
| Data pipeline change | Data Engineer | Tech Lead | DBA, DevSecOps | PO |
| Quarterly OKR setting | EM + PO | Leadership | Whole team | Stakeholders |
