#!/bin/bash
# Quick Push Script for TextbookBiasDetection
# Usage: ./push_to_github.sh <username> <repo-name>

# Check if username provided
if [ -z "$1" ]; then
    echo "❌ Error: GitHub username required"
    echo "Usage: ./push_to_github.sh <username> [repo-name]"
    echo "Example: ./push_to_github.sh yourusername TextbookBiasDetection"
    exit 1
fi

USERNAME=$1
REPO_NAME=${2:-TextbookBiasDetection}

echo "=========================================="
echo "📦 Pushing TextbookBiasDetection"
echo "=========================================="
echo "Target: https://github.com/$USERNAME/$REPO_NAME"
echo ""

# Check if remote already exists
if git remote get-url origin &> /dev/null; then
    echo "⚠️  Remote 'origin' already exists"
    echo "Current remote:"
    git remote -v
    echo ""
    read -p "Remove existing remote and continue? (y/n) " -n 1 -r
    echo
    if [[ $REPLY =~ ^[Yy]$ ]]; then
        git remote remove origin
        echo "✓ Removed existing remote"
    else
        echo "❌ Aborted"
        exit 1
    fi
fi

# Add remote
echo "📡 Adding remote..."
git remote add origin "https://github.com/$USERNAME/$REPO_NAME.git"

# Check current branch
CURRENT_BRANCH=$(git branch --show-current)
echo "Current branch: $CURRENT_BRANCH"

# Optionally rename to main
if [ "$CURRENT_BRANCH" = "master" ]; then
    read -p "Rename 'master' to 'main'? (y/n) " -n 1 -r
    echo
    if [[ $REPLY =~ ^[Yy]$ ]]; then
        git branch -M main
        CURRENT_BRANCH="main"
        echo "✓ Renamed to 'main'"
    fi
fi

# Show status
echo ""
echo "📊 Current status:"
git log --oneline -3
echo ""
echo "📁 Files to push:"
git ls-files | head -10
echo "... (and more)"
echo ""

# Push
echo "🚀 Pushing to GitHub..."
echo "Command: git push -u origin $CURRENT_BRANCH"
echo ""
read -p "Proceed with push? (y/n) " -n 1 -r
echo
if [[ $REPLY =~ ^[Yy]$ ]]; then
    git push -u origin "$CURRENT_BRANCH"

    if [ $? -eq 0 ]; then
        echo ""
        echo "=========================================="
        echo "✅ Successfully pushed to GitHub!"
        echo "=========================================="
        echo "View at: https://github.com/$USERNAME/$REPO_NAME"
        echo ""
        echo "Next steps:"
        echo "1. Visit your repository"
        echo "2. Add description and topics"
        echo "3. Enable GitHub Pages (optional)"
        echo "4. Set up branch protection (optional)"
    else
        echo ""
        echo "=========================================="
        echo "❌ Push failed!"
        echo "=========================================="
        echo "Common issues:"
        echo "1. Repository doesn't exist - create it first on GitHub"
        echo "2. Authentication failed - check credentials"
        echo "3. No permission - verify repository access"
        echo ""
        echo "See PUSH_INSTRUCTIONS.md for detailed help"
    fi
else
    echo "❌ Push cancelled"
    exit 1
fi
