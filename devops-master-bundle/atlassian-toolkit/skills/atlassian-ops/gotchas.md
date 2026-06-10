# Gotchas

> Check this file FIRST when something fails. Add a line every time a new failure is hit — this file is the skill's most valuable asset.

## Confluence

- **Wiki markup (`h1.`) pasted into Cloud new editor renders as literal text.** Cloud = Markdown paste only; wiki markup = Data Center / legacy editor.
- **Markdown paste is one-way.** After paste it's rich text; keep the `.md` source files as the editable master.
- **Complex Markdown tables sometimes paste as code blocks.** Fallback: copy the *rendered* preview from a Markdown viewer and paste that.
- **Smart-quote contamination:** pasting via Word/Outlook converts `"` to curly quotes and breaks code snippets. Route through plain-text paste (`Ctrl/Cmd+Shift+V`).
- **`/Table of Contents` shows nothing until the page has real headings** — paste body first, add the macro after.
- **Live docs hide footer comments**; they return when converted back to a page. Warn before converting a commented page.
- **Page titles are unique per space.** A "template" page and a registered template can't share a title cleanly — name the page "Work Item Template (reference)".

## Jira / Azure Boards

- **CSV import creates Epics and children in one pass only if the Epic rows precede children** and the parent column matches exactly; otherwise two passes.
- **"Feature" doesn't exist in standard Jira.** Map Feature→Epic and original Epic→label/component; tell the user about the mapping.
- **Spike is not a built-in type** in either tool — use a Task with a `spike` label.
- **`AB#123` / `PROJ-123` links do nothing until the integration app/connection is installed.** Always state the prerequisite.
- **JQL custom field names vary per instance** (`"Story Points"` vs `"Story point estimate"`). Give the query and say which field name to verify.
- **Azure Boards hierarchy order is fixed** — you can hide levels or add portfolio levels, but not reorder.

## Process

- **Don't put execution items into Sprint 0** even if the user lists them — restate the governance-first rule and park them in the backlog.
- **Don't regenerate content the user already wrote.** Diff-level changes only; full rewrites destroy their review history.
