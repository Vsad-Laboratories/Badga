import random
import subprocess
import time
from datetime import datetime

# Real-looking developer commit messages
COMMIT_MESSAGES = [
    "feat: update landing page layout and styling",
    "fix: resolve null pointer exception in auth handler",
    "docs: update API endpoints documentation in README",
    "chore: update dependencies and patch security vulnerabilities",
    "refactor: clean up redundant conditional logic in utility functions",
    "style: fix linting issues and missing semicolons",
    "test: add unit tests for user profile registration flow",
    "fix: adjust responsive behavior on mobile viewports",
    "feat: implement dark mode toggle state persistence",
    "chore: optimize asset compression settings for build pipeline"
]

def run_git_command(command):
    subprocess.run(command, shell=True, check=True)

def main():
    current_hour = datetime.now().hour
    
    # Human sleep simulation: Skip or drastically reduce activity between 12 AM and 7 AM
    if 0 <= current_hour <= 7:
        # 90% chance to sleep completely during these hours
        if random.random() > 0.1:
            print("Skipping commit to simulate human sleep cycle.")
            return

    # Target: 30 to 120 commits per day. 
    # Spread across 16 active hours, that averages 2 to 7 commits per hour.
    commit_count = random.randint(2, 7)
    print(f"Generating {commit_count} human-style commits for this hour...")

    for i in range(commit_count):
        # 1. Modify the file
        with open("history.log", "a") as f:
            f.write(f"Update verified at {datetime.now().isoformat()}\n")
        
        # 2. Pick a random message
        msg = random.choice(COMMIT_MESSAGES)
        
        # 3. Commit locally
        run_git_command("git add history.log")
        run_git_command(f'git commit -m "{msg}"')
        
        # 4. Tiny random pause between micro-commits to look natural
        if i < commit_count - 1:
            time.sleep(random.randint(1, 5))

    # 5. Push all accumulated commits at once
    run_git_command("git push")

if __name__ == "__main__":
    main()
