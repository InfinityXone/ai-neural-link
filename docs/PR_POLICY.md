# PR policy (automated)

- All PRs run CI (`ci` workflow).
- PRs from Dependabot are auto-approved and auto-merged on green.
- Any PR labeled `automerge` is auto-merged on green.
- Branch is deleted after merge.

**Recommended (manual once):** Enable branch protection on `main` (require status check `ci`).
