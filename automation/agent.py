#!/usr/bin/env python3
"""Atlassian setup agent: publishes the DevOps space to Confluence and the backlog to Jira.

Usage:
  export ATLASSIAN_API_TOKEN=...           # from id.atlassian.com/manage-profile/security/api-tokens
  python agent.py --dry-run                # ALWAYS first: shows every action, changes nothing
  python agent.py --docs-only              # Confluence pages only
  python agent.py --jira-only              # Jira backlog only
  python agent.py                          # everything
Idempotent: re-running updates pages in place and skips Jira issues that already exist (matched by summary).
"""
import argparse, sys, yaml
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
from lib.confluence import Confluence
from lib.jira import Jira

HERE = Path(__file__).parent

def load(name): return yaml.safe_load((HERE / name).read_text())

def publish_docs(cfg, dry):
    c = Confluence(cfg)
    manifest = load("manifest.yaml")
    print(f"\n== Confluence: space {c.space} ==")
    c.space_id()  # fail fast if space missing
    parents = {}
    for section in manifest["sections"]:            # layer parent pages (folders aren't API-creatable)
        pid = c.upsert_page(section["title"], section.get("intro", f"# {section['title']}\nPages in this layer are listed below."), dry=dry)
        parents[section["key"]] = pid
    for page in manifest["pages"]:
        md = (HERE / "content" / page["file"]).read_text()
        pid = c.upsert_page(page["title"], md, parent_id=parents.get(page["section"]), dry=dry)
        for lbl in page.get("labels", ["devops"]):
            c.add_label(pid, lbl, dry=dry)
    print("Confluence done." if not dry else "Confluence dry-run done.")
    print("NOTE (API limits): folders, databases, and whiteboards cannot be created via REST — "
          "the agent uses parent pages for layers; create the 2 databases and 2 whiteboards "
          "manually per BUILD-GUIDE Parts 3–4 (≈20 min).")

def publish_jira(cfg, dry):
    j = Jira(cfg)
    backlog = load("backlog.yaml")
    print(f"\n== Jira: project {j.project} ==")
    for epic in backlog["epics"]:
        ekey = j.create("Epic", epic["summary"], epic.get("description", ""), labels=epic.get("labels"), dry=dry)
        for story in epic.get("stories", []):
            j.create(cfg["jira"].get("story_issuetype", "Story"), story["summary"],
                     story.get("description", ""), parent_key=ekey,
                     points=story.get("points"), labels=story.get("labels"), dry=dry)
    print("Jira done." if not dry else "Jira dry-run done.")

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--docs-only", action="store_true")
    ap.add_argument("--jira-only", action="store_true")
    a = ap.parse_args()
    cfg = load("config.yaml")
    import os
    if not a.dry_run and "ATLASSIAN_API_TOKEN" not in os.environ:
        sys.exit("Set ATLASSIAN_API_TOKEN env var (never put the token in config.yaml).")
    if a.dry_run and "ATLASSIAN_API_TOKEN" not in os.environ:
        os.environ["ATLASSIAN_API_TOKEN"] = "dry"
    if not a.jira_only: publish_docs(cfg, a.dry_run)
    if not a.docs_only: publish_jira(cfg, a.dry_run)
