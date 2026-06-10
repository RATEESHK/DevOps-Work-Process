> Type `/Table of Contents` here after pasting. Points use our Fibonacci scale; the day figures are planning approximations for a team of ~6–8 with a Backlog Owner driving setup. Verify each story's tasks at refinement before committing — the task lists below are the proposed breakdown to verify.

## Implementation plan — from zero to operating model

Total: **3 sprints (6 weeks) to a fully running model**, with the team delivering normally from Sprint 2 onward. Approximate effort ≈ 100 points across the three sprints.

## Sprint 0 — "Governance & Backlog Setup" (Days 1–10, ~34 points)

Goal: space published, backlog loaded, rules agreed. Planning work only — no technical remediation.

| Story | Pts | ~Days | Proposed tasks (verify at refinement) |
|---|---|---|---|
| Publish Confluence space + pages 0–9 | 5 | 3 | Create space; paste 10 page bodies; macros/labels; permissions; register work-item template |
| Publish team pages 10–17 (this set) | 3 | 2 | Paste 8 bodies; fill contact directory; replace {{links}} |
| Load governance backlog into Boards | 3 | 1.5 | Create Epics/Features/Stories; order backlog; tag themes |
| Define board states + restrictions | 3 | 1.5 | Configure columns/states; set per-state movers; evidence rules |
| Queries & dashboards | 3 | 1.5 | Ordered backlog, Not-Ready, Ready, Blocked, Current sprint, Traceability-gap |
| Connect GitHub ↔ Boards | 2 | 1 | Project settings connection; test AB# link on a sample PR |
| Agree DoR/DoD + sizing scale at CoP | 2 | 0.5 (session) | Walk pages 12/14; record decisions in Decision Log |
| Ceremony calendar + focus blocks | 1 | 0.5 | Book recurring invites with agendas; protect focus hours |
| Sprint-0 review & decision log | 2 | 0.5 | Demo space; capture gaps as backlog items |
| Contact directory + link hub filled | 2 | 1 | Names, channels, escalation; all {{link}} placeholders |
| Pilot Three Amigos on 2 sample stories | 3 | 1 | Run sessions; refine the spec template from experience |
| Buffer / unplanned | 5 | — | — |

## Sprint 1 — "Standards & First Remediation Planning" (Days 11–20, ~36 points)

Goal: standards baselined; assessment findings decomposed into sized, Ready items.

| Story | Pts | ~Days | Proposed tasks (verify) |
|---|---|---|---|
| Branch + PR governance live on repos | 5 | 3 | Branch protection; CODEOWNERS; PR template with AB# field; reviewer rules |
| README baseline rolled to all repos | 3 | 2 | Template; PR per repo; verify against standard |
| Secret-handling & .gitignore baseline | 5 | 3 | Standard .gitignore; secret scanning on; rotate any exposures |
| Dependency & vulnerability SLA defined | 3 | 1.5 | Severity SLAs; scanning in CI; triage owner |
| Pipeline inventory + rationalisation plan | 5 | 3 | Inventory 17 low-usage pipelines; owners; retire/merge proposals |
| Decompose CWA + API assessment findings | 5 | 2.5 | One sized story per finding with DoR fields |
| Logging standard adopted (Kibana) | 5 | 3 | JSON log format; correlation ID; saved searches; bug-template link |
| Reference stories per size captured | 1 | 0.5 | Link 1 example per point value into page 12 |
| Retro improvements from Sprint 0 | 2 | 1 | Max 2 actions, owners assigned |
| Buffer | 2 | — | — |

## Sprint 2 — "Execution Begins" (Days 21–30, ~30+ points)

Goal: first technical remediation items (now Ready + Amigos-passed) delivered through the full flow; the operating model is simply how work happens now.

Pull from the decomposed assessment backlog by priority — e.g. vulnerability gates in CI/CD (5), stale-branch lifecycle automation (3), PR reviewer strengthening (3), cert/secret risk review (5), first pipeline retirements (3) — sized and verified at refinement like any other work. From here, velocity is measured and future sprints plan against the rolling average.

## Daily rhythm once running (how the time is actually spent)

Per person per day: 15-min standup + ~30 min responding to tags/reviews + protected 2–3h focus block + remaining time on sprint items. Ceremonies total ≈1 day per sprint. No overtime by design — the sprint is capacity-capped at planning, unplanned work enters as spike/timeboxed items, and overtime occurrences are retro topics, not habits.

## Verification loop for this plan

Each story above is *proposed*; it becomes committed only after refinement verifies tasks/AC and Three Amigos passes it. Anything the team finds mis-sized gets resized there — the plan serves the team, not the reverse.
