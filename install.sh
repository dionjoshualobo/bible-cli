#!/bin/sh
set -e

INSTALL_DIR="/usr/local/share/bible"
BIN_LINK="/usr/local/bin/bible"

echo "Installing bible CLI..."

sudo mkdir -p "$INSTALL_DIR"
sudo cp bible bible.xml "$INSTALL_DIR"
sudo chmod +x "$INSTALL_DIR/bible"
sudo ln -sf "$INSTALL_DIR/bible" "$BIN_LINK"

# Check for Python availability (python3 or python)
if command -v python3 >/dev/null 2>&1; then
	: # python3 available
elif command -v python >/dev/null 2>&1; then
	: # python available
else
	echo "\nWARNING: Python 3 was not found on this system." >&2
	echo "This tool requires Python 3 to run the 'bible' script." >&2
	echo "Please install Python 3 (e.g. on Debian/Ubuntu: 'sudo apt install python3', on macOS: 'brew install python') and re-run the installer or ensure 'python'/'python3' is on your PATH." >&2
fi

echo "Done. Run: bible"
