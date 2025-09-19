@echo off
REM Batch file version
for /f "tokens=2 delims==" %%a in ('wmic OS Get localdatetime /value') do set "dt=%%a"
set "YY=%dt:~0,4%" & set "MM=%dt:~4,2%" & set "DD=%dt:~6,2%"
set "folder_name=src\\%YY%-%MM%-%DD%"
mkdir "%folder_name%" 2>nul
if exist "%folder_name%" (
    echo Folder "%folder_name%" created successfully.
) else (
    echo Folder "%folder_name%" already exists.
)

REM PowerShell version (uncomment the line below to use instead)
REM powershell -Command "New-Item -ItemType Directory -Name (Get-Date -Format 'yyyy-MM-dd') -Force | Out-Null; Write-Host 'Folder created:' (Get-Date -Format 'yyyy-MM-dd')"
