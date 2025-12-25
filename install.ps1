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

# Create a CMD wrapper to allow running `bible` from cmd/powerShell
$cmdPath = Join-Path $installDir 'bible.cmd'
$cmdContent = "@echo off`r`npython \"%~dp0\\bible.py\" %*"
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

Write-Host "Installation complete. Open a new terminal and run: bible"
