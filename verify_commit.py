import subprocess
import os

os.chdir(r"C:\Users\izzyh\OneDrive - Community College of Philadelphia\Documents\satayoo-site-master")

print("="*70)
print("VERIFYING GIT STATUS AND COMMITS")
print("="*70)
print()

# Check git status
result = subprocess.run("git status --porcelain", shell=True, capture_output=True, text=True)
if result.stdout:
    print("⚠️ UNCOMMITTED CHANGES FOUND:")
    print(result.stdout)
    print()
    print("Committing now...")
    subprocess.run("git add -A", shell=True)
    result = subprocess.run('git commit -m "Ensure Breakthrough AI version is committed"', shell=True, capture_output=True, text=True)
    if result.returncode == 0:
        print("✓ Changes committed!")
    else:
        print("Note:", result.stdout or result.stderr)
else:
    print("✓ No uncommitted changes - working tree clean")

print()
print("Current commit:")
result = subprocess.run("git log --oneline -1", shell=True, capture_output=True, text=True)
print(result.stdout.strip())

print()
print("Checking what's in index.html:")
with open("index.html", "r", encoding="utf-8") as f:
    content = f.read()
    if "Breakthrough AI" in content and "Introducing Zeta" in content:
        print("✓ index.html has the Breakthrough AI version!")
    else:
        print("⚠️ index.html doesn't have the Breakthrough AI version")
        print("First 500 chars:", content[:500])

print()
print("Pushing to ensure GitHub is updated...")
result = subprocess.run("git push origin main", shell=True, capture_output=True, text=True)
if "Everything up-to-date" in result.stderr:
    print("✓ Already up to date on GitHub")
elif result.returncode == 0:
    print("✓ Pushed to GitHub successfully!")
else:
    print("Push result:", result.stderr or result.stdout)

print()
print("="*70)
print("VERIFICATION COMPLETE")
print("="*70)
print()
print("Check your GitHub: https://github.com/Satayoo/satayoo-site-master")
print()
input("Press Enter to exit...")
