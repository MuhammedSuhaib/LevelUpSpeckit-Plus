# Using Multiple Agents in a SpecKit-Plus Project

## The Problem (Important)

When **SpecKit-Plus** initializes a project, it asks **which agent you will use**.

This choice is **one-time only**.

* If you select **Gemini**, you cannot use **Qwen or Claude later**
* `/sp.*` commands will **not work** for other agents
* Many students already faced this issue in **Hackathon 1**

This is a **SpecKit-Plus limitation**, not your mistake.

---

## The Workaround (Correct Way)

To use **more than one agent**, follow these steps.

---

## Step 1: Create a New SpecKit-Plus Project

* Initialize a **new** SpecKit-Plus project
* Select the agent you want to **add as a co-agent**

  * Example: Qwen or Claude

---

## Step 2: Copy Agent Files to Your Main Project

From the new project, copy:

* The agent folder

  * Example:

    ```
    .qwen
    ```
* The agent system instruction file

  * Example:

    ```
    Qwen.md
    ```

    or

    ```
    Claude.md
    ```

Paste them into your **main project**.

> These files are critical — they contain system instructions generated during `speckit-plus init`.

---

## Step 3: Agent Onboarding (Very Important)

When you start using the new agent:

* Tell it to **crawl the entire project**
* Explain:

  * What the project is about
  * Current phase status
  * Existing structure

### Phase / ADR continuity rule

* The agent must **continue the sequence**
* Example:

  * Last PHR = `005`
  * New agent must create `006`
* Never reset numbering

---

## Step 4: Multi-Agent Orchestration (Optional but Recommended)

You can now:

* Divide tasks between agents
* Assign work clearly
* Avoid overlap

Use this template to coordinate agents:

👉 **[AIChat Template](AIChat/README.md)**

This creates a **bridge** between agents and preserves context.

---

## Summary

* SpecKit-Plus allows **one agent at init**
* Multi-agent use requires a **manual workaround**
* Copy:

  * Agent folder (`.qwen`, `.claude`, etc.)
  * Agent `.md` system file
* Onboard the agent properly
* Maintain phase / ADR sequence
* Use AIChat for coordination

---
