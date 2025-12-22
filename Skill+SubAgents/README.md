# 🛠️ AI Skills & Sub-Agents Toolkit

This is a collection of "modular brains" for Claude. Instead of giving Claude one giant, messy prompt, we use these **Skills** to give it specific "superpowers" only when it needs them.

Think of a **Skill** as a specialized "Onboarding Guide" for a specific task.

---

## 📂 What’s in the Box?

---

### 🚀 Quick Navigation

*   📂 **[Main Skills Directory](./Skill+SubAgents/)** — *The root folder for all modular extensions.*
*   🤖 **[Agent Definitions](./Skill+SubAgents/agents/)** — *Instructions for the ProjectOrganizer and SkillCreator.*
*   🛰️ **[Qdrant RAG Skill](./Skill+SubAgents/qdrant-rag-skill/)** — *Implementation guide and templates for Vector DBs.*

---

## 🤖 Meet the Agents

### 1. The Project Organizer (`ProjectOrganizer.md`)
**What it does:** Ever have a coding project where all your files are in one folder and the imports are a mess? This agent fixes that. 
- **Superpower:** It looks at your files, suggests a professional folder structure (like putting models in `/models`), and **automatically fixes all the import paths** so the code still runs.
- **When to use:** When your project gets too big and you're tired of manually moving files around.

### 2. The Skill Creator (`SkillCreator.md`)
**What it does:** This is the meta-tool. It’s an agent designed to help *you* build more skills like the ones in this folder.
- **Superpower:** It interviews you about what you want to build, scaffolds the folders for you, and writes the instructions in a way that Claude understands perfectly.
- **Pro Tip:** It uses **"Progressive Disclosure."** This means it keeps the main instructions short so Claude doesn't get confused, but links to bigger files for details.

### 3. Qdrant RAG Skill (`qdrant-rag-skill/`)
**What it does:** This is a pre-built skill for anyone working with **Vector Databases** (specifically Qdrant).
- **Superpower:** It knows the exact code syntax for Qdrant, handles the math for embeddings, and prevents common bugs like "String vs Integer IDs."
- **When to use:** If you're building an AI app that needs to "remember" documents using a database.

---

## 💡 How to Build Your Own Skill
If you want to make a new skill for the class (e.g., a "React Tailwind Expert" or "Latex Formatter"), follow this **3-Level Design**:

1.  **Level 1: The Tag (Metadata):** A short name and description. Claude sees this and says, *"Hey, I should use this!"*
2.  **Level 2: The Brain (`SKILL.md`):** High-level "How-to" instructions. Keep it under 5,000 words.
3.  **Level 3: The Toolkit:** 
    *   `/scripts`: Python scripts for hard tasks (math, file conversion).
    *   `/references`: Large documents or API manuals.
    *   `/assets`: Templates or boilerplate code.

---

## 🚀 Quick Start for Classmates

1.  **To Organize Code:** Open `agents/ProjectOrganizer.md`, copy the content, and paste it into a fresh Claude chat. Point it at your messy project folder.
2.  **To Create a New Skill:** Use the **Skill Creator** agent. It will guide you through the `init_skill.py` workflow to make sure your skill is formatted correctly.
3.  **To Use RAG:** If you're doing a data project, look at the `qdrant-rag-skill` folder for "best practice" code templates so you don't have to start from scratch.

---

### ⚠️ Pro-Rules for the Repo
*   **No "You":** When writing instructions for skills, don't say "You should do this." Instead, say "Analyze the file" or "Extract the data." It makes the AI more reliable.
*   **Stay Lean:** Don't put huge lists of data in the `SKILL.md`. Put them in the `references/` folder. It saves "Context Window" space!
