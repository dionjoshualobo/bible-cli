#!/usr/bin/env pwsh
# Simple Windows installer for bible-cli.
# It copies the Python script and data into `%LOCALAPPDATA%\bible-cli`, creates a `bible.cmd` wrapper,
# and adds that folder to the current user's PATH.
#
# Run in PowerShell:
#     .\install.ps1
# or (if execution policy blocks):
#     powershell -ExecutionPolicy Bypass -File .\install.ps1

$ErrorActionPreference = 'Stop'

Write-Host "Installing bible CLI for current user..."

$installDir = Join-Path $env:LOCALAPPDATA 'bible-cli'
Write-Host "Target install directory: $installDir"

New-Item -ItemType Directory -Force -Path $installDir | Out-Null

$scriptDir = Split-Path -Parent $MyInvocation.MyCommand.Definition

# Copy the main script as bible.py (Windows-friendly name)
Copy-Item -Path (Join-Path $scriptDir 'bible') -Destination (Join-Path $installDir 'bible.py') -Force
Copy-Item -Path (Join-Path $scriptDir 'bible.xml') -Destination $installDir -Force
Copy-Item -Path (Join-Path $scriptDir 'books.py') -Destination $installDir -Force

# Create a CMD wrapper to allow running `bible` from cmd/PowerShell.
# The wrapper will try 'python' first, then the 'py' launcher.
$cmdPath = Join-Path $installDir 'bible.cmd'
$cmdContent = @"
@echo off
where python >nul 2>&1
if %errorlevel%==0 (
  python "%~dp0\bible.py" %*
  goto :eof
)
where py >nul 2>&1
if %errorlevel%==0 (
  py -3 "%~dp0\bible.py" %*
  goto :eof
)
echo Python 3 is not installed or not on PATH. Please install Python 3 from https://www.python.org/downloads/
exit /b 1
"@
Set-Content -Path $cmdPath -Value $cmdContent -Encoding ASCII

# Ensure the install directory is in the user PATH
$userPath = [Environment]::GetEnvironmentVariable('Path','User')
if (-not $userPath) { $userPath = "" }
if ($userPath -notlike "*$installDir*") {
    Write-Host "Adding $installDir to the user PATH..."
    if ($userPath -eq "") { $newPath = $installDir } else { $newPath = "$userPath;$installDir" }
    [Environment]::SetEnvironmentVariable('Path', $newPath, 'User')
    Write-Host "Added. You may need to restart your terminal for changes to take effect."
} else {
    Write-Host "Install directory already in user PATH."
}

# Check for Python presence (python or py launcher)
$hasPython = $false
if (Get-Command python -ErrorAction SilentlyContinue) { $hasPython = $true }
elseif (Get-Command py -ErrorAction SilentlyContinue) { $hasPython = $true }

if (-not $hasPython) {
    Write-Warning "Python 3 was not found on this system."
    Write-Host "This tool requires Python 3 to run the 'bible' script. Please install Python 3 (https://www.python.org/downloads/) and re-open your terminal."
}

Write-Host "Installation complete. Open a new terminal and run: bible"
