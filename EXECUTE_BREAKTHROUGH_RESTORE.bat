@echo off
echo ======================================================================
echo    RESTORING BREAKTHROUGH AI VERSION (137092e)
echo ======================================================================
echo.

REM Navigate to project directory
cd /d "C:\Users\izzyh\OneDrive - Community College of Philadelphia\Documents\satayoo-site-master"
echo Current directory: %CD%
echo.

REM Step 1: Restore the Breakthrough AI version (commit 137092e)
echo Step 1: Restoring the Breakthrough AI version (commit 137092e)...
git checkout 137092e -- .
if %errorlevel% neq 0 (
    echo ERROR: Failed to restore files!
    pause
    exit /b 1
)
echo SUCCESS: Files restored from Breakthrough AI version!
echo.

REM Step 2: Stage all changes
echo Step 2: Staging all changes...
git add .
echo SUCCESS: All changes staged!
echo.

REM Step 3: Commit with descriptive message
echo Step 3: Creating commit...
git commit -m "Restore Breakthrough AI version with Zeta focus, AI logos, and blog"
if %errorlevel% equ 0 (
    echo SUCCESS: Commit created!
) else (
    echo Note: Nothing to commit or already at this version
)
echo.

REM Step 4: Push to GitHub
echo Step 4: Pushing to GitHub...
git push origin main
if %errorlevel% equ 0 (
    echo SUCCESS: Pushed to GitHub!
) else (
    echo Note: May already be up to date
)
echo.

echo ======================================================================
echo    RESTORATION COMPLETE!
echo ======================================================================
echo.
echo The Breakthrough AI version has been restored with:
echo   - Breakthrough AI for Active Living tagline
echo   - Zeta-focused content
echo   - Different AI logos
echo   - Blog section
echo.
echo Check your site at: https://github.com/Satayoo/satayoo-site-master
echo.
pause
