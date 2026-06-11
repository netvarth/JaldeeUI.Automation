$ErrorActionPreference = "Stop"

Write-Host "Running tests with Allure..." -ForegroundColor Cyan

# Clean previous report output so stale reports do not open after import errors.
if (Test-Path "reports/allure-results") {
    Remove-Item -Recurse -Force "reports/allure-results"
}

if (Test-Path "reports/allure-report") {
    Remove-Item -Recurse -Force "reports/allure-report"
}

New-Item -ItemType Directory -Force -Path "reports/current" | Out-Null
New-Item -ItemType Directory -Force -Path "reports/artifacts" | Out-Null
New-Item -ItemType Directory -Force -Path "reports/allure-results" | Out-Null
New-Item -ItemType Directory -Force -Path "reports/allure-report" | Out-Null

pytest

$pytestExitCode = $LASTEXITCODE

$allureResultFiles = Get-ChildItem "reports/allure-results" -Filter "*.json" -ErrorAction SilentlyContinue

if ($allureResultFiles.Count -eq 0) {
    Write-Host ""
    Write-Host "No Allure result files were generated. Skipping Allure report generation." -ForegroundColor Yellow
    Write-Host "Fix the pytest error above and run again." -ForegroundColor Yellow
    exit $pytestExitCode
}

Write-Host ""
Write-Host "Writing Allure environment details..." -ForegroundColor Cyan

@"
Environment=scale
Framework=Playwright + Pytest
Language=Python
Browser=Chromium
Report=Allure
"@ | Out-File -Encoding utf8 "reports/allure-results/environment.properties"

Write-Host ""
Write-Host "Generating Allure report..." -ForegroundColor Cyan

allure generate reports/allure-results -o reports/allure-report --clean

Write-Host ""
Write-Host "Allure report generated:" -ForegroundColor Green
Write-Host "reports/allure-report"

Write-Host ""
Write-Host "Opening Allure report..." -ForegroundColor Cyan
allure open reports/allure-report

exit $pytestExitCode