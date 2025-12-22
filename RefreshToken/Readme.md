## Auto Qwen Token Refresh for Claude Code Router

### Problem

During hackathons:

* Qwen access tokens expire
* CCR stops working
* You lose time reopening Qwen, copying tokens, restarting CCR

This script **automates everything**.

---

### What this script does

1. Launches Qwen to refresh the OAuth token
2. Waits until the new token is generated
3. Closes Qwen automatically
4. Updates Claude Code Router config
5. Restarts CCR
6. Opens `ccr code` in a new terminal

All in **one command**.

---

### Why this saves time in a hackathon

* No manual token copying
* No UI clicking
* No restarting services by hand
* Fixes token issues in **~10 seconds**

You stay focused on coding.

---

### How to use

Use VSCode code runner extension to run this script with a single click.

OR

```bash
python refresh_token.py
```
---

### When to run it

* Whenever you get 401 errors


# Optional (Manual Debug Helper)

If someone can’t run the Python script, this batch file is included only for manual inspection:
[Manual script](Manual.bat)

# HERE ARE SOME MAIN CCR Shortcuts:

 ```! for bash mode       double tap esc to clear input      ctrl + _ to undo
  / for commands        alt + m to auto-accept edits       alt + v to paste images
  @ for file paths      ctrl + o for verbose output        alt + p to switch model
  # to memorize         ctrl + t to show todos             ctrl + s to stash prompt```
  & for background      \⏎ for newline
