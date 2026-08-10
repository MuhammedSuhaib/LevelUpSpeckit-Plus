# Qwen Code Chat Recovery

Extract clean chat history from Qwen Code JSONL logs (single file, wildcard, or whole directory).

## Why

Qwen Code sessions are stored as JSONL. This tool converts them into readable USER / ASSISTANT text files so you can resume the conversation elsewhere.

## Usage

1. Run `extract_qwen_code.bat`
2. Drag a `.jsonl` file, a wildcard (`*.jsonl`), or a folder
3. Each file is saved next to the original as `.txt`

## Output format

```
USER: ...

ASSISTANT: ...
```

Thoughts are filtered out. Only real user + model turns are kept.