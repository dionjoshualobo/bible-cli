#!/bin/sh
set -e

INSTALL_DIR="/usr/local/share/bible"
BIN_LINK="/usr/local/bin/bible"

echo "Installing bible CLI..."

sudo mkdir -p "$INSTALL_DIR"
 sudo cp bible ESV.xml books.py updater.py "$INSTALL_DIR"
sudo chmod +x "$INSTALL_DIR/bible"
sudo ln -sf "$INSTALL_DIR/bible" "$BIN_LINK"

# Record install metadata (if installing from a git clone, capture commit and origin)
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
if [ -d "$SCRIPT_DIR/.git" ]; then
    # Try to read commit and origin if git is available
    if command -v git >/dev/null 2>&1; then
        COMMIT=$(git -C "$SCRIPT_DIR" rev-parse --verify HEAD 2>/dev/null || true)
        ORIGIN=$(git -C "$SCRIPT_DIR" config --get remote.origin.url 2>/dev/null || true)
        if [ -n "$COMMIT" ]; then
            printf '%s\n' "$COMMIT" | sudo tee "$INSTALL_DIR/COMMIT" >/dev/null
        fi
        if [ -n "$ORIGIN" ]; then
            printf '%s\n' "$ORIGIN" | sudo tee "$INSTALL_DIR/ORIGIN" >/dev/null
        fi
    fi
fi

# Check for Python availability (python3 or python)
 # Check for python or python3 on PATH; warn the user if neither is available.
 if command -v python3 >/dev/null 2>&1; then
     PYEXEC=$(command -v python3)
 elif command -v python >/dev/null 2>&1; then
     PYEXEC=$(command -v python)
 else
     echo "WARNING: No Python interpreter found in PATH."
     echo "The 'bible' script requires Python to run. Install Python 3 and try again." >&2
 fi

echo "Done. Run: bible"
