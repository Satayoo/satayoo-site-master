@echo off
echo ======================================================================
echo    RESTORING VERSION WITH BREAKTHROUGH AI TAGLINE AND LOGOS
echo ======================================================================
echo.

cd /d "C:\Users\izzyh\OneDrive - Community College of Philadelphia\Documents\satayoo-site-master"

echo Step 1: Restoring the Breakthrough AI version (137092e)...
echo This version has: "Breakthrough AI for Active Living"
echo.

git checkout 137092e -- .

if %errorlevel% neq 0 (
    echo ERROR: Failed to restore files!
    pause
    exit /b 1
)

echo Successfully restored the Breakthrough AI version!
echo.

echo Step 2: Staging all changes...
git add .
echo.

echo Step 3: Creating new commit...
git commit -m "Restore version with Breakthrough AI tagline, different AI logos and blog"
echo.

echo Step 4: Pushing to GitHub...
git push origin main
echo.

echo ======================================================================
echo    RESTORATION COMPLETE!
echo ======================================================================
echo.
echo The version with Breakthrough AI tagline and logos has been restored!
echo Check https://github.com/Satayoo/satayoo-site-master
echo.
pause
