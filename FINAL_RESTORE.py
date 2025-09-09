#!/usr/bin/env python3
import subprocess
import os
import sys

def run_git(cmd):
    """Run git command and return success status"""
    try:
        result = subprocess.run(f"git {cmd}", shell=True, capture_output=True, text=True)
        return result.returncode == 0, result.stdout, result.stderr
    except Exception as e:
        return False, "", str(e)

os.chdir(r"C:\Users\izzyh\OneDrive - Community College of Philadelphia\Documents\satayoo-site-master")

print("="*70)
print("FINAL RESTORATION - BREAKTHROUGH AI VERSION")
print("="*70)
print()
print("This will restore the version with:")
print("  • Breakthrough AI for Active Living tagline")
print("  • Different AI logos")
print("  • Zeta-focused content")
print()

# First, let's check what we currently have
print("Current status...")
success, out, err = run_git("status --short")
if out:
    print("You have uncommitted changes. Committing them first...")
    run_git("add .")
    run_git('commit -m "Save current state before restoration"')

print()
print("Step 1: Restoring commit 137092e (Breakthrough AI version)...")

# Restore the specific commit
success, out, err = run_git("checkout 137092e -- .")

if not success:
    print(f"ERROR: {err}")
    print("\nTrying alternative approach...")
    # Try resetting to that commit
    success, out, err = run_git("reset --hard 137092e")
    if not success:
        print("Failed to restore. Please close any programs using git files and try again.")
        input("Press Enter to exit...")
        sys.exit(1)

print("✓ Files restored successfully!")

print()
print("Step 2: Committing the restoration...")
run_git("add .")
success, out, err = run_git('commit -m "Restore Breakthrough AI version with Zeta focus, AI logos, and blog"')

if success:
    print("✓ Commit created!")
elif "nothing to commit" in out or "nothing to commit" in err:
    print("Already at this version!")
else:
    print(f"Commit status: {out or err}")

print()
print("Step 3: Pushing to GitHub...")
success, out, err = run_git("push origin main --force-with-lease")

if success:
    print("✓ Pushed to GitHub successfully!")
elif "Everything up-to-date" in err:
    print("✓ Already up to date on GitHub")
else:
    # Try regular push
    success2, out2, err2 = run_git("push origin main")
    if success2:
        print("✓ Pushed to GitHub!")
    else:
        print(f"Push status: {err2 or err}")

print()
print("="*70)
print("✅ RESTORATION COMPLETE!")
print("="*70)
print()
print("The 'Breakthrough AI for Active Living' version has been restored!")
print("This version should now have:")
print("  • Breakthrough AI tagline")
print("  • Zeta-focused content")  
print("  • Different AI logos")
print("  • Blog section")
print()
print("Check it at: https://github.com/Satayoo/satayoo-site-master")
print()

input("Press Enter to exit...")
