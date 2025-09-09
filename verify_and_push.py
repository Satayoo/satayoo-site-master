import subprocess
import os

def run_cmd(cmd):
    try:
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
        return result.stdout, result.stderr, result.returncode
    except Exception as e:
        return "", str(e), 1

os.chdir(r"C:\Users\izzyh\OneDrive - Community College of Philadelphia\Documents\satayoo-site-master")

print("Checking current git status...")
stdout, stderr, code = run_cmd("git status --porcelain")

if stdout:
    print("There are uncommitted changes. Let's commit them...")
    
    # Add all changes
    run_cmd("git add .")
    
    # Commit
    stdout, stderr, code = run_cmd('git commit -m "Restore old fire version with hero video and logo clean layout from Professional AGENTIC Izzy platform design"')
    
    if code == 0:
        print("✓ Commit created successfully!")
    else:
        print(f"Commit status: {stderr or stdout}")
else:
    print("No uncommitted changes found.")

print("\nPushing to GitHub...")
stdout, stderr, code = run_cmd("git push origin main")

if code == 0:
    print("✓ Successfully pushed to GitHub!")
    print("\nYour website has been restored!")
    print("Check: https://github.com/Satayoo/satayoo-site-master")
else:
    if "Everything up-to-date" in stderr or "Everything up-to-date" in stdout:
        print("✓ Already up to date on GitHub")
    else:
        print(f"Push result: {stderr or stdout}")

print("\nDONE! The old fire version with AGENTIC Izzy has been restored.")
input("\nPress Enter to exit...")
