> Type `/Table of Contents` here after pasting. Replace every {{link}} placeholder with your real URLs — this page is the team's map.

This is the shared technical reference: what each platform term means for us, the developer and tester pseudo-code patterns, the logging/observability standard (Kibana), and the link hub.

## 1. Platform definitions (our working meanings)

- **DevOps** — the practice of shipping through automated, governed pipelines: CI/CD, infrastructure as code, traceable changes. Owns the paved road from commit to production.
- **DevSecOps** — security embedded in that pipeline as code: SAST/DAST, dependency and secret scanning, policy-as-code gates (e.g. OPA/Checkov), remediation SLAs by severity.
- **SRE** — operating services against SLOs with error budgets; observability, incident response, blameless postmortems, toil reduction through automation.
- **On-premises** — servers in our own/bank data centres; change-controlled, network-segmented, hardware lifecycle managed by Infra/Network engineering.
- **Cloud** — provider-hosted (e.g. AWS) elastic infrastructure, provisioned only via IaC; no console changes.
- **Hybrid cloud** — workloads spanning on-prem and cloud with secure connectivity (private links/VPN), unified identity (IAM), and consistent policy on both sides. Our payment workloads are hybrid: data-resident components on-prem, elastic compute in cloud regions.
- **Platform engineering** — the internal developer platform: golden-path templates, shared modules (IAM role mapping, Vault integration), self-service with guardrails.

## 2. Developer pseudo-code pattern (per story)

Written/confirmed at Three Amigos; lives in the story before *In Progress*:

```
FUNCTION handle<StoryCapability>(request):
    validate input against business rules        # rules numbered in the spec
    IF invalid: RETURN structured error + log(WARN, rule_id)
    authorize via central IAM module             # never inline auth
    perform core action (idempotent where possible)
    persist / call downstream WITH retry + circuit breaker
    emit structured log (INFO, correlation_id, outcome)
    emit metric (counter/duration)
    RETURN response matching contract

TESTS REQUIRED: each Given/When/Then example from Three Amigos
DOCS REQUIRED:  update endpoint/contract page in the same PR
```

## 3. Tester pseudo-code pattern (per story)

```
FOR each example (Given/When/Then) from Three Amigos:
    arrange test data per Given
    execute via API/UI per When
    assert outcome per Then + side effects (DB, events, logs)
ADD: 1 negative auth test, 1 boundary test, 1 idempotency/retry test
AUTOMATE: happy path + top edge case into the regression suite
ATTACH: run results to the work item (state gate to Done-ready)
```

## 4. Logging & observability standard (Kibana / ELK)

- **Structured JSON logs only**: timestamp, level, service, environment, `correlation_id`, work-item-deployable version, message, and rule/error codes. No PII or secrets in logs — DevSecOps gate scans for patterns.
- Every request carries a **correlation ID** end-to-end (generated at the edge, propagated in headers) so one Kibana query reconstructs a transaction across services.
- **Levels**: ERROR = needs action, WARN = degraded/rule rejection, INFO = business event, DEBUG = off in production.
- **Kibana usage**: saved searches per service ({{link}}), dashboards per SLO ({{link}}), and the bug template requires the Kibana query link as evidence.
- Metrics + traces accompany logs (the three pillars); SRE owns the dashboards, everyone can read them.

## 5. Link hub (replace placeholders)

| What | Link |
|---|---|
| This Confluence space home | {{link}} |
| Azure Boards / Jira board | {{link}} |
| GitHub org / key repos | {{link}} |
| CI/CD pipelines | {{link}} |
| Kibana | {{link}} |
| Dashboards (SLO / sprint) | {{link}} |
| Vault / secrets process | {{link}} |
| Architecture diagrams / ADRs | {{link}} |
| On-call rota & incident process | {{link}} |
| Environments (dev/stage/prod endpoints) | {{link}} |
| Access requests (IAM) | {{link}} |
