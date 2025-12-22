## Multi-Agent Coordination File (Qwen ↔ Claude)

### Purpose

This file enables **two AI agents to work inside one project** by sharing context, tasks, and decisions.

It acts as a **handoff + coordination layer** between:

* **Qwen** (Alibaba Cloud)
* **Claude** (Anthropic)

---

### How it works

1. Both agents are given a **system instruction** to:

   * Read this file regularly
   * Append updates when needed

2. If an agent encounters a task that is:

   * Outside its responsibility
   * Better handled by the other agent

   It **writes the task here** instead of guessing or blocking.

3. The other agent:

   * Detects the new entry
   * Picks up the task
   * Responds in a new thread

---

### What this file is used for

* Task delegation between agents
* Context persistence across sessions
* Cross-agent debugging
* Preventing duplicated work
* Long-running project memory

---

### Rules for agents

* Do **not** modify or delete previous threads
* Always add a new numbered thread
* Clearly state:

  * Date
  * Task / issue
  * Action taken or question asked
* Close each thread explicitly

---

### Thread format

```md
## Chat Thread #N: Task Title
**Date:** YYYY-MM-DD
**From:** Qwen | Claude
**To:** Qwen | Claude
**Status:** Open | Resolved

**Message:**
Task description or handoff details.

[End of Thread #N]
```

---

### Why this matters in hackathons

* No context loss
* Agents don’t fight or overlap
* Faster problem resolution
* Clean responsibility boundaries

Both agents stay productive **without human micromanagement**.

---

### Summary

> One project
> Two agents
> Shared brain

My opinion: this is a **proper multi-agent architecture pattern**, not a chat log.
