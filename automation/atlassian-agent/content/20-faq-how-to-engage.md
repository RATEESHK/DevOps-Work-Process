> Seeded FAQ — this page grows by rule: whenever a question is answered in the channel, the answer is added here and the link posted back. Type `/Table of Contents` after pasting.

## How do I raise DevOps work?
Create a work item in Azure Boards using the **DevOps Work Item Template** (page 07) and leave it in the backlog. Don't start work on it, and don't assign it to a sprint — it enters a sprint only after refinement passes the Definition of Ready. Full detail: **Intake & Planning Process** (page 02).

## Something urgent broke — do I still raise a ticket first?
For a **Sev-1** (production outage), page on-call and swarm immediately; the ticket is created in parallel, not as a precondition. For everything else, yes — item first. Severities and handling: **Bug, Spike & Timebox Policy** (page 14).

## I've been asked to do something that isn't in the sprint. What do I do?
Don't silently do it. If it's unknown/unplanned → create a **spike** (timeboxed question). If it belongs to another team/customer → create a **timeboxed dependency item**. If it's just new work → backlog, via the PO. The sprint is capacity-capped; unplanned work displaces planned work only by PO decision.

## Who do I contact for X?
The contact directory on **Roles, Goals & KPIs** (page 11, plus the addendum on page 19) lists the owner per area — business spec, architecture, pipelines, security, IAM, data, DB, network — with escalation paths. If the directory doesn't answer it, that's a gap: comment on page 11.

## Where do decisions live?
In the **Decision Log** (page 09) or on the work item — never only in a chat. If a decision happens in a chat, whoever made it copies it to the log the same day and posts the link back.

## How do I know what to work on today?
The board, ordered top-down within the sprint. Self-assign the next Amigos-passed item you can take. If you're blocked, flag the item and tag the unblocking owner — don't wait for standup.

## Why was my item bounced back a state?
Almost always missing evidence: PR link for In Review, test results for Done-ready, PO acceptance for Done. The per-state evidence table is on page 14 — attach and move it forward again. It's a workflow rule, never personal.

## How big should my story be?
1–5 points ideally; 8 means try to split; 13 means it's a Feature. Sizing scale, reference stories, and planning-poker rules: **Story Sizing** (page 12).

## Do I really have to write docs during the sprint?
Yes — in the same PR/item, not after. It's what makes releases fast and kills status calls. The split of who documents what: **Documentation & Evidence Standard** (page 16). If a doc update takes >15 minutes, the doc structure is wrong — raise an item.

## Can I decline a meeting?
If it has no agenda in the invite — yes, by team rule. Meeting rules and timeboxes: **Team Operating Model** (page 10).

## I want to learn/work on something outside my usual area. How?
Say so at retro (the "what do you want more of" question) or to your lead — work is routed by interest where possible, and stretch tasks are encouraged. Nothing is forced; small contributions are credited by name at sprint review.

## Where are the dashboards / Kibana / the pipelines?
All in the **link hub** on the Engineering Handbook (page 15).
