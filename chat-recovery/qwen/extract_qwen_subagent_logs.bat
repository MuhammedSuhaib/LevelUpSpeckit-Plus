@echo off
REM Extract chat messages and Qwen sub-agent tool execution traces from JSONL log files.
REM Works for both main chat logs and Qwen sub-agent trace files (e.g., agent-a1f2d38.jsonl).

echo.
echo ===== Qwen Sub-Agent ^& Chat Log Extractor =====
echo.
set /p INPUT_PATH="Enter JSONL file path, wildcard, or directory (or drag here): "
if "%INPUT_PATH%"=="" (
    echo Error: No path specified!
    pause
    exit /b 1
)

:: Remove quotes if present
set INPUT_PATH=%INPUT_PATH:"=%

powershell -ExecutionPolicy Bypass -Command "$ErrorActionPreference = 'Stop'; $path = '%INPUT_PATH%'; $files = if (Test-Path -Path $path -PathType Container) { Get-ChildItem -LiteralPath $path -Filter *.jsonl } else { Get-ChildItem -Path $path }; if (-not $files) { Write-Host 'No JSONL files found.'; exit 0 }; foreach ($f in $files) { if ($f.Extension -ne '.jsonl') { continue }; Write-Host ('Processing ' + $f.Name + '...'); $rawLines = Get-Content -LiteralPath $f.FullName -Encoding utf8; $output = @(); foreach ($line in $rawLines) { if (-not $line.Trim()) { continue }; try { $obj = $line | ConvertFrom-Json; if ($obj.type -eq 'user') { if ($obj.message.content -is [string]) { $output += ('USER: ' + $obj.message.content) } elseif ($obj.message.parts) { $text = ($obj.message.parts | Where-Object { $_.text }).text -join ''; if ($text) { $output += ('USER: ' + $text) } } } elseif ($obj.type -eq 'assistant') { if ($obj.message.content -is [array]) { foreach ($item in $obj.message.content) { if ($item.type -eq 'text' -and $item.text) { $output += ('ASSISTANT: ' + $item.text) } elseif ($item.type -eq 'tool_use') { $output += ('TOOL CALL [' + $item.name + ']: ' + ($item.input | ConvertTo-Json -Compress)) } } } elseif ($obj.message.content -is [string]) { $output += ('ASSISTANT: ' + $obj.message.content) } elseif ($obj.message.parts) { $text = ($obj.message.parts | Where-Object { -not $_.thought -and $_.text }).text -join ''; if ($text) { $output += ('ASSISTANT: ' + $text) } } } } catch { } }; $outFile = [System.IO.Path]::ChangeExtension($f.FullName, '.txt'); $output -join \"`r`n`r`n----------------------------------------`r`n`r`n\" | Set-Content -LiteralPath $outFile -Encoding utf8; Write-Host ('  - Saved ' + $output.Count + ' entries to ' + $outFile) }"

echo.
echo Done!
echo.
pause
