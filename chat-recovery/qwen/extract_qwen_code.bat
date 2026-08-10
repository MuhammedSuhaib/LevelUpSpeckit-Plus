@echo off
REM Extract chat history from JSONL file(s)
REM Usage: extract_chat.bat (will ask for filename, wildcard, or directory)

echo.
echo ===== Chat History Extractor =====
echo.
set /p INPUT_PATH="Enter JSONL file path, wildcard, or directory (or drag here): "
if "%INPUT_PATH%"=="" (
    echo Error: No path specified!
    pause
    exit /b 1
)

:: Remove quotes if present
set INPUT_PATH=%INPUT_PATH:"=%

powershell -ExecutionPolicy Bypass -Command "& { $ErrorActionPreference = 'Stop'; $path = '%INPUT_PATH%'; if (Test-Path -Path $path -PathType Container) { $files = Get-ChildItem -LiteralPath $path -Filter *.jsonl } else { $files = Get-ChildItem -Path $path }; if (-not $files) { Write-Host 'No JSONL files found.'; exit 0 }; foreach ($f in $files) { if ($f.Extension -ne '.jsonl') { continue }; Write-Host ('Processing ' + $f.Name + '...'); $lines = Get-Content -LiteralPath $f.FullName -Raw; $jsonObjects = $lines -split '(?<=\n)(?=\{)' | Where-Object { $_.Trim() }; $output = @(); foreach ($jsonStr in $jsonObjects) { try { $obj = $jsonStr | ConvertFrom-Json; if ($obj.type -eq 'user' -and $obj.message.role -eq 'user') { $text = $obj.message.parts.text -join ''; if ($text) { $output += ('USER: ' + $text) } } elseif ($obj.type -eq 'assistant' -and $obj.message.role -eq 'model') { $parts = $obj.message.parts | Where-Object { -not $_.thought }; $text = $parts.text -join ''; if ($text) { $output += ('ASSISTANT: ' + $text) } } } catch { } }; $outFile = [System.IO.Path]::ChangeExtension($f.FullName, '.txt'); $output -join \"`n`n\" | Set-Content -LiteralPath $outFile -Encoding utf8; Write-Host ('  - Saved ' + $output.Count + ' messages to ' + $outFile) } }"

echo.
echo Done!
echo.
pause
