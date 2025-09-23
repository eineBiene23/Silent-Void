@echo off
title SB3 Project Unpacker Launcher

:: --- Checks ---
:: Check 1: Was a file dropped onto the script?
if "%~1"=="" (
    echo Error: No .sb3 file was provided.
    echo.
    echo Please drag and drop your .sb3 project file onto this script.
    goto end
)

cd..
:: Check 2: Does the Python script exist in this folder?
if not exist "sb3-unzip.bat" (
    echo Error: Could not find the Batch script 'sb3-unzip.bat' in this folder.
    goto end
)

:: --- Main Process ---
echo.
echo Running the main script...
echo --------------------------------
:: Run the python script with the dropped file as the first argument
:: and "src" as the second argument.
sb3-unzip.bat "%~1"
echo --------------------------------


:end
echo Process terminated.
timeout -t -1 >nul
exit /b