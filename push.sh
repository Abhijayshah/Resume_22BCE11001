#!/bin/bash
cd /Users/abhijayhome/MEGA_2/VSCODE/PROJECT/Resume_22BCE11001
git config pull.rebase false
git add -A
git commit -m "Add Xebia data-ai role resume" || true
git pull origin main --no-edit
git push origin main -f
