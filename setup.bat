@echo off
setlocal

python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo Python is not installed! Downloading now...
    
    set PYTHON_URL=https://www.python.org/ftp/python/3.11.0/python-3.11.0rc2-amd64.exe
    set INSTALLER_PATH=%TEMP%\python_installer.exe

    powershell -Command "(New-Object System.Net.WebClient).DownloadFile('%PYTHON_URL%', '%INSTALLER_PATH%')"

    if exist "%INSTALLER_PATH%" (
        echo Installing Python...
        start /wait %INSTALLER_PATH% /quiet InstallAllUsers=1 PrependPath=1
        del %INSTALLER_PATH%
    ) else (
        echo Failed to download Python!
        exit /b 1
    )

    python --version >nul 2>&1
    if %errorlevel% neq 0 (
        echo Python installation failed!
        exit /b 1
    )
)

echo Python is installed!

:: Upgrade pip and install required libraries
echo Installing Python libraries...
python -m pip install --upgrade pip
python -m pip install colorama keyboard

echo All done!
exit /b 0
