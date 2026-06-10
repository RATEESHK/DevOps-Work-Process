"""Confluence Cloud REST API client: idempotent page publishing from Markdown."""
import os, requests, markdown

class Confluence:
    def __init__(self, cfg):
        self.base = cfg["confluence"]["base_url"].rstrip("/")  # https://yoursite.atlassian.net/wiki
        self.space = cfg["confluence"]["space_key"]
        self.auth = (cfg["auth"]["email"], os.environ["ATLASSIAN_API_TOKEN"])
        self.s = requests.Session(); self.s.auth = self.auth
        self.s.headers.update({"Accept": "application/json", "Content-Type": "application/json"})

    def _get(self, path, **params):
        r = self.s.get(f"{self.base}/rest/api{path}", params=params); r.raise_for_status(); return r.json()

    def space_id(self):
        r = self.s.get(f"{self.base}/api/v2/spaces", params={"keys": self.space}); r.raise_for_status()
        results = r.json()["results"]
        if not results: raise SystemExit(f"Space {self.space} not found — create it in the UI first.")
        return results[0]["id"]

    def find_page(self, title):
        data = self._get("/content", spaceKey=self.space, title=title, expand="version")
        return data["results"][0] if data["results"] else None

    @staticmethod
    def md_to_storage(md_text):
        """Markdown -> XHTML acceptable as Confluence storage format.
        Tables/fenced code need the extensions; raw HTML passthrough kept off for safety."""
        html = markdown.markdown(md_text, extensions=["tables", "fenced_code", "sane_lists"])
        # Confluence storage chokes on bare <hr>/<br>; ensure self-closing
        return html.replace("<hr>", "<hr/>").replace("<br>", "<br/>")

    def upsert_page(self, title, md_body, parent_id=None, dry=False):
        body = self.md_to_storage(md_body)
        existing = self.find_page(title)
        if dry:
            action = "UPDATE" if existing else "CREATE"
            print(f"  [dry-run] {action}: {title}" + (f" (parent {parent_id})" if parent_id else ""))
            return existing["id"] if existing else f"dry-{title}"
        if existing:
            pid, ver = existing["id"], existing["version"]["number"] + 1
            payload = {"id": pid, "type": "page", "title": title, "version": {"number": ver},
                       "body": {"storage": {"value": body, "representation": "storage"}}}
            r = self.s.put(f"{self.base}/rest/api/content/{pid}", json=payload)
        else:
            payload = {"type": "page", "title": title, "space": {"key": self.space},
                       "body": {"storage": {"value": body, "representation": "storage"}}}
            if parent_id: payload["ancestors"] = [{"id": str(parent_id)}]
            r = self.s.post(f"{self.base}/rest/api/content", json=payload)
        if r.status_code >= 400:
            raise SystemExit(f"Confluence error on '{title}': {r.status_code} {r.text[:300]}")
        pid = r.json()["id"]; print(f"  ok: {title} (id {pid})"); return pid

    def add_label(self, page_id, label, dry=False):
        if dry: return
        self.s.post(f"{self.base}/rest/api/content/{page_id}/label", json=[{"prefix": "global", "name": label}])
