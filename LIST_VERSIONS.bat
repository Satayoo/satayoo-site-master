@echo off
echo ============================================
echo   AVAILABLE VERSIONS TO RESTORE
echo ============================================
echo.
cd /d "C:\Users\izzyh\OneDrive - Community College of Philadelphia\Documents\satayoo-site-master"

echo Recent commits that might contain the hero video version:
echo.
git --no-pager log --oneline -20
echo.
echo ============================================
echo To restore a specific version, note the commit hash (like fa68f18)
echo Then run: git checkout HASH -- .
echo          git add .
echo          git commit -m "Restore old version"
echo          git push origin main
echo ============================================
pause
