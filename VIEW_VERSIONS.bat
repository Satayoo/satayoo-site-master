@echo off
echo ======================================================================
echo                     ALL AVAILABLE VERSIONS
echo ======================================================================
echo.
echo Looking for the "old fire" version with hero video...
echo.

git log --oneline -30

echo.
echo ======================================================================
echo TO RESTORE A DIFFERENT VERSION:
echo.
echo 1. Note the commit hash (7-character code)
echo 2. Run: git checkout [HASH] -- .
echo 3. Then: git add . 
echo 4. Then: git commit -m "Restore correct version"
echo 5. Then: git push origin main
echo ======================================================================
echo.
echo Which one is the "old fire" version you want?
echo.
pause
