# Qwen Code Chat Recovery

Extract clean chat history from Qwen Code JSONL logs (single file, wildcard, or whole directory).

## Why

Qwen Code sessions are stored as JSONL. These tools convert them into readable USER / ASSISTANT text files so you can resume the conversation elsewhere.

## Scripts

### 1. `extract_qwen_code.bat`
Basic chat extractor (USER + ASSISTANT turns only).

### 2. `extract_qwen_subagent_logs.bat`
Advanced extractor that also captures:
- Tool calls (`TOOL CALL [name]: ...`)
- Sub-agent traces
- Full content arrays

Works for both main chat logs and sub-agent files (e.g. `agent-a1f2d38.jsonl`).

## Usage

1. Run either `.bat`
2. Drag a `.jsonl` file, a wildcard (`*.jsonl`), or a folder
3. Each file is saved next to the original as `.txt`

## Output format

```
USER: ...

----------------------------------------

ASSISTANT: ...

----------------------------------------

TOOL CALL [tool_name]: {...}
```

Thoughts are filtered out. Only real user + model turns (and tool calls in the sub-agent script) are kept.