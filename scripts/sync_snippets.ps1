# 🛠️ PowerShell: Sync + Git Push

Write-Host "-------------------------------------"
Write-Host "🔁 STEP 1: Syncing VS Code snippets..."
Write-Host "-------------------------------------"

python scripts/sync_snippets.py

Write-Host ""
Write-Host "-------------------------------------"
Write-Host "🚀 STEP 2: Committing snippet updates via Git..."
Write-Host "-------------------------------------"

Start-Process -NoNewWindow -Wait -FilePath "scripts\git\git_push.bat"

Write-Host ""
Write-Host "✅ Snippet sync + Git push completed."
Pause
# scripts/sync_snippets.ps1