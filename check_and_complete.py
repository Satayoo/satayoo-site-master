import subprocess
import os
import sys

def run_cmd(cmd):
    try:
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
        return result.stdout, result.stderr, result.returncode
    except Exception as e:
        return "", str(e), 1

os.chdir(r"C:\Users\izzyh\OneDrive - Community College of Philadelphia\Documents\satayoo-site-master")

print("="*70)
print("CHECKING RESTORATION STATUS")
print("="*70)
print()

# Check git status
stdout, stderr, code = run_cmd("git status --porcelain")
if stdout:
    print("Found uncommitted changes. Completing restoration...")
    print()
    
    # Show what changed
    changed_files = stdout.strip().split('\n')[:10]  # Show first 10 files
    print("Changed files:")
    for f in changed_files:
        print(f"  {f}")
    if len(stdout.strip().split('\n')) > 10:
        print(f"  ... and {len(stdout.strip().split('\n')) - 10} more files")
    print()
    
    # Commit changes
    print("Committing changes...")
    run_cmd("git add .")
    stdout, stderr, code = run_cmd('git commit -m "Complete restoration of Breakthrough AI version with Zeta focus"')
    if code == 0:
        print("✓ Commit created!")
    else:
        print(f"Commit status: {stderr or stdout}")
    
    # Push to GitHub
    print()
    print("Pushing to GitHub...")
    stdout, stderr, code = run_cmd("git push origin main")
    if code == 0:
        print("✓ Pushed successfully!")
    else:
        print(f"Push status: {stderr or stdout}")
else:
    print("No uncommitted changes found.")
    print()
    
    # Check current version
    print("Checking current version...")
    stdout, stderr, code = run_cmd("git log --oneline -1")
    if stdout:
        print(f"Current commit: {stdout.strip()}")
    
    # Check if we're at the right commit
    if "137092e" in stdout or "Breakthrough" in stdout or "Zeta" in stdout:
        print("✓ Already at the Breakthrough AI version!")
    else:
        print()
        print("Not at the Breakthrough AI version yet. Restoring now...")
        print()
        
        # Do the restoration
        print("Restoring commit 137092e...")
        stdout, stderr, code = run_cmd("git checkout 137092e -- .")
        if code == 0:
            print("✓ Files restored!")
            
            # Stage and commit
            run_cmd("git add .")
            stdout, stderr, code = run_cmd('git commit -m "Restore Breakthrough AI version with Zeta focus, AI logos, and blog"')
            if code == 0:
                print("✓ Commit created!")
                
                # Push
                stdout, stderr, code = run_cmd("git push origin main")
                if code == 0:
                    print("✓ Pushed to GitHub!")
                else:
                    print(f"Push result: {stderr or stdout}")
            else:
                print(f"Commit result: {stderr or stdout}")
        else:
            print(f"Restore failed: {stderr}")

print()
print("="*70)
print("FINAL STATUS")
print("="*70)

# Show final commit
stdout, stderr, code = run_cmd("git log --oneline -1")
if stdout:
    print(f"Current version: {stdout.strip()}")

print()
print("Check your site at: https://github.com/Satayoo/satayoo-site-master")
print()

input("Press Enter to exit...")
