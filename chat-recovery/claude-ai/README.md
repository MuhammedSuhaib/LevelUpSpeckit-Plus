# Claude.ai Chat Recovery

Recover and clean conversation history exported from [Claude.ai](https://claude.ai).

## Why this is critical

Claude accounts can be banned or restricted at any time (false age flags, policy mistakes, etc.).  
When that happens the **only** thing you can still do is download your data once.  
After that the chats are gone forever unless you already extracted them.

This tool exists so you can:

- Rescue every usable conversation **before** or **immediately after** a ban.
- Convert the messy export into clean request/response turns.
- Resume the same context in any other agent (Qwen, Gemini, Claude Code Router, ChatGPT, etc.).

> **Real case**: Claude flagged an adult account as under-18 and demanded selfie verification.  
> Uploading a selfie to a company that already mishandled the age check was not an option.  
> The only path taken was the data export + this script.

**Do this regularly.** Don’t wait for the ban email.

## Overview

Claude data exports arrive as a ZIP. After extraction you get account metadata plus a single large `conversations.json` file that holds every chat as an array of objects. Many of those objects are empty (deleted chats, aborted sessions, etc.). This tool filters out empty conversations and produces clean, readable per-chat JSON files that can be resumed in other agents or tools.

## Export ZIP Structure

```
C:.
│   conversations.json     # Array of all chat objects: [{chat}, {chat}, ...]
│   login_history.json     # Login / auth history
│   users.json             # Account details
│
└───projects/
        <project-id>.json  # One file per project you created
        ...
```

### users.json example

```json
[
  {
    "uuid": "...",
    "full_name": "User Name",
    "email_address": "example@gmail.com",
    "verified_phone_number": "+9xxxxxxxxx"
  }
]
```

## conversations.json Schema

`conversations.json` is a JSON array. Each element represents one conversation and contains:

| Field | Description |
|-------|-------------|
| `uuid` | Unique ID of the conversation |
| `name` | Title of the chat session (often empty) |
| `summary` | AI-generated short summary (often empty) |
| `created_at` | Timestamp when the conversation was started |
| `updated_at` | Timestamp of the last modification |
| `account` | Object with the owning account’s `uuid` |
| `chat_messages` | Array of all messages in the conversation |

### chat_messages[] fields

| Field | Description |
|-------|-------------|
| `uuid` | Unique ID of the message |
| `text` | Plain-text content of the message |
| `content` | Rich / formatted content blocks |
| `sender` | `"human"` or `"assistant"` |
| `created_at` / `updated_at` | Message timestamps |
| `attachments` / `files` | Arrays of attached media or uploaded files |
| `parent_message_uuid` | ID of the preceding message (used to rebuild the conversation tree) |

Empty conversations (no real messages) are common and are filtered out by the script.

## Usage

1. Download your data from Claude.ai (Settings → Privacy → Export data).
2. Extract the ZIP and place `conversations.json` next to the script (or update the path inside the script).
3. Run:

```bash
python process_convos.py
```

Cleaned conversations are written to `./convos/` as numbered JSON files:

```
001_Title_abcdef12.json
```

## Output Format

```json
{
  "id": "...",
  "title": "...",
  "created_at": "...",
  "updated_at": "...",
  "total_turns": 12,
  "turns": [
    {
      "turn": 1,
      "request": "...",
      "response": "...",
      "files": ["optional.pdf"]
    }
  ]
}
```

## Notes

- Only non-empty turns are kept.
- Filenames are sanitized and truncated for filesystem safety.
- The script clears the previous `convos/` directory on each run.
