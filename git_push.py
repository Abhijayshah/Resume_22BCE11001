#!/usr/bin/env python3
import subprocess
import sys
import os

os.chdir('/Users/abhijayhome/MEGA_2/VSCODE/PROJECT/Resume_22BCE11001')

def run_cmd(cmd, description=""):
    """Run a shell command and return result"""
    if description:
        print(f"\n{'='*50}")
        print(f"{description}")
        print('='*50)
    
    print(f"$ {' '.join(cmd)}")
    result = subprocess.run(cmd, capture_output=True, text=True)
    
    if result.stdout:
        print(result.stdout)
    if result.stderr and result.returncode != 0:
        print(f"Error: {result.stderr}", file=sys.stderr)
    
    return result

# Check if merge in progress
if os.path.exists('.git/MERGE_HEAD'):
    run_cmd(['git', 'merge', '--abort'], "Aborting pending merge...")

# Add all changes
run_cmd(['git', 'add', '-A'], "Adding all changes...")

# Check status
run_cmd(['git', 'status', '--short'], "Staged changes:")

# Configure user
subprocess.run(['git', 'config', 'user.email', 'abhijay@example.com'], capture_output=True)
subprocess.run(['git', 'config', 'user.name', 'Abhijay'], capture_output=True)

# Check if there are changes to commit
result = subprocess.run(['git', 'diff-index', '--quiet', 'HEAD', '--'], capture_output=True)
if result.returncode != 0:  # There are changes
    run_cmd(['git', 'commit', '-m', 'Update resume files'], "Committing changes...")
else:
    print("\nNo changes to commit")

# Configure pull strategy
subprocess.run(['git', 'config', 'pull.rebase', 'false'], capture_output=True)

# Verify remote
run_cmd(['git', 'remote', '-v'], "Checking remote configuration...")

# Pull latest
run_cmd(['git', 'pull', 'origin', 'main', '--no-edit'], "Pulling latest from remote...")

# Push
run_cmd(['git', 'push', 'origin', 'main'], "Pushing to remote...")

# Final status
run_cmd(['git', 'status'], "Final status:")

print("\n✅ Push complete!")
