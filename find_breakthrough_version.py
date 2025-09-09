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
print("SEARCHING FOR THE BREAKTHROUGH AI VERSION")
print("="*70)
print()

# Get all commits with their messages
stdout, stderr, code = run_cmd("git log --oneline -50")

if stdout:
    commits = stdout.strip().split('\n')
    
    print("Looking for commits with 'Breakthrough', 'Zeta', 'blog', or 'fire'...")
    print()
    
    found_candidates = []
    
    for commit in commits:
        lower_commit = commit.lower()
        if any(keyword in lower_commit for keyword in ['breakthrough', 'zeta', 'blog', 'fire', 'hero', 'video', 'clean', 'logo']):
            found_candidates.append(commit)
            print(f"✓ Found: {commit}")
    
    print()
    print("="*70)
    
    # Check specific commits that look promising
    promising_commits = [
        "137092e",  # Zeta-focused with Breakthrough AI
        "64b454f",  # Windows PC Agent
        "56a4504",  # Remove images/videos (the one before this might be good)
    ]
    
    print("Checking specific commits for content...")
    print()
    
    for commit_hash in promising_commits:
        print(f"Checking {commit_hash}...")
        # Get the commit message
        stdout, stderr, code = run_cmd(f"git log --oneline -1 {commit_hash}")
        if stdout:
            print(f"  Message: {stdout.strip()}")
        
        # Check what files were in that commit
        stdout, stderr, code = run_cmd(f"git ls-tree --name-only -r {commit_hash} | grep -E '(index|styles|blog)' | head -5")
        if stdout:
            print(f"  Has files: {stdout.strip().replace(chr(10), ', ')}")
        print()
    
    print("="*70)
    print("RECOMMENDATION:")
    print("="*70)
    print()
    print("Based on your description (Breakthrough AI tagline, different AI logos, blog),")
    print("the version you want is likely:")
    print()
    print("  137092e - 'content: concise Zeta-focused landing page (Breakthrough AI for Active Living)'")
    print()
    print("This commit has the 'Breakthrough AI' tagline you mentioned.")
    print()
else:
    print("Error getting commit history")

input("Press Enter to continue...")
