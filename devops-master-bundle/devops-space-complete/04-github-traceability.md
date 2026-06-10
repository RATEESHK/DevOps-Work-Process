> Type `/Table of Contents` here after pasting.

Where DevOps work results in repository or pipeline changes, the work must be traceable from planning intent (Azure Boards) through to code (GitHub). This improves visibility, auditability, and alignment between planning and delivery, and speeds up root-cause analysis.

## 1. Linking model (Azure Boards ↔ GitHub)

Azure Boards connects to GitHub so that commits, pull requests, branches, and issues can be linked to work items. The link is created by mentioning the work-item ID using the `AB#<ID>` syntax.

- **Commit message:** include `AB#1234` to link the commit to work item 1234.
- **Pull request title or description:** include `AB#1234` to link the PR.
- **Branch:** create the branch from the work item (or name it with the ID) so the branch is associated with the item.

> Prerequisite: an admin connects the GitHub org/repos under **Project settings → GitHub connections** in Azure DevOps.

## 2. Branch naming convention

```
<type>/AB-<workitemID>-<short-description>
```

Examples:

- `feature/AB-1234-eks-ingress-policy`
- `fix/AB-1290-rotate-static-credentials`
- `chore/AB-1305-cleanup-stale-branches`

Where `<type>` is one of: `feature`, `fix`, `chore`, `spike`, `docs`.

## 3. Commit message guidance

```
<type>: <imperative summary>  (AB#<ID>)

<optional body: what changed and why>
```

Example: `fix: block unencrypted port 80 routing in CI (AB#1290)`

## 4. PR requirements

Every pull request must:

- reference the work item with `AB#<ID>` in the title or description;
- use the PR template (below);
- meet the branch-protection / review rules in *Repository & Pipeline Governance Standards*;
- show passing compliance / security checks before merge.

### PR description template

```
## Linked work item
AB#____

## What changed
-

## Why
-

## Compliance / security impact
- [ ] No new public load balancers / open ingress
- [ ] Secrets handled via the approved vault (no static credentials)
- [ ] Policy / static-analysis checks passing

## Evidence
- (links to pipeline run, scan results, screenshots)
```

## 5. Evidence expectations for audit / governance

- The work item links to the branch, PR, and merge commit.
- The PR shows the compliance/security check results.
- Any standard or runbook affected by the change is updated and linked.
- For regulated changes, the audit trail is sufficient to reconstruct *what changed, who approved it, and why* without reference to personal chats.

> Note: the same traceability principle applies if any team uses Jira instead of Azure Boards — reference the issue key in branches, commits, and PRs. Be aware that permissions and some workflow transitions are handled separately in that toolchain.