@echo off
echo ======================================================================
echo           REVERTING TO PREVIOUS VERSION
echo ======================================================================
echo.

REM Go back to the previous commit (before the wrong restoration)
git revert HEAD --no-edit

REM Push the revert
git push origin main

echo.
echo ======================================================================
echo REVERTED! Your site is back to how it was before.
echo.
echo Now let's find the RIGHT version with the hero video...
echo ======================================================================
echo.
echo Recent versions in your repository:
echo.

git log --oneline -20

echo.
echo ======================================================================
echo Which one has the hero video and clean layout you want?
echo Look for commits mentioning "video", "hero", or from August 2024
echo ======================================================================
pause
