#!/bin/bash
# Auto Create and Push Script for TextbookBiasDetection

set -e

echo "=========================================="
echo "Creating GitHub Repository"
echo "=========================================="

# Create repository
gh repo create dl1413/TextbookBiasDetection \
  --public \
  --description "Detecting Publisher Bias in Academic Textbooks Using Bayesian Ensemble Methods and LLMs" \
  --confirm

if [ $? -eq 0 ]; then
    echo "✓ Repository created successfully"

    echo ""
    echo "=========================================="
    echo "Pushing Code"
    echo "=========================================="

    # Push to repository
    git push -u origin main

    if [ $? -eq 0 ]; then
        echo ""
        echo "=========================================="
        echo "✅ SUCCESS!"
        echo "=========================================="
        echo "Repository: https://github.com/dl1413/TextbookBiasDetection"
        echo ""
        echo "Your project is now live!"
    else
        echo "❌ Push failed"
        exit 1
    fi
else
    echo "❌ Repository creation failed"
    echo "Creating repository manually at: https://github.com/new"
    exit 1
fi
