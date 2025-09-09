import subprocess
import os
import sys

def run_git_command(cmd, cwd):
    """Run a git command and return the result"""
    try:
        result = subprocess.run(
            cmd,
            shell=True,
            cwd=cwd,
            capture_output=True,
            text=True
        )
        return result.returncode == 0, result.stdout, result.stderr
    except Exception as e:
        return False, "", str(e)

def main():
    # Set the working directory
    project_dir = r"C:\Users\izzyh\OneDrive - Community College of Philadelphia\Documents\satayoo-site-master"
    os.chdir(project_dir)
    
    print("="*50)
    print("  RESTORING OLD FIRE VERSION WITH HERO VIDEO")
    print("="*50)
    print()
    
    # Step 1: Create backup branch
    print("Step 1: Creating backup branch...")
    success, stdout, stderr = run_git_command("git branch backup-dec2024", project_dir)
    if success:
        print("✓ Backup branch created")
    elif "already exists" in stderr:
        print("✓ Backup branch already exists")
    else:
        print(f"Note: {stderr}")
    print()
    
    # Step 2: Restore files from old commit
    print("Step 2: Restoring files from the old version (fa68f18)...")
    print("This is the 'Complete website redesign - Professional AGENTIC Izzy platform' version")
    success, stdout, stderr = run_git_command("git checkout fa68f18 -- .", project_dir)
    if success:
        print("✓ Successfully restored files!")
    else:
        print(f"ERROR: Failed to restore files - {stderr}")
        input("Press Enter to exit...")
        sys.exit(1)
    print()
    
    # Step 3: Stage all changes
    print("Step 3: Staging all changes...")
    success, stdout, stderr = run_git_command("git add .", project_dir)
    if success:
        print("✓ Changes staged")
    else:
        print(f"Error: {stderr}")
    print()
    
    # Step 4: Commit changes
    print("Step 4: Creating new commit...")
    commit_msg = "Restore old fire version with hero video and logo clean layout from Professional AGENTIC Izzy platform design"
    success, stdout, stderr = run_git_command(f'git commit -m "{commit_msg}"', project_dir)
    if success:
        print("✓ Commit created successfully!")
        if stdout:
            print(stdout)
    else:
        if "nothing to commit" in stderr or "nothing to commit" in stdout:
            print("Note: No changes to commit (files might already be at this version)")
        else:
            print(f"Error: {stderr}")
    print()
    
    # Step 5: Push to GitHub
    print("Step 5: Pushing to GitHub...")
    success, stdout, stderr = run_git_command("git push origin main", project_dir)
    if success:
        print("✓ Successfully pushed to GitHub!")
    else:
        print(f"Push output: {stderr}")
    print()
    
    print("="*50)
    print("  RESTORATION COMPLETE!")
    print("="*50)
    print()
    print("Your website has been restored to the old fire version.")
    print("Check: https://github.com/Satayoo/satayoo-site-master")
    print()
    
    input("Press Enter to exit...")

if __name__ == "__main__":
    main()
