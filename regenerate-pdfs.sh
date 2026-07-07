#!/usr/bin/env bash
# Baut alle Lead-Magnet-PDFs neu.
# Voraussetzung: Python-Venv unter .venv wurde mit fpdf2 + markdown eingerichtet.

set -e
cd "$(dirname "$0")"
source .venv/Scripts/activate
python 00-shared/tools/build-pdfs.py
