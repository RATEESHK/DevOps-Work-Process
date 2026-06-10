> Two templates in one page: the recurring CoP / governance forum agenda, and the launch announcement to send when the space goes live. Register the agenda block as a Confluence template (Space settings → Content tools → Templates) so each session creates a notes page from it.

## CoP / Governance Forum — recurring agenda (45 min, every 2 weeks)

```
Date:            YYYY-MM-DD     Facilitator:            Notetaker:
Attendees:       (required: DevOps Lead, Backlog Owner, PO, Tech Lead; open to all)

1. Decisions since last session (5 min)
   — walk new Decision Log entries; confirm none live only in chat

2. Backlog health (10 min)
   — Not-Ready query count, Ready pipeline depth, Blocked items + owners

3. Standards & exceptions (10 min)
   — proposed standard changes; security exceptions nearing expiry

4. KPI / OKR glance (5 min)
   — anything red on the dashboard; overtime occurrences since last session

5. Escalations & cross-team dependencies (10 min)
   — items stuck >1 sprint on external parties

6. AOB → backlog (5 min)
   — every concern raised becomes an item before the meeting ends

Outputs (write before leaving the room):
- Decisions → Decision Log (IDs: ____)
- New items created (IDs: ____)
- Actions with owners (item IDs: ____)
```

Rules: agenda published with the invite; questions brought written; hard stop at 45 minutes — anything unresolved becomes an item, the meeting never extends.

## Launch announcement (post to the team channel / CoP)

```
📣 DevOps Governance Space is live

What: our single source of truth for how DevOps work is raised, planned,
sized, delivered, and measured — charter, intake, standards, ceremonies,
roles & contacts, sizing, bug/spike rules, Kibana/logging standard,
KPIs/OKRs, and the implementation plan.

Where: {{space link}}
Board: {{board link}} — the governance backlog is already loaded (Sprint 0 + 1).

What changes for you, starting now:
• All work enters via a backlog item (template in the space) — no chat-only asks.
• Decisions get logged same-day in the Decision Log — chats are never the record.
• Stories pass Three Amigos before development; evidence attaches per state.
• Meetings need an agenda; focus blocks are protected; no overtime by design.

Start here (10 min read): space home → Charter → Team Operating Model.
Questions → FAQ page first, then the team channel (answers get added to the FAQ).

First CoP forum: {{date}} — agenda is in the invite. The charter is agreed
there and recorded as decision D-001.
```

## Starter Decision Log entries (paste into page 09 once agreed at the first CoP)

| ID | Date | Decision | Status |
|---|---|---|---|
| D-001 | {{CoP date}} | Adopt the DevOps Charter (page 01) as the team operating authority | Proposed → Accepted at CoP |
| D-002 | {{CoP date}} | Hierarchy: Epic → Feature → Story → Task in Azure Boards; Spike = tagged Task | Proposed |
| D-003 | {{CoP date}} | Confluence = knowledge, Azure Boards = planning, GitHub = code; decisions logged same-day | Proposed |
| D-004 | {{CoP date}} | Sprint 0 contains planning work only; execution items require DoR + Amigos-passed | Proposed |
| D-005 | {{CoP date}} | Fibonacci sizing per page 12; sprint capacity capped at ~70–75% | Proposed |
