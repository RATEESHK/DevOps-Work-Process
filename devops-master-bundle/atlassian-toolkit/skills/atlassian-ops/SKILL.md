---
name: atlassian-ops
description: >
  Set up and operate Atlassian products end-to-end: Confluence spaces/pages/live docs,
  Jira projects/boards/backlogs, JSM, Bitbucket, and traceability to GitHub or Azure Boards.
  Produces paste-ready page bodies, import-ready backlogs, runbooks, and governance artifacts.
  Trigger whenever the user mentions Confluence, Jira, JSM, Atlassian, wiki pages, spaces,
  page trees, "paste into Confluence", sprint/backlog setup, DevOps charter or governance docs,
  Definition of Ready, decision logs, S.C.A.L.E.D., or linking work items to branches/PRs —
  even if they don't say "Atlassian". Also trigger for "document this in the wiki" or
  "create a ticket/epic/story" requests.
version: 1.0.0
user-invocable: true
---

# Atlassian Ops

Hub skill. Read the spoke file that matches the task — don't load everything.

## First run — check config

```bash
cat "$(dirname "$0")/config.json" 2>/dev/null || echo "NOT_CONFIGURED"
```

If `NOT_CONFIGURED`, ask the user for: Confluence edition (Cloud/Data Center), planning tool (Jira or Azure Boards), code host (GitHub/Bitbucket), space key, project key, and link syntax (`PROJ-123` or `AB#123`). Write answers to `config.json` in this directory and proceed. Don't re-ask on later runs.

## Dispatch table

| Task looks like... | Read |
|---|---|
| Create/structure a Confluence space, paste content into pages, live docs vs pages, templates, macros | `confluence-publishing.md` |
| Create a Jira project, backlog hierarchy, sprints, boards, JQL, CSV import; Azure Boards equivalents | `jira-projects.md` |
| Charter, standards, DoR/DoD, decision logs, intake process, S.C.A.L.E.D. comms, rollout sequencing | `governance-rollout.md` |
| Branch/commit/PR conventions, work-item linking, audit evidence | `traceability.md` |
| Anything failing or behaving oddly | `gotchas.md` (check this FIRST when something breaks) |
| Need a ready template (work item, PR, decision log, page skeletons) | `templates/` |

## Non-negotiables (apply to every task)

- **Convert, don't invent.** When the user supplies content, preserve it verbatim; only change structure/format. Mark gaps you fill with `ASSUMPTION:`.
- **Files, not descriptions.** Output one paste-ready file per Confluence page, import-ready CSV for Jira, numbered runbooks for humans.
- **Governance before execution.** Planning artifacts ship first; technical items stay in backlog until Definition of Ready is met.
- **Edition awareness.** Cloud and Data Center have different paste/markup behavior — check config.json before choosing output format (details in `confluence-publishing.md`).
- **No chat-only decisions.** Anything decided during the session that affects standards gets a decision-log entry in the output.
