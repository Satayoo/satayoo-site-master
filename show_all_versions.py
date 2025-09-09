import subprocess
import os

def run_cmd(cmd):
    try:
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
        return result.stdout, result.stderr, result.returncode
    except Exception as e:
        return "", str(e), 1

os.chdir(r"C:\Users\izzyh\OneDrive - Community College of Philadelphia\Documents\satayoo-site-master")

print("="*70)
print("ALL AVAILABLE VERSIONS IN YOUR REPOSITORY")
print("="*70)
print("\nShowing commit history with dates and descriptions:")
print("(Look for mentions of 'hero', 'video', 'fire', or the date August 8)\n")

# Get detailed commit history
stdout, stderr, code = run_cmd('git log --format="%h | %ad | %s" --date=short -50')

if stdout:
    lines = stdout.strip().split('\n')
    for i, line in enumerate(lines, 1):
        print(f"{i:2}. {line}")
        if i % 5 == 0:
            print()  # Add spacing every 5 commits
else:
    print("Error getting commit history")

print("\n" + "="*70)
print("TO RESTORE A DIFFERENT VERSION:")
print("="*70)
print("1. Note the commit hash (the 7-character code at the start)")
print("2. I can help you restore that specific version")
print("\nWhich version has the 'old fire' hero video layout you want?")
print("Look for commits that mention video, hero, or were from August 2024")
print("\n" + "="*70)

input("\nPress Enter to exit...")
