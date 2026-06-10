# Atlassian Setup Agent — Confluence pages + Jira backlog, automated

Publishes the entire DevOps space (26 pages in 5 layers) to **Confluence Cloud** and the full backlog (5 epics, ~45 stories incl. the 22/05/2026 assessment remediation items) to **Jira Cloud**. Idempotent and safe: re-running updates pages in place and skips existing issues.

## Setup (10 minutes, once)

1. **Prereqs in the UI** (the API can't create these): create the Confluence space (key `DEVOPS`) and the Jira project (key `DEVGOV`, scrum).
2. **API token:** https://id.atlassian.com/manage-profile/security/api-tokens → Create token. One token works for both Jira and Confluence on the same site.
3. **Configure:**
   ```bash
   cp config.example.yaml config.yaml     # edit base URLs, email, keys
   export ATLASSIAN_API_TOKEN='your-token'   # env var only — never in the file
   pip install -r requirements.txt
   ```

## Run

```bash
python agent.py --dry-run     # ALWAYS first: prints every create/update, touches nothing
python agent.py --docs-only   # Confluence only
python agent.py --jira-only   # Jira only
python agent.py               # everything (~2 minutes)
```

Approval gate by design: dry-run is the change plan; the real run only does what dry-run showed.

## What it does / can't do

| Does automatically | Can't (Atlassian API limits) — do manually per BUILD-GUIDE |
|---|---|
| 5 layer parent pages + 26 content pages, correct hierarchy, labels | Folders (uses parent pages instead — same navigation effect) |
| Markdown → Confluence storage format conversion | Databases (Contacts, Decisions) — Part 3, ~10 min |
| Updates pages in place on re-run (version-safe) | Whiteboards — Part 4, ~10 min |
| 5 Epics + ~45 Stories with points, labels, descriptions, epic links | Smart-link Embed display mode (paste URLs in UI) |
| Skips issues that already exist (summary match) | Space permissions, cover images, status lozenges |

## Gotchas (read before your first real run)

1. **"Story Points" silently missing** → Jira custom field IDs vary per site. Find yours: `GET {base}/rest/api/3/field`, search "Story point", put the `customfield_XXXXX` id in `config.yaml`. Blank = points skipped, everything else still works.
2. **Company-managed vs team-managed project** → team-managed accepts `parent` for Story-under-Epic (default behavior). Company-managed older setups need `epic_link_field` (usually `customfield_10014`). Symptom of wrong choice: 400 error mentioning parent/epic.
3. **"Story" issuetype doesn't exist** → some project templates only have Task. Set `story_issuetype: Task`.
4. **403 on Confluence v2 API** → your token user needs space contributor permission; check Space settings → Permissions.
5. **Tables render oddly** → the markdown→storage conversion handles standard tables; exotic markdown (nested tables, raw HTML) may need a UI touch-up. The shipped content avoids these.
6. **Data Center instead of Cloud** → auth becomes a PAT (`Authorization: Bearer`), Jira search path differs, and `/api/v2/spaces` doesn't exist. This agent targets Cloud; say the word and it can be ported.
7. **Re-run after editing a page in the UI** → the agent will overwrite UI edits with file content (files are the source of truth, by design — that's the low-coupling model). Edit the `.md` files in `content/`, not the pages.

## Files

```
agent.py            orchestrator (--dry-run / --docs-only / --jira-only)
config.example.yaml site URLs + keys (copy to config.yaml)
manifest.yaml       file → page title → layer → labels
backlog.yaml        epics/stories incl. assessment findings F-01..F-13
content/*.md        the 26 page bodies (source of truth)
lib/confluence.py   md→storage conversion + idempotent upsert
lib/jira.py         idempotent issue creation (epic links, points)
```
