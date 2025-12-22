@echo off
REM Audible notification using PowerShell TTS
REM Usage: speak.bat "Your message here"

if "%~1"=="" (
  echo Usage: speak.bat "Your message here"
  exit /b 1
)

powershell -NoProfile -Command "Add-Type -AssemblyName System.Speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak('%*')"
