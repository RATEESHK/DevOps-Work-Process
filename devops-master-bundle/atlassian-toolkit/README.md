# Atlassian Toolkit — prompt, skill, agents, hooks, instructions

Everything needed to make Claude a first-class Atlassian operator for your team.

```
atlassian-toolkit/
├── CLAUDE.md                      ← project instructions (repo root)
├── prompts/
│   └── atlassian-master-prompt.md ← reusable fill-in prompt (chat / Code / Cowork)
├── skills/atlassian-ops/          ← hub-and-spoke Claude Code skill
│   ├── SKILL.md                   ← hub: dispatch table + config-on-first-run
│   ├── confluence-publishing.md   ← paste paths per edition, macros, space build
│   ├── jira-projects.md           ← hierarchy mapping, CSV import, JQL, JSM
│   ├── governance-rollout.md      ← page tree, DoR/DoD, S.C.A.L.E.D., rollout order
│   ├── traceability.md            ← link syntax per stack, conventions, evidence bar
│   ├── gotchas.md                 ← failure modes; check FIRST when things break
│   └── templates/                 ← work-item, PR, decision-log skeletons
├── agents/                        ← three custom agents (plan → build → audit)
└── hooks/hooks-guide.md           ← settings.json + 3 hook scripts + /careful pattern
```

## Install (Claude Code)

```bash
# Skill (per-user)
mkdir -p ~/.claude/skills && cp -r skills/atlassian-ops ~/.claude/skills/
# Or per-repo: cp -r skills/atlassian-ops .claude/skills/

# Agents
mkdir -p ~/.claude/agents && cp agents/*.md ~/.claude/agents/

# Instructions
cp CLAUDE.md /path/to/your/repo/CLAUDE.md   # then fill the {{...}} stack facts

# Hooks: follow hooks/hooks-guide.md (settings.json + scripts in .claude/hooks/)
```

First skill use will ask for your stack (Confluence edition, planning tool, code host, keys) and save it to `config.json` — answer once.

## The intended workflow

1. **Plan** — paste `prompts/atlassian-master-prompt.md` filled in, in PLAN mode, or invoke the `atlassian-architect` agent. Review the design.
2. **Build** — switch to BUILD mode / `content-publisher` agent → page files + backlog CSV + runbook.
3. **Audit** — `governance-auditor` agent before announcing → findings become backlog items.
4. **Operate** — the skill handles day-to-day asks ("add a standards page", "import these stories", "why won't this paste").
5. **Improve** — every failure becomes a line in `gotchas.md`; every correction becomes a line in CLAUDE.md. Never fix the same thing twice by prompting.

## Design notes (why it's shaped this way)

- **Hub-and-spoke + progressive disclosure**: SKILL.md stays small; Claude reads only the spoke that matches the task.
- **Description = trigger condition**: the skill triggers on Confluence/Jira/wiki/backlog/charter phrasing even when "Atlassian" isn't said.
- **Gotchas as the growth point**: the highest-signal file; append on every failure.
- **No railroading**: spokes give constraints and facts, not step-scripts, so Claude adapts to your instance.
- **Plan/build/audit agent split**: separate contexts kill self-preferential bias — the auditor doesn't trust the publisher.
- **Hooks enforce mechanically** what prompts enforce only probabilistically: no destructive API calls, no wrong-edition markup, no chat-only decisions.

## Iterating the skill

In Claude Code, run a few real tasks, note misses, then: "update the atlassian-ops skill: it did X wrong, add to gotchas" — or use the skill-creator skill to run trigger-rate evals on the description.
