# GitHub Sub-Issues: API Usage Notes

[Collected 2026-03-07] [AI Provider: Anthropic, Claude Opus 4.6]

## Overview

GitHub introduced sub-issues (parent/child issue relationships) in 2024-2025. This allows hierarchical task decomposition directly in GitHub Issues without requiring GitHub Projects.

## GraphQL API

### Getting an Issue's Node ID

```bash
gh api graphql -f query='{ repository(owner:"OWNER", name:"REPO") { issue(number:N) { id } } }' --jq '.data.repository.issue.id'
```

Returns a global node ID like `I_kwDOQ_ZEIc7wwl04`.

### Adding a Sub-Issue

```graphql
mutation {
  addSubIssue(input: {
    issueId: "PARENT_NODE_ID",
    subIssueId: "CHILD_NODE_ID"
  }) {
    issue { id }
    subIssue { number title }
  }
}
```

CLI equivalent:

```bash
gh api graphql -f query='mutation { addSubIssue(input: {issueId: "PARENT_ID", subIssueId: "CHILD_ID"}) { issue { id } subIssue { number title } } }'
```

### Removing a Sub-Issue

```graphql
mutation {
  removeSubIssue(input: {
    issueId: "PARENT_NODE_ID",
    subIssueId: "CHILD_NODE_ID"
  }) {
    issue { id }
    subIssue { number title }
  }
}
```

## REST API (alternative to GraphQL)

```bash
# Get numeric resource ID (NOT the issue number, NOT the GraphQL node_id)
CHILD_ID=$(gh api repos/OWNER/REPO/issues/CHILD_NUMBER --jq '.id')

# Link child as sub-issue
gh api repos/OWNER/REPO/issues/PARENT_NUMBER/sub_issues -X POST -F sub_issue_id="$CHILD_ID"

# List sub-issues
gh api repos/OWNER/REPO/issues/PARENT_NUMBER/sub_issues

# Remove sub-issue
gh api repos/OWNER/REPO/issues/PARENT_NUMBER/sub_issues -X DELETE -F sub_issue_id="$CHILD_ID"
```

## Querying Sub-Issue Progress (GraphQL)

```graphql
{
  repository(owner: "OWNER", name: "REPO") {
    issue(number: 42) {
      parent { number title }
      subIssues(first: 100) { nodes { number title state } }
      subIssuesSummary { total completed percentCompleted }
    }
  }
}
```

## Constraints

| Constraint | Value |
|---|---|
| Max sub-issues per parent | 100 |
| Max nesting depth | 8 levels |
| Parent uniqueness | Exactly 1 parent per issue |
| Cross-org | Not supported (same org only) |
| Cross-repo | Supported within same org |
| Minimum permission | Triage role |

## Key Points

* No GitHub Projects required — works directly on Issues
* Sub-issues appear in the parent issue's body in the GitHub WebUI
* Each sub-issue can still have its own labels, assignees, milestones
* Cross-repo within same org; NOT cross-org
* The `addSubIssue` mutation requires both parent and child to be Issues (not PRs)
* A sub-issue can only have one parent
* Use `replaceParent: true` in addSubIssue input to reparent an issue that already has a parent

## Workflow Used in This Repo

For issue #1 (Multi-denomination portfolio valuation), we created 5 sub-issues (#2-#6) covering:

1. Core research paper (#2)
2. Debiasing framework document (#3)
3. Cross-reference updates (#4)
4. Python implementation example (#5)
5. Literature review research artifact (#6)

Each was created via `gh issue create` and then linked via the `addSubIssue` GraphQL mutation.
