@echo off
REM Extract chat history from JSONL file
REM Usage: filter.bat (will ask for filename)

echo.
echo ===== Chat History Extractor =====
echo.
set /p INPUT_FILE="Enter JSONL file path (or drag file here): "
if "%INPUT_FILE%"=="" (
    echo Error: No file specified!
    pause
    exit /b 1
)

:: Strip quotes if the user dragged and dropped the file
set "INPUT_FILE=%INPUT_FILE:"=%"

:: Set output file to same path and name, just with .md extension
for %%F in ("%INPUT_FILE%") do set "OUTPUT_FILE=%%~dpnF.md"

echo.
echo Input: %INPUT_FILE%
echo Output: %OUTPUT_FILE%
echo.

powershell -NoProfile -Command "& { $ErrorActionPreference = 'Stop'; $lines = Get-Content '%INPUT_FILE%' -Raw; $jsonObjects = $lines -split '(?<=\n)(?=\{)' | Where-Object { $_.Trim() }; $output = @(); foreach ($jsonStr in $jsonObjects) { try { $obj = $jsonStr | ConvertFrom-Json; if ($obj.type -eq 'user') { $text = ($obj.content | ForEach-Object { $_.text }) -join ''; if ($text) { $output += ('USER: ' + $text) } } elseif ($obj.type -eq 'gemini') { if ($obj.content) { $output += ('ASSISTANT: ' + $obj.content) } } } catch { } }; $output -join \"`n`n\" | Out-File '%OUTPUT_FILE%' -Encoding utf8; Write-Host \"Done! Extracted $($output.Count) messages\" }"

echo.
echo Output saved to: %OUTPUT_FILE%
echo.
pause