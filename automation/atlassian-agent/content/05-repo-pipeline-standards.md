> Type `/Table of Contents` here after pasting.

These are the baseline standards for repositories and pipelines. They are the boundary every change is reviewed against. Treat them as the minimum; individual repos may add stricter rules.

## 1. Branch policy baseline

- Protected default branch (`main`); no direct pushes.
- Changes land via pull request only.
- Required: passing status checks + at least the minimum number of approving reviews (see PR control).
- Linear history preferred (squash or rebase merge); delete branch on merge.
- Branch names follow the convention in *GitHub / Work Item Traceability*.

## 2. PR control baseline

- Minimum **2 reviewers** on all repos (assessment finding: 1-reviewer minimum on the API repo does not meet enterprise-grade standards).
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
- integration points and process flow (e.g. Tink / Payments context);
- links to the relevant Confluence standards.

## 4. Secret handling and `.gitignore`

- No secrets, keys, certificates, or credentials committed to source control.
- Secrets are retrieved at runtime from the approved central vault; rotate per policy.
- A standardised `.gitignore` baseline excludes secrets, local config, build artefacts, and credential/certificate files (for example `*.pem`, `*.per`, `*.pfx`, `*.key`, `.env`), **validated in CI: the build fails if excluded file patterns are detected in commits** (existence of .gitignore alone is not evidence — the assessment flagged exactly this gap).
- Secret-scanning enabled; any historical exposure is rotated and remediated.

## 5. Dependency management

- Remediation SLA by severity: **Critical/High within 7 days; Moderate within 14 days** (per the 22/05/2026 CI/CD assessment recommendation).
- Automated dependency and vulnerability scanning in CI, with **Dependabot (or enterprise equivalent) enabled** to auto-raise PRs for vulnerable dependencies.
- Vulnerability gates in the pipeline that block merges/deploys breaching the policy threshold.
- A documented owner for triaging and tracking remediation items.

## 6. Pipeline lifecycle governance

- Every pipeline has a named owner and a documented purpose.
- Pipelines follow the policy-as-code / static-analysis gates defined for the org.
- Low-usage or duplicate pipelines are reviewed for rationalisation on a **quarterly cadence**, with named pipeline ownership and lifecycle (creation → usage → retirement).
- Changes to shared pipeline templates go through PR review like code.
- **Quality gates are mandatory**: linting blocks merge on failure; code-quality gate (Sonar or equivalent) enforced.
- **Shift-left**: pre-commit hooks for linting, secret detection, and dependency checks; a standardised "golden pipeline" template (security scans, branch protections, quality checks, audit logging) is the default for all Tink/ICS repos.
- **Audit visibility**: dashboards for vulnerability trends, repository hygiene, and PR compliance, aligned to regulatory expectations.

## 7. Retirement and clean-up criteria

- **Stale branches:** auto-delete merged branches; branches inactive beyond **30–60 days** are flagged and removed after owner confirmation.
- **Unused pipelines:** pipelines below a usage threshold (or with no runs in a defined period) are candidates for retirement.
- **Archival:** repositories no longer in use are archived (read-only) rather than left active.
- All retirements are tracked as work items so the action is auditable.