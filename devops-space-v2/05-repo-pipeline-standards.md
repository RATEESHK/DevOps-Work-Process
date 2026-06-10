> Type `/Table of Contents` here after pasting.

These are the baseline standards for repositories and pipelines. They are the boundary every change is reviewed against. Treat them as the minimum; individual repos may add stricter rules.

## 1. Branch policy baseline

- Protected default branch (`main`); no direct pushes.
- Changes land via pull request only.
- Required: passing status checks + at least the minimum number of approving reviews (see PR control).
- Linear history preferred (squash or rebase merge); delete branch on merge.
- Branch names follow the convention in *GitHub / Work Item Traceability*.

## 2. PR control baseline

- Minimum reviewers defined per repo (default: 1; raise to 2 for production-impacting repos).
- Code owners auto-requested where a `CODEOWNERS` file exists.
- No self-approval for production-impacting changes.
- Compliance / security checks must pass before merge.
- PR references the work item (`AB#<ID>`) and uses the PR template.

## 3. README / documentation baseline

Every repository has a `README.md` covering:

- purpose of the repository / service;
- owning team and contacts;
- how to build, test, and run locally;
- pipeline overview and environments;
- how to contribute (branching, PR, review expectations);
- links to the relevant Confluence standards.

## 4. Secret handling and `.gitignore`

- No secrets, keys, certificates, or credentials committed to source control.
- Secrets are retrieved at runtime from the approved central vault; rotate per policy.
- A standardised `.gitignore` baseline excludes secrets, local config, build artefacts, and credential/certificate files (for example `*.pem`, `*.pfx`, `*.key`, `.env`).
- Secret-scanning enabled; any historical exposure is rotated and remediated.

## 5. Dependency management

- A defined remediation SLA by severity (for example: critical within X days, high within Y days).
- Automated dependency and vulnerability scanning in CI.
- Vulnerability gates in the pipeline that block merges/deploys breaching the policy threshold.
- A documented owner for triaging and tracking remediation items.

## 6. Pipeline lifecycle governance

- Every pipeline has a named owner and a documented purpose.
- Pipelines follow the policy-as-code / static-analysis gates defined for the org.
- Low-usage or duplicate pipelines are reviewed for rationalisation.
- Changes to shared pipeline templates go through PR review like code.

## 7. Retirement and clean-up criteria

- **Stale branches:** branches with no activity beyond a defined window are flagged and removed after owner confirmation.
- **Unused pipelines:** pipelines below a usage threshold (or with no runs in a defined period) are candidates for retirement.
- **Archival:** repositories no longer in use are archived (read-only) rather than left active.
- All retirements are tracked as work items so the action is auditable.