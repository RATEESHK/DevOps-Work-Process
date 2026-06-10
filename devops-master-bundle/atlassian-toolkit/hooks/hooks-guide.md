# Hooks for Atlassian / governance work

Two kinds, per the on-demand-hooks pattern: session-scoped guardrails inside a skill, and project-level hooks in `.claude/settings.json`.

## 1. Project-level hooks (`.claude/settings.json`)

```json
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Bash",
        "hooks": [
          {
            "type": "command",
            "command": "python3 .claude/hooks/guard_destructive.py"
          }
        ]
      }
    ],
    "PostToolUse": [
      {
        "matcher": "Write|Edit",
        "hooks": [
          {
            "type": "command",
            "command": "python3 .claude/hooks/check_governance_files.py"
          }
        ]
      }
    ],
    "Stop": [
      {
        "hooks": [
          {
            "type": "command",
            "command": "python3 .claude/hooks/decision_log_reminder.py"
          }
        ]
      }
    ]
  }
}
```

## 2. The three hook scripts

### `guard_destructive.py` — block destructive Atlassian/git actions
Reads the tool input JSON from stdin; exits non-zero with a message if the command matches:
- `curl -X DELETE` against `*.atlassian.net` (space/page deletion via API)
- `git push --force` to protected branches
- bulk-delete JQL operations
Exit code 2 blocks the call and shows Claude the reason.

```python
import json, re, sys
data = json.load(sys.stdin)
cmd = data.get("tool_input", {}).get("command", "")
patterns = [
    r"curl[^|]*-X\s*DELETE[^|]*atlassian\.net",
    r"git\s+push\s+.*--force.*\b(main|master|release)\b",
    r"rm\s+-rf\s+/(?!tmp)",
]
for p in patterns:
    if re.search(p, cmd, re.I):
        print(f"BLOCKED by governance hook: matches '{p}'. Raise a work item instead.", file=sys.stderr)
        sys.exit(2)
sys.exit(0)
```

### `check_governance_files.py` — paste-safety lint after edits
After any Write/Edit to `*-page*.md` / files under a `devops-space/` or `pages/` folder, warn (exit 0, print to stderr) if the file contains:
- wiki markup tokens (`h1.`, `h2.`, `{code}`) when config says Cloud
- a title as the first line (page files must be body-only)
- tables wider than 8 columns (paste-mangling risk)

### `decision_log_reminder.py` — Stop hook
When a session ends, scan the transcript summary for decision-ish phrases ("we decided", "agreed to", "going with"). If found and no edit touched a decision-log file this session, print: "A decision may have been made this session — add it to the Decision Log before closing."

## 3. On-demand (skill-scoped) hook — `/careful-atlassian`

For risky sessions (production space cleanup, bulk imports), a slash-command skill can register the PreToolUse guard only for that session, so the guardrail doesn't run on everyday work. Put the same `guard_destructive.py` matcher in the skill's hook block; it activates when the skill is invoked and lasts the session.

## Why these three

- PreToolUse guard = irreversible-action insurance (deletes, force-pushes).
- PostToolUse lint = catches the #1 real failure (wrong markup for the edition) at write time, not paste time.
- Stop reminder = enforces the "no decision lives only in chat" rule mechanically, not by memory.
