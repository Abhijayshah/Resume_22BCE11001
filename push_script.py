import subprocess
import os

os.chdir('/Users/abhijayhome/MEGA_2/VSCODE/PROJECT/Resume_22BCE11001')

try:
    # Try to abort merge if in progress
    subprocess.run(['git', 'merge', '--abort'], capture_output=True)
except:
    pass

# Add all changes
subprocess.run(['git', 'add', '-A'], capture_output=True)

# Get git status
result = subprocess.run(['git', 'status', '--porcelain'], capture_output=True, text=True)
print("Git Status:")
print(result.stdout)

# If there are changes, commit them
if result.stdout.strip():
    subprocess.run(['git', 'config', 'user.email', 'abhijay@xample.com'], capture_output=True)
    subprocess.run(['git', 'config', 'user.name', 'Abhijay'], capture_output=True)
    commit_result = subprocess.run(['git', 'commit', '-m', 'Update resume files'], capture_output=True, text=True)
    print("Commit Output:")
    print(commit_result.stdout)
    print(commit_result.stderr)

# Configure pull strategy
subprocess.run(['git', 'config', 'pull.rebase', 'false'], capture_output=True)

# Pull latest from remote
pull_result = subprocess.run(['git', 'pull', 'origin', 'main'], capture_output=True, text=True)
print("Pull Output:")
print(pull_result.stdout)
print(pull_result.stderr)

# Push to remote
push_result = subprocess.run(['git', 'push', 'origin', 'main'], capture_output=True, text=True)
print("Push Output:")
print(push_result.stdout)
print(push_result.stderr)

# Final status
final_status = subprocess.run(['git', 'status'], capture_output=True, text=True)
print("Final Status:")
print(final_status.stdout)
