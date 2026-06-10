# 🔍 CI/CD Assessment — Findings & Remediation Tracker (22/05/2026)

> Source: CI/CD & Repository Assessment, 22/05/2026. Scope: **Tink Payments CWA** and **Tink Payments API**. This page is the evidence anchor — every remediation backlog item links back here. Status lozenge: `/Status` → CURRENT.

## 1. Headline

Both repositories show foundational DevOps practices with a clear maturity gap across governance, security, and operational discipline. CWA has the stronger governance baseline but historically high security exposure; API is less mature overall. Net: the operating model is not yet standardised across Tink repositories — which is exactly what this space exists to fix.

## 2. Maturity comparison

| Capability | CWA | API |
|---|---|---|
| Branch governance | ✅ Strong | ⚠️ Basic |
| PR controls | ✅ Good | 🔴 Weak (1 reviewer) |
| Security management | 🔴 Reactive (high volume) | 🔴 Reactive (open issues) |
| Documentation | ✅ Adequate | 🔴 Poor (template README) |
| Repo hygiene | ⚠️ Moderate gaps | ⚠️ Moderate gaps |
| CI/CD efficiency | ✅ Stable | 🔴 Inefficient (17 low-usage pipelines) |

## 3. Findings → backlog mapping (the gap tracker)

| # | Finding (evidence) | Repo | Severity | Backlog item | Status |
|---|---|---|---|---|---|
| F-01 | 154 vulnerabilities (majority High/Critical), fixed reactively ~4 days before assessment — systemic dependency risk | CWA | 🔴 | Dependabot + remediation SLA (Crit/High <7d, Mod <14d) | Planned |
| F-02 | .gitignore present but effectiveness not evidenced; no CI validation | CWA | ⚠️ | .gitignore baseline + CI validation gate | Planned |
| F-03 | Multiple stale branches; no lifecycle management | CWA | ⚠️ | Auto-delete merged; 30–60 day stale policy | Planned |
| F-04 | Only 1 PR reviewer required | API | 🔴 | Enforce minimum 2 reviewers + code owners | Planned |
| F-05 | README is basic NestJS template — no purpose/architecture/CI/integration info | API | 🔴 | README to full baseline incl. integration points | Planned |
| F-06 | `cert.per` file present in repo; .gitignore coverage unclear | API | 🔴 | Validate/remove cert.per; extend .gitignore (certs, env configs, secrets) | Planned |
| F-07 | Open vulns: UUID buffer bounds (#56, #57 — package.json / package-lock.json); file-type ZIP bomb (#46, 2 months); file-type ASF infinite loop (#43, 2 months) — no SLA enforcement | API | 🔴 | Remediate #43/#46/#56/#57 within SLA; SLA policy live | Planned |
| F-08 | 17 low-usage pipelines — sprawl, overhead, outdated-pipeline risk | API | 🔴 | Pipeline rationalisation + quarterly governance review | Planned |
| F-09 | No secret scanning (both repos), incl. historical commits | Both | ⚠️ | Secret scanning + historical scan | Planned |
| F-10 | No mandatory quality gates (lint/Sonar) | Both | ⚠️ | Quality gates block merge | Planned |
| F-11 | No shift-left controls (pre-commit hooks) | Both | ⚠️ | Pre-commit: lint, secret detection, dependency checks | Planned |
| F-12 | No standardised pipeline template across Tink/ICS | Both | ⚠️ | Golden pipeline template | Planned |
| F-13 | No audit dashboards (vuln trends, hygiene, PR compliance) | Both | ⚠️ | Audit & compliance dashboards | Planned |

> Update the Status column as items move (Planned → In Sprint → Done + evidence link). When all rows read Done, this assessment is closed and the next one is scheduled.

## 4. Priority order (from the report)

Immediate: F-04, F-07, F-06, F-08 (API) and F-01, F-02 (CWA). Medium-term: F-03, F-05, F-09, F-10. Strategic: F-11, F-12, F-13. All remain **planned-not-executed** until items pass Definition of Ready and Three Amigos — per the charter.
