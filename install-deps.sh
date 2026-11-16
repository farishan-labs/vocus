#!/usr/bin/env bash
set -euo pipefail
sudo apt-get update
sudo apt-get install -y python3 python3-pip libgtk-3-dev libwebkit2gtk-4.0-dev python3-gi
echo "deps installed"