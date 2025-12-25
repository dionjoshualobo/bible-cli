#!/bin/sh
set -e

INSTALL_DIR="/usr/local/share/bible"
BIN_LINK="/usr/local/bin/bible"

echo "Installing bible CLI..."

sudo mkdir -p "$INSTALL_DIR"
 sudo cp bible bible.xml books.py "$INSTALL_DIR"
sudo chmod +x "$INSTALL_DIR/bible"
sudo ln -sf "$INSTALL_DIR/bible" "$BIN_LINK"

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
