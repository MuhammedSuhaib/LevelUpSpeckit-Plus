import os , time , json , subprocess 
from pathlib import Path

# --- Configuration ---
USER_PROFILE = Path.home()
QWEN_CREDS_PATH = USER_PROFILE / ".qwen" / "oauth_creds.json"
CCR_CONFIG_PATH = USER_PROFILE / ".claude-code-router" / "config.json"
PROVIDER_NAME = "qwen"

try:
    # 1. Run Qwen in non-interactive mode to refresh token
    print("Running Qwen in non-interactive mode to refresh token...")
    subprocess.run("qwen \"hi\"", shell=True)
    # Wait a bit for the token to be refreshed
    time.sleep(2)
    if not QWEN_CREDS_PATH.exists():
        raise FileNotFoundError("Qwen credentials file was not created after non-interactive run")

    # No need to kill qwen since non-interactive mode should complete on its own


    # 2. Read the new token (ensure file exists)
    if not QWEN_CREDS_PATH.exists():
        raise FileNotFoundError("Qwen credentials file not found")

    with open(QWEN_CREDS_PATH, "r", encoding="utf-8") as f:
        qwen_creds = json.load(f)

    new_token = qwen_creds.get("access_token")
    if not new_token:
        raise ValueError("Could not find 'access_token' in Qwen credentials.")

    print(f"Extracted new token: {new_token[:8]}...")

    # 3. Update CCR config (ensure file exists)
    if not CCR_CONFIG_PATH.exists():
        raise FileNotFoundError("CCR config file not found")

    with open(CCR_CONFIG_PATH, "r", encoding="utf-8") as f:
        ccr_config = json.load(f)

    provider_found = False
    for provider in ccr_config.get("Providers", []):
        if provider.get("name") == PROVIDER_NAME:
            provider["api_key"] = new_token
            provider_found = True
            break

    if not provider_found:
        raise ValueError("Qwen provider not found in CCR config")

    with open(CCR_CONFIG_PATH, "w", encoding="utf-8") as f:
        json.dump(ccr_config, f, indent=4)

    print("CCR config updated successfully.")

    # 4. Restart CCR
    print("Restarting CCR...")
    subprocess.run("ccr restart", shell=True, check=True)

    # 5. Open CCR in interactive mode
    print("Launching Claude Code...")
    subprocess.run("cls", shell=True)
    subprocess.Popen("start cmd /k ccr code --continue", shell=True)

    print("Done.")

except Exception as e:
    print(f"Error: {e}")
