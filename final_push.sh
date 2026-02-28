#!/bin/bash
cd /Users/abhijayhome/MEGA_2/VSCODE/PROJECT/Resume_22BCE11001

# Check status
echo "=== Git Status ==="
git status

# Reset merge state if needed
if [ -f .git/MERGE_HEAD ]; then
    echo "Aborting merge..."
    git merge --abort 2>/dev/null || true
fi

# Add all changes
echo ""
echo "=== Adding Changes ==="
git add -A

# Check what's staged
echo ""
echo "=== Staged Changes ==="
git status --short

# Configure user if needed
git config user.email "abhijay@example.com" >/dev/null 2>&1
git config user.name "Abhijay" >/dev/null 2>&1

# Commit if there are changes
echo ""
echo "=== Committing ==="
git diff-index --quiet HEAD -- || git commit -m "Update resume files"

# Pull latest
echo ""
echo "=== Pulling Latest ==="
git config pull.rebase false
git pull origin main --no-edit 2>&1 || true

# Push
echo ""
echo "=== Pushing ==="
git push origin main

# Final status
echo ""
echo "=== Final Status ==="
git status
