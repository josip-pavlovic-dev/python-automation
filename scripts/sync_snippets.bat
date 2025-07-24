@echo off
:: 🔄 Sync & Push Snippets – Full Automation (Windows)

echo -------------------------------------
echo 🔁 STEP 1: Syncing VS Code snippets...
echo -------------------------------------

python scripts\sync_snippets.py

echo.
echo -------------------------------------
echo 🚀 STEP 2: Committing snippet updates via Git...
echo -------------------------------------

call scripts\git\git_push.bat

echo.
echo ✅ Snippet sync + Git push completed.
pause
.