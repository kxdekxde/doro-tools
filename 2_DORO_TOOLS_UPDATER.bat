@echo off
setlocal enabledelayedexpansion
cls

:: Display warning and ask for confirmation
echo WARNING: This will completely replace your DORO_Tools folder with fresh files.
echo Any existing files will be permanently deleted, so make sure you don't have important files in your "Repacked" folders.
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

:: Execute the Python downloader script with retry logic
set "max_retries=10"
set "retry_count=0"

:download_retry
echo Starting download process (Attempt !retry_count!/!max_retries!)...
python megadownloader.py

if errorlevel 1 (
    set /a retry_count+=1
    echo.
    echo ERROR: Download failed (Error Code: %errorlevel%)
    
    if !retry_count! lss !max_retries! (
        echo Retrying in 5 seconds...
        timeout /t 5 /nobreak >nul
        goto download_retry
    ) else (
        echo Maximum retry attempts reached. Update failed.
        pause
        exit /b
    )
)

echo.
echo SUCCESS: Update completed successfully.
pause
