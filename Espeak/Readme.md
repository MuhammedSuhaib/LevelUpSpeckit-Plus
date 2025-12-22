# Audio Notification Script (Speak)

## What this is

A small script that **speaks messages aloud**.
Useful when you are **multitasking** and not staring at the terminal.

---

## Why use it

* Know when a task finishes
* Hear errors instantly
* No need to watch logs
* Saves time during hackathons

---

## Where to place the files (Important)

Put the scripts here:

```
.specify/scripts/bash
```

Do **not** move them.

Files:

* `speak.bat` → **Windows**
* `speak.sh` → **Linux / macOS**

---

## Which script to use

| OS            | Script      |
| ------------- | ----------- |
| Windows       | `speak.bat` |
| Linux / macOS | `speak.sh`  |

---

## Requirements

**Windows**

* Windows 10/11
* PowerShell (already installed)

**Linux / macOS**

* Bash
* `espeak` installed

---

## Manual usage

**Windows**

```bat
.specify\scripts\bash\speak.bat "Task completed"
```

**Linux / macOS**

```bash
.specify/scripts/bash/speak.sh "Task completed"
```

---

## System Prompt (Copy-Paste)

Use this in **agent system instructions**:

```
You are allowed to use audio notifications when the user is multitasking.

Audio scripts are available at:
- Windows: .specify\scripts\bash\speak.bat
- Linux/macOS: .specify/scripts/bash/speak.sh

Use them for:
- task completion
- errors
- important status updates

Use the correct script based on OS.
Keep messages short.
```

---

## Summary

Small script.
Big time saver.
Perfect for hackathons.
