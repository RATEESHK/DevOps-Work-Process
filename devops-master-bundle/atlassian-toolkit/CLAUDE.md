# CLAUDE.md — Atlassian / DevOps governance project

<!-- Drop this into the repo root (or merge into an existing CLAUDE.md).
     Per Boris: anytime Claude does something wrong here, add a line — don't re-prompt. -->

## What this project is
Governance-first DevOps operating model: Confluence holds standards, {{Jira | Azure Boards}} holds planning, {{GitHub | Bitbucket}} holds code. We are in governance-setup phase: planning artifacts ship first; technical remediation stays in backlog until Definition of Ready is met.

## Stack facts (keep current)
- Confluence edition: {{Cloud | Data Center}} → page bodies are written as Markdown; never use `h1.` wiki markup for Cloud.
- Planning tool: {{Azure Boards}} → hierarchy Epic → Feature → Story → Task; link syntax `AB#<id>`.
- Code host: {{GitHub}} → branch `type/AB-<id>-desc`; commit `type: summary (AB#id)`.
- Source-of-truth folder for page content: `devops-space/*.md` (body-only files; the `.md` files are the editable master — Confluence paste is one-way).

## Rules
- Convert, don't invent: when source content exists, change format only; mark gap-fills `ASSUMPTION:`.
- Page files contain body only — no title line, numbered prefix = tree order.
- Backlog changes go through the import CSV / hierarchy table, never described in prose only.
- Any decision made in-session → append a row to the decision log file and say so.
- No execution items in Sprint 0, even if asked; park them in backlog and say why.
- Use the `atlassian-ops` skill for anything touching Confluence/Jira; check its `gotchas.md` first when something fails, and append new gotchas there after fixing.

## Agents
- `atlassian-architect` — design before build (plans only).
- `content-publisher` — generates page files, CSVs, runbooks from an approved plan.
- `governance-auditor` — adversarial review of artifacts and traceability; run before announcing anything.

## Definition of done for any task here
Artifacts produced as files, paste/import-tested constructs only, runbook updated if setup steps changed, decision log current.
