# Governance & Rollout

## Canonical page tree (adapt, don't expand without reason)

```
[Space home] Overview + Children Display
├── Charter                 (purpose, scope, principles, roles, cadence, escalation)
├── Intake & Planning       (how to raise work, mandatory fields, DoR, DoD, prioritisation)
├── Backlog Taxonomy        (hierarchy, item-type definitions, sprint rules, dashboards)
├── Traceability            (branch/commit/PR conventions, link syntax, evidence)
├── Repo & Pipeline Standards (branch policy, PR controls, README, secrets, dependencies, lifecycle)
├── S.C.A.L.E.D. Framework  (comms standard, long + short formats)
├── Work Item Template      (also registered as a Confluence template)
├── Governance Backlog      (the Epic→Feature→Story plan)
└── Decision Log            (table or /Decision entries)
```

## Definition of Ready (minimum fields)

objective · impacted environment(s) · impacted repo/pipeline/service · value · dependencies · acceptance criteria · supporting links · estimate · priority · owner · target backlog/sprint. Not all present → stays in refinement, not actioned.

## Definition of Done

Planning items: published in the right place + reviewed in the governance forum + decisions logged + linked both ways.
Execution items: merged via compliant PR + AC evidenced + traceability links present + affected docs updated.

## S.C.A.L.E.D. comms standard

Use for architecture pitches, RCAs, tickets, PR descriptions. Two formats:
- **Long** (risk boards, RCAs): one spoken paragraph per element — Scale & blast radius, Compliance & constraints, Action & automation, Leverage of existing shared services, Effect with hard metrics, Diffusion into docs/guardrails.
- **Short** (tickets/PRs): six labelled one-liners `[S] [C] [A] [L] [E] [D]`.
Why each element exists: S kills "sounds too small"; C surfaces regulatory limits up front instead of as negativity; A keeps governance from stalling execution; L proves reuse over silo-building; E replaces vague claims with numbers; D forces knowledge out of private chats into the wiki and guardrails.

## Decision log discipline

Every decision affecting standards/scope/ownership gets: ID, date, decision, options considered, rationale, owner, status (Proposed/Accepted/Superseded/Rejected), link. Decisions made in chat are copied into the log same-day, with the log link posted back to the chat.

## Rollout sequence

1. Space + pages published → 2. backlog loaded → 3. tooling connected (GitHub↔planning tool) → 4. announce at the governance forum with the space link → 5. recurring governance review scheduled → 6. only then admit execution items to sprints.

When asked to "set everything up", deliver in this order and say which step the user is on.
