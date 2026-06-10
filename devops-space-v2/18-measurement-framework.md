> Type `/Table of Contents` here after pasting.

This page defines how we measure: what KPIs, OKRs, metrics, and NPS each mean for us, how they connect, who owns them, and the review cadence. The rule that keeps measurement honest: **metrics inform, they never punish** — they measure the system, not individuals, and are never used to justify overtime.

## 1. The four terms and how they relate

- **Metric** — any raw measurement the system produces continuously (deployment frequency, PR cycle time, error rate, test coverage, MTTR). Metrics are facts; on their own they carry no target.
- **KPI (Key Performance Indicator)** — a *chosen* metric with a target and an owner, used to judge the health of an ongoing process. KPIs are standing: they persist sprint after sprint (e.g. "S1 MTTR < 1 hour", "pipeline success rate ≥ 95%"). The per-role KPIs live on the Roles, Goals & KPIs page.
- **OKR (Objectives and Key Results)** — a *time-boxed ambition* (usually quarterly): one qualitative Objective plus 2–4 measurable Key Results. OKRs drive change; KPIs guard the baseline. Example — Objective: "Make releases boring." KR1: deployment frequency from 2/month → 2/week. KR2: change-failure rate < 10%. KR3: zero release-day overtime incidents.
- **NPS (Net Promoter Score)** — "how likely are you to recommend…" on a 0–10 scale; % promoters (9–10) minus % detractors (0–6). We use it in two forms: **customer NPS** (owned by PO + CX, from product surveys) and **team/internal NPS** (owned by EM, quarterly anonymous pulse: "would you recommend working in this team?") — the second is our satisfaction guardrail for the no-overtime, freedom-of-choice principles.

How they stack: **Metrics** feed **KPIs** (health) and **Key Results** (change); **OKRs** set direction for a quarter; **NPS** checks whether customers and the team are actually happier as a result.

## 2. Standing KPI set (team level)

| Area | KPI | Target (initial) | Owner | Source |
|---|---|---|---|---|
| Flow | Lead time for change | < 5 days | DevOps Lead | Boards + GitHub |
| Flow | Deployment frequency | ≥ 1/week per service | DevOps Lead | Pipeline |
| Quality | Change-failure rate | < 15% | Tech Lead | Pipeline + incidents |
| Quality | Escaped defects / sprint | Trend ↓ | QA Lead | Boards |
| Reliability | SLO attainment | ≥ 99.x% per service | SRE | Dashboards |
| Reliability | MTTR (S1/S2) | < 1h / < 1 day | SRE | Incident log |
| Security | Critical vuln remediation | Within SLA | DevSecOps | Scanner |
| Planning | DoR compliance at planning | 100% | Backlog Owner | Boards query |
| Traceability | Items in progress with linked PR | 100% | DevOps Lead | Traceability-gap query |
| People | Unplanned overtime occurrences | 0 | EM | Retro log |
| People | Internal team NPS | > +30 | EM | Quarterly pulse |

(The four DORA metrics — lead time, deployment frequency, change-failure rate, MTTR — are the industry-standard delivery measures; the rest guard quality, security, planning hygiene, and people.)

## 3. OKR cycle

Set quarterly at the governance forum: max 2 Objectives for the team, 2–4 Key Results each, every KR tied to a metric already collected (no hand-counted KRs). Graded 0.0–1.0 at quarter end; 0.7 is success — 1.0 every time means the ambition was too low. OKRs are recorded on this page and in the Decision Log; progress is a 5-minute read-out at sprint review, not a separate meeting.

## 4. Review cadence (no extra meetings)

Sprint review: KPI dashboard glance + OKR progress (5 min inside the existing timebox). Retro: people-KPIs (overtime, meeting load, enjoyment). Quarterly governance forum: OKR grading, KPI target adjustments, NPS results. All dashboards are self-serve links in the Engineering Handbook link hub — nobody compiles a report by hand.

## 5. Anti-gaming rules

A KPI with a target invites gaming; these rules prevent it: metrics are reviewed in pairs (speed KPIs always alongside quality KPIs); no individual leaderboards; targets change only at the quarterly review with a Decision Log entry; and any KPI that drives bad behaviour is itself raised as a retro item and replaced.
