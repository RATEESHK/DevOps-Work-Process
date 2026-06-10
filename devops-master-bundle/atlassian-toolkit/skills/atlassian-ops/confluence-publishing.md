# Confluence Publishing

How to get content into Confluence cleanly, per edition.

## Decide the content type first

- **Page** — standards, charters, runbooks: anything stable and referenced. Default choice.
- **Live doc** (Cloud) — collaborative drafting, meeting notes; no Publish step, edits visible in real time. Convert to a page once finalised (More actions → Convert). Footer comments hide while it's a live doc.
- **Blog post** — announcements only.
- **Whiteboard / database** — brainstorms / structured records; don't put standards in them.

## Paste paths by edition

**Cloud (new editor):**
- Paste Markdown as plain text (`Ctrl/Cmd+Shift+V`) into the body → auto-converts headings, bold, lists, simple tables. One-way: after paste it's rich text.
- Wiki markup (`h1.`, `*bold*`) does NOT work in the new editor. Don't offer it.
- If a table/code block mangles: render the Markdown in a previewer, copy the rendered output, paste that.
- Bulk/automated: REST API with `representation: storage` (storage-format XHTML) or `atlas_doc_format` (ADF JSON). Use API when >10 pages.

**Data Center / Server:**
- Insert → Markup → choose Markdown or Confluence wiki. Wiki markup (`h1.`) works here.
- If the user has `h1.`-style source, it pastes directly — no conversion needed.

## Space build sequence

1. Create space (meaningful key, e.g. `DEVGOV`).
2. Home page first; child pages in reading order.
3. Per page: title → paste body → verify render → labels → publish.
4. Home page: `/Children Display` macro. Long pages: `/Table of Contents` at top.
5. Permissions: team view+comment; restrict edit on standards pages to owners.
6. Register reusable templates: Space settings → Content tools → Templates.

## Macros worth using (type `/` + name)

Table of Contents · Children Display · Info/Note/Warning panels · Status lozenge · Decision · Action item · Expand · Include Page (single-source shared content) · Jira (embed live issues/JQL — use this instead of pasting static ticket lists).

## Structure rules

- One concern per page; link rather than duplicate.
- Page titles are globally searchable — make them specific ("DevOps Definition of Ready", not "DoR").
- Keep trees ≤3 levels deep; beyond that, split into another space.
- Every page gets ≥2 labels: one space-wide (`devops`), one topic-specific.
