# Gemini CLI Chat Recovery

Extract clean chat history from Gemini CLI JSONL logs.

## Why

Gemini CLI stores sessions as JSONL. This tool turns them into readable USER / ASSISTANT markdown so you can continue the conversation in any other agent.

## Usage

1. Run `extract_gemini_cli.bat`
2. Drag the `.jsonl` file or paste its path
3. Output is saved next to the input as `.md`

## Output format

```
USER: ...

ASSISTANT: ...
```

Only non-empty user and gemini turns are kept.