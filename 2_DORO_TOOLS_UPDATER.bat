@echo off
setlocal enabledelayedexpansion
cls

:: Display warning and ask for confirmation
echo WARNING: This will completely replace your DORO_Tools folder with fresh files.
echo Any existing files will be permanently deleted, so make sure you don't have important files in your "Repacked" folders.
echo.
echo IMPORTANT: 
echo If the downloads fail or you get the MEGA servers error you need to close this window and double-click this file again,
echo eventually the downloads will start properly.
echo.
set /p "update_confirmation=Do you wish to update the tools now? Yes/No [y/n]: "

:: Check user response
if /i "%update_confirmation%"=="y" goto proceed
if /i "%update_confirmation%"=="yes" goto proceed
echo Update cancelled by user.
pause
exit /b

:proceed
:: Define the output folder path
set "output_folder=%~dp0DORO_Tools"

:: Cleanup existing files
echo Preparing for fresh download...
if exist "%output_folder%" (
    echo Removing old files...
    rmdir /s /q "%output_folder%" >nul 2>&1
    if exist "%output_folder%" (
        echo ERROR: Could not remove old files.
        echo Please close any programs using these files and try again.
        pause
        exit /b
    )
)

:: Recreate the folder
mkdir "%output_folder%" >nul 2>&1

:: Test internet connection
echo Testing connection to MEGA...
ping -n 1 mega.nz >nul 2>&1 || (
    echo ERROR: Cannot reach MEGA servers.
    echo Please check your internet connection.
    pause
    exit /b
)

:: Execute the Python downloader script
echo Starting download process...
python megadownloader.py

if errorlevel 1 (
    echo.
    echo ERROR: Download failed (Error Code: %errorlevel%)
    pause
    exit /b
)

echo.
echo SUCCESS: Update completed successfully.
pause