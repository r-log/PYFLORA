@echo off
>nul 2>&1 "%SYSTEMROOT%\system32\cacls.exe" "%SYSTEMROOT%\system32\config\system"
if '%errorlevel%' NEQ '0' (
    echo Requesting administrative privileges...
    goto UACPrompt
) else ( goto gotAdmin )

:UACPrompt
    echo Set UAC = CreateObject^("Shell.Application"^) > "%temp%\getadmin.vbs"
    echo UAC.ShellExecute "%~s0", "", "", "runas", 1 >> "%temp%\getadmin.vbs"
    "%temp%\getadmin.vbs"
    exit /B

:gotAdmin
    if exist "%temp%\getadmin.vbs" ( del "%temp%\getadmin.vbs" )
    pushd "%CD%"
    CD /D "%~dp0"

echo Running PyFlora...
del debug_out.txt 2>nul
start /B cmd /c "python main.py > debug_out.txt 2>&1"
echo Waiting for application to initialize...
timeout /t 3 > nul

:check_output
cls
echo ========== CURRENT OUTPUT ==========
type debug_out.txt
echo ===================================
timeout /t 1 > nul
goto check_output