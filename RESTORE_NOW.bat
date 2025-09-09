@echo off
echo ============================================
echo   RESTORING OLD FIRE VERSION WITH HERO VIDEO
echo ============================================
echo.

cd /d "C:\Users\izzyh\OneDrive - Community College of Philadelphia\Documents\satayoo-site-master"

echo Step 1: Creating backup branch...
git branch backup-dec2024 2>nul
echo.

echo Step 2: Restoring files from the old version (fa68f18)...
git checkout fa68f18 -- .
if %errorlevel% neq 0 (
    echo ERROR: Failed to restore files!
    pause
    exit /b 1
)
echo Successfully restored files!
echo.

echo Step 3: Staging all changes...
git add .
echo.

echo Step 4: Creating new commit...
git commit -m "Restore old fire version with hero video and logo clean layout from Professional AGENTIC Izzy platform design"
echo.

echo Step 5: Pushing to GitHub...
git push origin main
echo.

echo ============================================
echo   RESTORATION COMPLETE!
echo ============================================
echo.
echo Your website has been restored to the old fire version.
echo Check https://github.com/Satayoo/satayoo-site-master
echo.
pause
