"""Updater helper for bible-cli.

This module exposes `perform_update(base_dir: Path) -> int` which will:
- If `base_dir` is a git repo, run `git pull` in it.
- Otherwise download the latest main ZIP from GitHub, extract it, and run the appropriate
  platform installer (`install.sh` on POSIX, `install.ps1` via PowerShell on Windows).

Return codes: 0 == success, nonzero == failure.
"""
from pathlib import Path
import subprocess
import tempfile
import urllib.request
import zipfile
import shutil
import platform
import sys

REPO_ZIP_URL = 'https://github.com/dionjoshualobo/bible-cli/archive/refs/heads/main.zip'


def run_subproc(cmd, **kwargs):
    try:
        subprocess.run(cmd, check=True, **kwargs)
        return 0
    except subprocess.CalledProcessError as e:
        print(f"Command failed: {cmd}\nReturn: {e.returncode}")
        return e.returncode


def in_git_repo(path: Path) -> bool:
    return (path / '.git').exists()


def perform_update(base_dir: Path, check_only: bool = False) -> int:
    """Perform update for the project at `base_dir`.

    Returns 0 on success, non-zero on error.
    """
    base_dir = Path(base_dir)

    print("Starting update...")

    if in_git_repo(base_dir):
        # Git repo: either check or pull
        if check_only:
            print("Detected git repository. Checking for updates (fetching)...")
            rc = run_subproc(['git', '-C', str(base_dir), 'fetch'])
            if rc != 0:
                print("git fetch failed. Cannot determine update status.")
                return 1
            try:
                local = subprocess.check_output(['git', '-C', str(base_dir), 'rev-parse', 'HEAD']).strip()
                upstream = subprocess.check_output(['git', '-C', str(base_dir), 'rev-parse', '@{u}']).strip()
            except subprocess.CalledProcessError:
                print('Unable to determine upstream tracking branch. Cannot check update status.')
                return 1

            if local != upstream:
                print('Update available: local HEAD differs from upstream.')
                return 2
            else:
                print('Up-to-date: local HEAD matches upstream.')
                return 0
        else:
            print("Detected git repository. Pulling latest changes...")
            rc = run_subproc(['git', '-C', str(base_dir), 'pull'])
            if rc == 0:
                print("Repository updated. If you installed globally, re-run the installer to update system-installed files.")
            else:
                print("git pull failed. Please pull manually from inside the repository.")
            return rc

    # Not a git repo: either check or download+install
    if check_only:
        print('Not a git repository; cannot reliably check update status for non-git installs.')
        print(f"You can run the updater to download the latest snapshot: {REPO_ZIP_URL}")
        return 1

    print(f"Downloading latest from {REPO_ZIP_URL}...")
    tmpdir = Path(tempfile.mkdtemp(prefix='bible-update-'))
    try:
        zip_path = tmpdir / 'bible.zip'
        urllib.request.urlretrieve(REPO_ZIP_URL, str(zip_path))
        print(f"Downloaded to {zip_path}")

        with zipfile.ZipFile(str(zip_path), 'r') as z:
            z.extractall(str(tmpdir))

        # The extracted folder will be like bible-cli-main
        extracted_dirs = [p for p in tmpdir.iterdir() if p.is_dir()]
        if not extracted_dirs:
            print("Failed to find extracted content.")
            return 1

        src_dir = extracted_dirs[0]
        print(f"Extracted to {src_dir}")

        # Choose installer per platform
        system = platform.system()
        if system == 'Windows':
            installer = src_dir / 'install.ps1'
            pwsh = shutil.which('pwsh') or shutil.which('powershell')
            if not pwsh:
                print('PowerShell not found. Please run the downloaded installer manually:', installer)
                return 1
            print('Running Windows installer (PowerShell)...')
            rc = run_subproc([pwsh, '-ExecutionPolicy', 'Bypass', '-File', str(installer)])
            return 0 if rc == 0 else rc
        else:
            # POSIX (Linux/macOS)
            installer = src_dir / 'install.sh'
            if not installer.exists():
                print('No POSIX installer found in the downloaded release. Please update manually.')
                return 1

            # Prefer running the installer directly; it may prompt for sudo
            print('Running POSIX installer (may require sudo)...')
            # Try without sudo first
            rc = run_subproc(['sh', str(installer)], cwd=str(src_dir))
            if rc != 0:
                # Try with sudo if available
                if shutil.which('sudo'):
                    print('Retrying with sudo...')
                    rc = run_subproc(['sudo', 'sh', str(installer)], cwd=str(src_dir))
                else:
                    print('sudo not found. Please run the installer manually as root:')
                    print(str(installer))
                    return 1

            if rc == 0:
                print('Update and installation completed.')
            else:
                print('Update failed. Please run the installer manually from the extracted folder:', src_dir)
            return 0 if rc == 0 else rc
    finally:
        # Clean up temporary download directory if it exists
        try:
            if tmpdir.exists():
                shutil.rmtree(str(tmpdir))
        except Exception:
            pass
