@echo off
title Git Auto Push Script
echo 📤 Git Auto Push Script
echo -------------------------

set /p msg=🔤 Enter commit message: 
if "%msg%"=="" (
    echo ❌ Commit message is required!
    pause
    exit /b
)

git add .
git commit -m "%msg%"
git push

echo ✅ Push completed!
pause
