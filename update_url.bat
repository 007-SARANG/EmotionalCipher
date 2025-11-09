@echo off
echo.
echo ======================================================================
echo       🔗 Update README with Vercel Deployment URL
echo ======================================================================
echo.
echo After deploying to Vercel, you'll get a URL like:
echo https://emotion-cipher-xyz123.vercel.app
echo.
echo Enter your Vercel URL below:
echo.
set /p vercel_url="Vercel URL: "

echo.
echo Updating README.md...
python update_vercel_url.py "%vercel_url%"

echo.
echo ======================================================================
echo Next steps:
echo ======================================================================
echo 1. Add screenshots to screenshots/ folder
echo 2. Run: git add README.md screenshots/
echo 3. Run: git commit -m "Update live URL and add screenshots"
echo 4. Run: git push
echo.

pause
