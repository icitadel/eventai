#!/bin/bash
# Export Beads issues to GitHub Issues
# Usage: ./export-to-github.sh

set -e

REPO="icitadel/eventai"
JSONL_FILE=".beads/issues.jsonl"

if [ ! -f "$JSONL_FILE" ]; then
    echo "Error: $JSONL_FILE not found"
    exit 1
fi

# Check if gh is installed
if ! command -v gh &> /dev/null; then
    echo "Error: GitHub CLI (gh) is not installed"
    echo "Install with: brew install gh"
    exit 1
fi

# Check if authenticated
if ! gh auth status &> /dev/null; then
    echo "Error: Not authenticated with GitHub"
    echo "Run: gh auth login"
    exit 1
fi

echo "Exporting Beads issues to GitHub..."
echo "Repository: $REPO"
echo ""

# Create a mapping file to track beads ID -> GitHub issue number
MAPPING_FILE=".beads/github-mapping.json"
if [ ! -f "$MAPPING_FILE" ]; then
    echo "{}" > "$MAPPING_FILE"
fi

# Process each issue
count=0
while IFS= read -r line; do
    # Parse JSON fields
    id=$(echo "$line" | jq -r '.id')
    title=$(echo "$line" | jq -r '.title')
    description=$(echo "$line" | jq -r '.description')
    status=$(echo "$line" | jq -r '.status')
    priority=$(echo "$line" | jq -r '.priority')
    issue_type=$(echo "$line" | jq -r '.issue_type')
    created_at=$(echo "$line" | jq -r '.created_at')
    
    # Check if already exported
    existing=$(jq -r --arg id "$id" '.[$id]' "$MAPPING_FILE")
    if [ "$existing" != "null" ]; then
        echo "⏭️  Skipping $id (already exported as #$existing)"
        continue
    fi
    
    # Build the issue body
    body="**Beads ID:** \`$id\`
**Type:** $issue_type
**Priority:** P$priority
**Status:** $status
**Created:** $created_at

---

$description"
    
    # Create GitHub issue (without labels to avoid label errors)
    echo "📝 Creating: $id - $title"
    
    gh_issue_url=$(gh issue create \
        --repo "$REPO" \
        --title "[$id] $title" \
        --body "$body" \
        2>&1)
    
    # Extract issue number from URL
    issue_num=$(echo "$gh_issue_url" | grep -oE '[0-9]+$' || echo "")
    
    if [ -n "$issue_num" ]; then
        # Save mapping
        jq --arg id "$id" --arg num "$issue_num" '.[$id] = $num' "$MAPPING_FILE" > "$MAPPING_FILE.tmp"
        mv "$MAPPING_FILE.tmp" "$MAPPING_FILE"
        echo "   ✅ Created GitHub issue #$issue_num"
        
        # Close if needed
        if [ "$status" = "closed" ]; then
            gh issue close "$issue_num" --repo "$REPO" --reason completed
            echo "   🔒 Closed issue #$issue_num"
        fi
    else
        echo "   ❌ Failed to create issue"
    fi
    
    ((count++))
    
    # Rate limiting - be nice to GitHub API
    sleep 1
    
done < "$JSONL_FILE"

echo ""
echo "✅ Exported $count issues to GitHub"
echo "📋 Mapping saved to $MAPPING_FILE"
