"""Jira Cloud REST v3 client: idempotent Epic/Story creation from backlog.yaml."""
import os, requests, json

class Jira:
    def __init__(self, cfg):
        self.base = cfg["jira"]["base_url"].rstrip("/")          # https://yoursite.atlassian.net
        self.project = cfg["jira"]["project_key"]
        self.points_field = cfg["jira"].get("story_points_field", "")   # e.g. customfield_10016; blank = skip
        self.epic_link_field = cfg["jira"].get("epic_link_field", "")   # company-managed only; team-managed uses parent
        self.auth = (cfg["auth"]["email"], os.environ["ATLASSIAN_API_TOKEN"])
        self.s = requests.Session(); self.s.auth = self.auth
        self.s.headers.update({"Accept": "application/json", "Content-Type": "application/json"})

    def search_by_summary(self, summary, issuetype):
        jql = f'project = {self.project} AND issuetype = "{issuetype}" AND summary ~ "\\"{summary}\\"" ORDER BY created'
        r = self.s.get(f"{self.base}/rest/api/3/search/jql", params={"jql": jql, "fields": "summary", "maxResults": 5})
        if r.status_code == 404:  # older deployments
            r = self.s.get(f"{self.base}/rest/api/3/search", params={"jql": jql, "fields": "summary", "maxResults": 5})
        r.raise_for_status()
        for it in r.json().get("issues", []):
            if it["fields"]["summary"].strip().lower() == summary.strip().lower():
                return it["key"]
        return None

    @staticmethod
    def adf(text):
        return {"type": "doc", "version": 1, "content": [
            {"type": "paragraph", "content": [{"type": "text", "text": text or " "}]}]}

    def create(self, issuetype, summary, description="", parent_key=None, points=None, labels=None, dry=False):
        existing = self.search_by_summary(summary, issuetype)
        if existing:
            print(f"  skip (exists): [{existing}] {summary}"); return existing
        if dry:
            print(f"  [dry-run] CREATE {issuetype}: {summary}" + (f" (parent {parent_key})" if parent_key else ""))
            return f"DRY-{summary[:20]}"
        fields = {"project": {"key": self.project}, "issuetype": {"name": issuetype},
                  "summary": summary, "description": self.adf(description)}
        if labels: fields["labels"] = labels
        if parent_key:
            if self.epic_link_field:                 # company-managed
                fields[self.epic_link_field] = parent_key
            else:                                    # team-managed: parent works for Story under Epic
                fields["parent"] = {"key": parent_key}
        if points and self.points_field:
            fields[self.points_field] = points
        r = self.s.post(f"{self.base}/rest/api/3/issue", json={"fields": fields})
        if r.status_code >= 400:
            raise SystemExit(f"Jira error on '{summary}': {r.status_code} {r.text[:400]}\n"
                             "Hints: wrong issuetype name? points/epic-link field id wrong? See README gotchas.")
        key = r.json()["key"]; print(f"  ok: [{key}] {summary}"); return key
