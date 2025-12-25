#!/bin/sh
set -e

INSTALL_DIR="/usr/local/share/bible"
BIN_LINK="/usr/local/bin/bible"

echo "Installing bible CLI..."

sudo mkdir -p "$INSTALL_DIR"
sudo cp bible bible.xml "$INSTALL_DIR"
sudo chmod +x "$INSTALL_DIR/bible"
sudo ln -sf "$INSTALL_DIR/bible" "$BIN_LINK"

echo "Done. Run: bible"
