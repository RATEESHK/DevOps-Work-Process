# Traceability (work item ↔ code)

## Link syntax by stack (read config.json)

| Planning tool | Code host | Link token | Where |
|---|---|---|---|
| Jira | GitHub/Bitbucket | `PROJ-123` | branch name, commit message, PR title |
| Azure Boards | GitHub | `AB#123` | commit message, PR title/description; branch created from the work item |
| Azure Boards | Azure Repos | `#123` | commit message |

Jira+GitHub needs the **GitHub for Jira** app installed; Azure Boards+GitHub needs the connection under Project settings → GitHub connections. Mention the prerequisite — the syntax silently does nothing without it.

## Conventions

Branch: `<type>/<KEY>-<short-desc>` where type ∈ feature|fix|chore|spike|docs.
Commit: `<type>: <imperative summary> (<KEY>)`.
PR must include: link token, what/why, compliance impact checklist, evidence links (pipeline run, scans).

## Evidence bar (audit-grade)

From the work item alone, a reviewer must reach: the branch, the PR with approvals and passing checks, the merge commit, and any updated standard — without chat history. If any hop is missing, that's a traceability gap; surface it as a backlog item, not a comment.
