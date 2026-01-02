# 🛠️ AI Skills & Sub-Agents Toolkit

This is a collection of "modular brains" for Claude. Instead of giving Claude one giant, messy prompt, we use these **Skills** to give it specific "superpowers" only when it needs them.

Think of a **Skill** as a specialized "Onboarding Guide" for a specific task.
/plugin marketplace add anthropics/skills
---

## 📂 What’s in the Box?

---

### 🚀 Quick Navigation

*   📂 **[Main Skills Directory](./Skill+SubAgents/)** — *The root folder for all modular extensions.*
*   🤖 **[Agent Definitions](./Skill+SubAgents/agents/)** — *Instructions for the ProjectOrganizer.*
*   🛠️ **[Skills Directory](./Skill+SubAgents/skills/)** — *Modular skills including Skill Creator and Qdrant RAG.*
*   🌐 **[Next.js 16 Skills](./Skill+SubAgents/skills/claude-nextjs-skills/)** — *Comprehensive skill bundle for Next.js 16 with proven performance improvements.*

---

## 🤖 Meet the Agents

### 1. The Project Organizer (`ProjectOrganizer.md`)
**What it does:** Ever have a coding project where all your files are in one folder and the imports are a mess? This agent fixes that.
- **Superpower:** It looks at your files, suggests a professional folder structure (like putting models in `/models`), and **automatically fixes all the import paths** so the code still runs.
- **When to use:** When your project gets too big and you're tired of manually moving files around.

### 2. The Skill Creator (`skills/skill-creator/`)
**What it does:** This is the meta-tool. It's a skill designed to help *you* build more skills like the ones in this folder.
- **Superpower:** It interviews you about what you want to build, scaffolds the folders for you, and writes the instructions in a way that Claude understands perfectly.
- **Pro Tip:** It uses **"Progressive Disclosure."** This means it keeps the main instructions short so Claude doesn't get confused, but links to bigger files for details.

### 3. Qdrant RAG Skill (`skills/qdrant-rag-skill/`)
**What it does:** This is a pre-built skill for anyone working with **Vector Databases** (specifically Qdrant).
- **Superpower:** It knows the exact code syntax for Qdrant, handles the math for embeddings, and prevents common bugs like "String vs Integer IDs."
- **When to use:** If you're building an AI app that needs to "remember" documents using a database.

---

## 🚀 Complete Skills Directory

This repository contains a comprehensive collection of specialized skills for Claude, organized by category:

**Next.js 16 Skills** (Located in `skills/claude-nextjs-skills/`):
Proven to dramatically improve Claude's performance on Next.js evaluations (78% for Haiku 4.5, 76% for Sonnet 4.5).
- [`nextjs-app-router-fundamentals`](./skills/claude-nextjs-skills/nextjs-app-router-fundamentals/SKILL.md)
- [`nextjs-16-async-apis`](./skills/claude-nextjs-skills/nextjs-16-async-apis/SKILL.md)
- [`nextjs-16-proxy-patterns`](./skills/claude-nextjs-skills/nextjs-16-proxy-patterns/SKILL.md)
- [`nextjs-server-client-components`](./skills/claude-nextjs-skills/nextjs-server-client-components/SKILL.md)
- [`nextjs-advanced-routing`](./skills/claude-nextjs-skills/nextjs-advanced-routing/SKILL.md)
- [`nextjs-anti-patterns`](./skills/claude-nextjs-skills/nextjs-anti-patterns/SKILL.md)
- [`nextjs-dynamic-routes-params`](./skills/claude-nextjs-skills/nextjs-dynamic-routes-params/SKILL.md)
- [`nextjs-pathname-id-fetch`](./skills/claude-nextjs-skills/nextjs-pathname-id-fetch/SKILL.md)
- [`nextjs-server-navigation`](./skills/claude-nextjs-skills/nextjs-server-navigation/SKILL.md)
- [`nextjs-use-search-params-suspense`](./skills/claude-nextjs-skills/nextjs-use-search-params-suspense/SKILL.md)
- [`nextjs-client-cookie-pattern`](./skills/claude-nextjs-skills/nextjs-client-cookie-pattern/SKILL.md)
- [`vercel-ai-sdk`](./skills/claude-nextjs-skills/vercel-ai-sdk/SKILL.md)

**Authentication & Security Skills:**
- [`better-auth-jwt-jwks`](./skills/better-auth-jwt-jwks/SKILL.md) - Expert skill for implementing Better Auth with JWT tokens and JWKS for secure authentication
- [`docusaurus-auth`](./skills/docusaurus-auth/SKILL.md) - Skill for implementing authentication in Docusaurus static sites
- [`fastapi-jwt-auth`](./skills/fastapi-jwt-auth/SKILL.md) - Expert skill for implementing JWT-based authentication in FastAPI applications
- [`session-management-ssg-ssr`](./skills/session-management-ssg-ssr/SKILL.md) - Expert skill for implementing session management in SSG/SSR contexts

**AI & Chat Skills:**
- [`chatkit`](./skills/chatkit/chatkit-backend.skill.md) - Skill for creating a production-ready ChatKit Python backend

**AI Search & Retrieval Skills:**
- [`qdrant-rag-skill`](./skills/qdrant-rag-skill/SKILL.md) - Robust Qdrant vector database integration with RAG (Retrieval Augmented Generation) systems

**Development Tool Skills:**
- [`skill-creator`](./skills/skill-creator/SKILL.md) - Guide for creating effective skills that extend Claude's capabilities

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
2.  **To Create a New Skill:** Use the **Skill Creator** skill in the `skills/` directory. It will guide you through the `init_skill.py` workflow to make sure your skill is formatted correctly.
3.  **To Use RAG:** If you're doing a data project, look at the `skills/qdrant-rag-skill` folder for "best practice" code templates so you don't have to start from scratch.
4.  **For Next.js 16 Development:** Use the skills in `skills/claude-nextjs-skills/` to dramatically improve Claude's Next.js development capabilities.

---

### ⚠️ Pro-Rules for the Repo
*   **No "You":** When writing instructions for skills, don't say "You should do this." Instead, say "Analyze the file" or "Extract the data." It makes the AI more reliable.
*   **Stay Lean:** Don't put huge lists of data in the `SKILL.md`. Put them in the `references/` folder. It saves "Context Window" space!
