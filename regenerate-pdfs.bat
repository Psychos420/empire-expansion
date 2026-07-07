@echo off
REM Baut alle Lead-Magnet-PDFs neu.
REM Voraussetzung: Python-Venv unter .venv wurde mit fpdf2 + markdown eingerichtet.

cd /d "%~dp0"
call .venv\Scripts\activate.bat
python 00-shared\tools\build-pdfs.py
pause
