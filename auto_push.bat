@echo off
echo ===============================
echo   Python Practice Git Auto Push
echo ===============================

:: Check if git is installed
git --version >nul 2>&1
if errorlevel 1 (
    echo Git is not installed or not in PATH.
    pause
    exit /b
)

:: Check if folder is a git repo
if not exist ".git" (
    echo This folder is not a git repository.
    pause
    exit /b
)

echo Checking git status...
git status

:: Check if there are changes
git diff --quiet
if %errorlevel%==0 (
    echo No changes detected. Nothing to commit.
    pause
    exit /b
)

echo.
echo Adding files...
git add .

echo.
set msg=Auto update %date% %time%

echo Committing changes...
git commit -m "%msg%" 2>nul

if errorlevel 1 (
    echo Commit failed.
    pause
    exit /b
)

echo.
echo Pushing to GitHub...
git push origin main

if errorlevel 1 (
    echo Push failed.
    pause
    exit /b
)

echo.
echo ==================================
echo   Successfully pushed to GitHub
echo ==================================

pause