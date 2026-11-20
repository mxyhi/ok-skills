---
name: security-audit
description: Review source code and configuration for security defects. Use for a focused security question, a codebase security review, or triage of an existing finding. Produce source-backed findings, remediation, and a structured report when requested.
license: MIT
---

# Security audit

Start with the revision, files, and security question in scope. For a focused question, answer it directly. For a broader review, identify the protected resources, the principals allowed to access them, and where the application enforces those rules. Include the reviewed scope and any gaps in the report.

## Review the source

1. State the expected control in application terms, such as which tenant may update a record. Follow the ordinary code path through its caller, middleware, and data access layer. Check alternate entry points when they share the same protected operation.
2. Look for evidence against the suspected defect. Check wrappers, configuration, storage policies, and existing tests that could enforce the same rule. Cite repository-relative paths and line numbers from the reviewed revision. Use source inspection, checked-in tests, or existing redacted diagnostics as evidence.
3. Assign a verdict. Use `confirmed` when the available evidence establishes both the missing control and its effect. For `needs_validation`, name the missing fact and the artifact its owner can inspect, such as the effective deployment manifest. Use `rejected` when a control or an unreachable path disproves the claim.
4. For confirmed issues, identify the affected resource, preconditions, and impact. Recommend the smallest fix at the point that decides access, and specify the expected behavior of a regression test. Give severity only to confirmed findings and keep it within the demonstrated impact.

## Report findings

Lead with confirmed issues, ordered by impact. Keep open questions and scope gaps visible. If the review found no issues, state which components were reviewed. In ordinary conversation, return the result inline.

When a JSON report is requested, use the bundled [report schema](report-schema.json). It defines separate records for the three verdicts. Use a stable fingerprint for each issue, sort the array by fingerprint, and use an empty array when there are no records. Validate the file with Node.js, resolving the script path relative to this skill:

```sh
node "<skill-directory>/validate-findings.cjs" "<report-directory>/findings.json"
```

The findings schema is adapted for source review. A confirmed record uses source evidence, expected behavior, and remediation. To check an existing Cloudflare coverage ledger supplied with a review, run `node "<skill-directory>/validate-coverage-ledger.cjs" "<ledger-file>"`.
