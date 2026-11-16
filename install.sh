#!/usr/bin/env bash
set -euo pipefail
REPO="farishan-labs/vocus"
BRANCH="main"
BASE="https://raw.githubusercontent.com/${REPO}/${BRANCH}"

echo "Installing vocus..."
# deps
if command -v apt-get >/dev/null 2>&1; then
  sudo apt-get update
  sudo apt-get install -y python3 python3-pip libgtk-3-dev libwebkit2gtk-4.0-dev python3-gi
fi
# source
TMPDIR="$(mktemp -d)"
git clone "https://github.com/${REPO}.git" "$TMPDIR/vocus"
cd "$TMPDIR/vocus"
pip install --user -e .
echo "vocus installed. Run: vocus --help"