@echo off
echo Opening config files...
code --reuse-window "C:\Users\%USERNAME%\.claude-code-router\config.json" "C:\Users\%USERNAME%\.qwen\oauth_creds.json"
pause