> Type `/Table of Contents` here after pasting.

This page defines how we size stories so sprints are predictable and nobody is overloaded. Points measure relative effort + complexity + uncertainty — not hours. The day-mapping below is for planning approximation only; never use it to judge individuals.

## 1. The scale (Fibonacci)

| Points | Meaning | Approx. effort (one person, focused) | Example |
|---|---|---|---|
| 1 | Trivial, fully understood | ≤ half a day | Config value change with test |
| 2 | Small, clear | ~1 day | Add a field through one layer + tests |
| 3 | Standard story | 1.5–2 days | New endpoint with validation, tests, docs |
| 5 | Larger, some unknowns | 3–4 days | New component touching 2 systems |
| 8 | Big, notable uncertainty | ~5–7 days — **split it if possible** | Cross-service feature with migration |
| 13 | Too big for one sprint story | — | Must be split or become a Feature |
| ☕ Spike | Unknown | Timeboxed (see Bug & Spike Policy) | Investigation |

## 2. Sizing rules

1. Size at refinement using planning poker (whole team estimates simultaneously; discuss only when estimates diverge by ≥2 steps; re-vote once; if still split, take the higher).
2. Compare against **reference stories** (keep 1 example per size linked here once the first sprint completes) — relative sizing beats absolute guessing.
3. A story includes dev + tests + documentation + evidence. If testing is "someone else's story", the sizing is wrong.
4. Anything ≥8 gets a split attempt first (by user path, by layer, by happy-path-vs-edge-cases).
5. Unknowns are not padded into estimates — they become a spike *before* the story is sized.
6. Bugs found in-sprint for in-sprint work aren't pointed (they're unfinished work). Escaped bugs from production are pointed like stories.

## 3. Capacity and commitment

- Sprint length: **2 weeks (10 working days)**.
- Per-person plannable capacity: ~6 focused hours/day × 10 days, minus ceremonies (~1 day) and a 15–20% buffer for reviews, support, and the unexpected → plan to roughly **70–75% of theoretical capacity**.
- Team velocity is discovered, not declared: commit conservatively for sprints 1–2 (e.g. a 6-person delivery team typically lands somewhere near 30–45 points), then use the rolling average of the last 3 sprints.
- The sprint is full when capacity is reached — items beyond that stay in backlog regardless of pressure. Quality and no-overtime are protected by this rule.

## 4. Definition of a well-sized story

Independent, Negotiable, Valuable, Estimable, Small (≤5 ideally), Testable (INVEST) — plus our DoR fields and, for technical stories, the S.C.A.L.E.D. block. If a story can't be demoed or evidenced, it isn't a story.
