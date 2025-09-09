# PowerShell script to restore the old fire version
Write-Host "============================================" -ForegroundColor Cyan
Write-Host "  RESTORING OLD FIRE VERSION WITH HERO VIDEO" -ForegroundColor Cyan
Write-Host "============================================" -ForegroundColor Cyan
Write-Host ""

# Change to project directory
Set-Location "C:\Users\izzyh\OneDrive - Community College of Philadelphia\Documents\satayoo-site-master"

Write-Host "Step 1: Creating backup branch..." -ForegroundColor Yellow
git branch backup-dec2024 2>$null
Write-Host ""

Write-Host "Step 2: Restoring files from the old version (fa68f18)..." -ForegroundColor Yellow
git checkout fa68f18 -- .
if ($LASTEXITCODE -ne 0) {
    Write-Host "ERROR: Failed to restore files!" -ForegroundColor Red
    Read-Host "Press Enter to exit"
    exit 1
}
Write-Host "Successfully restored files!" -ForegroundColor Green
Write-Host ""

Write-Host "Step 3: Staging all changes..." -ForegroundColor Yellow
git add .
Write-Host ""

Write-Host "Step 4: Creating new commit..." -ForegroundColor Yellow
git commit -m "Restore old fire version with hero video and logo clean layout from Professional AGENTIC Izzy platform design"
Write-Host ""

Write-Host "Step 5: Pushing to GitHub..." -ForegroundColor Yellow
git push origin main
Write-Host ""

Write-Host "============================================" -ForegroundColor Cyan
Write-Host "  RESTORATION COMPLETE!" -ForegroundColor Green
Write-Host "============================================" -ForegroundColor Cyan
Write-Host ""
Write-Host "Your website has been restored to the old fire version." -ForegroundColor Green
Write-Host "Check https://github.com/Satayoo/satayoo-site-master" -ForegroundColor Cyan
Write-Host ""
Read-Host "Press Enter to exit"
