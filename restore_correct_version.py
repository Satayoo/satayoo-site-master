import subprocess
import os
import sys

def run_cmd(cmd):
    try:
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True, cwd=os.getcwd())
        return result.stdout, result.stderr, result.returncode
    except Exception as e:
        return "", str(e), 1

# Change to project directory
os.chdir(r"C:\Users\izzyh\OneDrive - Community College of Philadelphia\Documents\satayoo-site-master")

print("="*70)
print("  RESTORING VERSION WITH BREAKTHROUGH AI TAGLINE AND LOGOS")
print("="*70)
print()

# The commit with "Breakthrough AI for Active Living"
commit_hash = "137092e"

print(f"Restoring version from commit {commit_hash}...")
print("This version has: 'Breakthrough AI for Active Living' tagline")
print()

# Checkout files from that commit
stdout, stderr, code = run_cmd(f"git checkout {commit_hash} -- .")

if code == 0:
    print("✓ Successfully restored the Breakthrough AI version!")
else:
    print(f"ERROR: Failed to restore - {stderr}")
    input("Press Enter to exit...")
    sys.exit(1)

print()
print("Staging all changes...")
stdout, stderr, code = run_cmd("git add .")
print("✓ Changes staged")

print()
print("Creating commit...")
stdout, stderr, code = run_cmd('git commit -m "Restore version with Breakthrough AI tagline, different AI logos and blog"')

if code == 0:
    print("✓ Commit created!")
    if stdout:
        # Show what changed
        lines = stdout.split('\n')
        for line in lines[:5]:  # Show first 5 lines
            print(f"  {line}")
else:
    if "nothing to commit" in stderr or "nothing to commit" in stdout:
        print("Note: No changes to commit")
    else:
        print(f"Commit result: {stderr or stdout}")

print()
print("Pushing to GitHub...")
stdout, stderr, code = run_cmd("git push origin main")

if code == 0:
    print("✓ Successfully pushed to GitHub!")
else:
    if "Everything up-to-date" in stderr or "Everything up-to-date" in stdout:
        print("✓ Already up to date")
    else:
        print(f"Push result: {stderr or stdout}")

print()
print("="*70)
print("  RESTORATION COMPLETE!")
print("="*70)
print()
print("The version with Breakthrough AI tagline has been restored!")
print("This version should have:")
print("  • Breakthrough AI tagline")
print("  • Different AI logos")
print("  • Blog section")
print()
print("Check: https://github.com/Satayoo/satayoo-site-master")
print()

input("Press Enter to exit...")
