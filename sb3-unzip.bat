@echo off
title SB3 Project Unpacker

:: --- Checks ---
:: Check 1: Was a file dropped onto the script?
if "%~1"=="" (
    echo Error: No .sb3 file was provided.
    echo.
    echo Please drag and drop your .sb3 project file onto this script.
    goto end
)

:: Check 2: Does the Python script exist in this folder?
if not exist "sb3-unzip.py" (
    echo Error: Could not find the Python script 'unpacker.py' in this folder.
    goto end
)

:: --- Main Process ---
echo File provided: %~1
echo.
echo Running the unpacker...
echo --------------------------------
:: Run the python script with the dropped file as the first argument
:: and "src" as the second argument.
python sb3-unzip.py "%~1" "src"
echo --------------------------------
echo.
echo Process finished.

:end
echo Process terminated.
timeout -t -1 >nul
exit /b