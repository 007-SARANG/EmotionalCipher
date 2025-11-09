@echo off
echo.
echo ======================================================================
echo            🚀 Push EmotionCipher to GitHub
echo ======================================================================
echo.

REM Check if git is initialized
if not exist ".git" (
    echo Initializing Git repository...
    git init
    git branch -M main
    echo.
)

REM Add all files
echo Adding all files to Git...
git add .
echo.

REM Commit
echo Enter commit message (or press Enter for default):
set /p commit_msg="Commit message: "
if "%commit_msg%"=="" set commit_msg=Update EmotionCipher with Web GUI

echo.
echo Committing changes...
git commit -m "%commit_msg%"
echo.

REM Ask for remote URL if not set
git remote -v | find "origin" > nul
if errorlevel 1 (
    echo.
    echo ======================================================================
    echo Enter your GitHub repository URL:
    echo Example: https://github.com/username/EmotionCipher.git
    echo ======================================================================
    set /p repo_url="Repository URL: "
    git remote add origin %repo_url%
    echo.
)

REM Push to GitHub
echo Pushing to GitHub...
git push -u origin main
echo.

if errorlevel 0 (
    echo.
    echo ======================================================================
    echo ✅ Successfully pushed to GitHub!
    echo ======================================================================
    echo.
    echo Next steps:
    echo 1. Go to vercel.com and import your repository
    echo 2. Deploy your project
    echo 3. Get your live URL
    echo 4. Update README.md with the URL
    echo.
) else (
    echo.
    echo ======================================================================
    echo ❌ Push failed. Common issues:
    echo ======================================================================
    echo - Make sure you created the repository on GitHub
    echo - Check if you have the correct remote URL
    echo - Try: git remote set-url origin YOUR_CORRECT_URL
    echo - Ensure you're authenticated with GitHub
    echo.
)

pause
