# LevelUpSpeckit-Plus - Student Guide

Welcome to **LevelUpSpeckit-Plus**! This repository contains a collection of tools, scripts, and techniques designed to enhance your productivity during hackathons and coding projects using AI agents (Qwen, Claude, etc.).

## Introduction

This repository serves as a comprehensive toolkit for students working with AI agents in coding projects. It includes solutions for multi-agent coordination, audio notifications, token management, and specialized AI skills to enhance productivity during hackathons and development sprints. The tools are designed to work with Claude Code Router, Qwen, and other AI agents.

## Table of Contents

- [LevelUpSpeckit-Plus - Student Guide](#levelupspeckit-plus---student-guide)
  - [Introduction](#introduction)
  - [Table of Contents](#table-of-contents)
  - [Directory Structure](#directory-structure)
  - [Quick Start Guide](#quick-start-guide)
    - [For New Students](#for-new-students)
    - [Using Specific Tools](#using-specific-tools)
  - [Hackathon II Context](#hackathon-ii-context)
  - [Detailed Tool Descriptions](#detailed-tool-descriptions)
    - [Multi-Agent Coordination](#multi-agent-coordination)
    - [Audio Notifications](#audio-notifications)
    - [Token Refresh](#token-refresh)
    - [AI Skills & Sub-Agents](#ai-skills--sub-agents)
  - [Advanced Usage](#advanced-usage)

## Directory Structure

```
LevelUpSpeckit-Plus/
├── AgentCoordination/     # Multi-agent coordination techniques
├── Espeak/               # Audio notification scripts
├── LastClassCode/        # Example code from previous classes
├── RefreshToken/         # Token management for Claude Code Router
├── Skill+SubAgents/      # AI skills and sub-agent templates
├── .claude/              # Claude-specific configurations
└── Hackathon II - Todo Spec-Driven Development.md # Main hackathon document
```

## Quick Start Guide

### For New Students

1. **Start with Agent Coordination**: If you need to use multiple AI agents (Qwen, Claude) in your project, read [AgentCoordination/README.md](./AgentCoordination/README.md) first.

2. **Set up Audio Notifications**: Follow instructions in [Espeak/Readme.md](./Espeak/Readme.md) to set up audio feedback for your workflow.

3. **Configure Token Refresh**: Use the scripts in [RefreshToken](./RefreshToken/Readme.md) to automate token management if you're using Claude Code Router.

4. **Explore SubAgents and Skills**: Review [Skill+SubAgents/README.md](./Skill+SubAgents/README.md) to understand how to use specialized AI capabilities.

### Using Specific Tools

- **Multi-Agent Coordination**: Follow the 4-step process in [AgentCoordination/README.md](./AgentCoordination/README.md)
- **Audio Notifications**: Copy scripts to `.specify/scripts/bash/` and call them from your commands
- **Token Refresh**: Run [python refresh_token.py](./RefreshToken/refresh_token.py) or use with VSCode code runner
- **Project Organization**: Copy [Skill+SubAgents/agents/ProjectOrganizer.md](./Skill+SubAgents/agents/ProjectOrganizer.md) content and use as a Claude prompt
- **Skill Creation**: Use the skill creator in [Skill+SubAgents/skills/skill-creator/](./Skill+SubAgents/skills/skill-creator/) to generate new specialized skills

---

## Hackathon II 
Hackathon II pdf is also added [Hackathon II](./Hackathon%20II%20-%20Todo%20Spec-Driven%20Development.md)

## Detailed Tool Descriptions

### Multi-Agent Coordination
Located in `AgentCoordination/`, this directory contains techniques for using multiple AI agents (Qwen, Claude, etc.) within a single project. Because SpecKit-Plus allows only one agent at project initialization, this workaround allows students to use multiple agents by creating new projects and copying agent files.

**Key Features:**
- Workaround for SpecKit-Plus single-agent limitation
- Proper onboarding for additional agents
- Multi-agent orchestration templates
- Phase/ADR continuity rules

### Audio Notifications
Located in `Espeak/`, this directory contains scripts for audio notifications that speak messages aloud. This is particularly useful when multitasking and not staring at the terminal.

**Key Features:**
- Cross-platform support (Windows/Linux/macOS)
- Simple integration with existing workflows
- Customizable messages
- Time-saving during hackathons

### Token Refresh
Located in `RefreshToken/`, this directory contains scripts to automatically refresh Qwen access tokens for Claude Code Router. This solves the common problem of token expiration during hackathons.

**Key Features:**
- Automated token refresh (now uses non-interactive mode)
- Automatic CCR config updates
- Service restart capability
- One-command solution

### AI Skills & Sub-Agents
Located in `Skill+SubAgents/`, this directory contains modular skills for Claude that provide specific "superpowers" only when needed. Think of each skill as a specialized "Onboarding Guide" for a specific task.

**Key Components:**
- **Project Organizer**: Automatically organizes project structure and fixes import paths
- **Skill Creator**: Helps create new specialized skills
- **Qdrant RAG Skill**: Pre-built skill for vector database operations
- **Next.js 16 Skills**: Comprehensive set of skills for Next.js 16 development with significant improvements in eval scores
- **Modular Design**: 3-level design approach for maintainability

### All Available Skills
Located in `Skill+SubAgents/skills/`, this repository contains a comprehensive collection of specialized skills for Claude. Each skill provides specific "superpowers" for different domains and technologies.

**Next.js 16 Skills** (Located in `Skill+SubAgents/skills/claude-nextjs-skills/`):
Proven to dramatically improve Claude's performance on Next.js evaluations (78% for Haiku 4.5, 76% for Sonnet 4.5).
- [`nextjs-app-router-fundamentals`](./Skill+SubAgents/skills/claude-nextjs-skills/nextjs-app-router-fundamentals/SKILL.md)
- [`nextjs-16-async-apis`](./Skill+SubAgents/skills/claude-nextjs-skills/nextjs-16-async-apis/SKILL.md)
- [`nextjs-16-proxy-patterns`](./Skill+SubAgents/skills/claude-nextjs-skills/nextjs-16-proxy-patterns/SKILL.md)
- [`nextjs-server-client-components`](./Skill+SubAgents/skills/claude-nextjs-skills/nextjs-server-client-components/SKILL.md)
- [`nextjs-advanced-routing`](./Skill+SubAgents/skills/claude-nextjs-skills/nextjs-advanced-routing/SKILL.md)
- [`nextjs-anti-patterns`](./Skill+SubAgents/skills/claude-nextjs-skills/nextjs-anti-patterns/SKILL.md)
- [`nextjs-dynamic-routes-params`](./Skill+SubAgents/skills/claude-nextjs-skills/nextjs-dynamic-routes-params/SKILL.md)
- [`nextjs-pathname-id-fetch`](./Skill+SubAgents/skills/claude-nextjs-skills/nextjs-pathname-id-fetch/SKILL.md)
- [`nextjs-server-navigation`](./Skill+SubAgents/skills/claude-nextjs-skills/nextjs-server-navigation/SKILL.md)
- [`nextjs-use-search-params-suspense`](./Skill+SubAgents/skills/claude-nextjs-skills/nextjs-use-search-params-suspense/SKILL.md)
- [`nextjs-client-cookie-pattern`](./Skill+SubAgents/skills/claude-nextjs-skills/nextjs-client-cookie-pattern/SKILL.md)
- [`vercel-ai-sdk`](./Skill+SubAgents/skills/claude-nextjs-skills/vercel-ai-sdk/SKILL.md)

**Authentication & Security Skills:**
- [`better-auth-jwt-jwks`](./Skill+SubAgents/skills/better-auth-jwt-jwks/SKILL.md) - Expert skill for implementing Better Auth with JWT tokens and JWKS for secure authentication
- [`docusaurus-auth`](./Skill+SubAgents/skills/docusaurus-auth/SKILL.md) - Skill for implementing authentication in Docusaurus static sites
- [`fastapi-jwt-auth`](./Skill+SubAgents/skills/fastapi-jwt-auth/SKILL.md) - Expert skill for implementing JWT-based authentication in FastAPI applications
- [`session-management-ssg-ssr`](./Skill+SubAgents/skills/session-management-ssg-ssr/SKILL.md) - Expert skill for implementing session management in SSG/SSR contexts

**AI & Chat Skills:**
- [`chatkit`](./Skill+SubAgents/skills/chatkit/chatkit-backend.skill.md) - Skill for creating a production-ready ChatKit Python backend

**AI Search & Retrieval Skills:**
- [`qdrant-rag-skill`](./Skill+SubAgents/skills/qdrant-rag-skill/SKILL.md) - Robust Qdrant vector database integration with RAG (Retrieval Augmented Generation) systems

**Development Tool Skills:**
- [`skill-creator`](./Skill+SubAgents/skills/skill-creator/SKILL.md) - Guide for creating effective skills that extend Claude's capabilities

## Advanced Usage

For advanced users, the repository supports:
- Custom skill creation using the 3-level design approach
- Multi-agent workflows with proper context continuity
- Integration with Claude Code Router for seamless AI agent usage
- Audio feedback systems for improved productivity
- Automated token management to prevent service interruptions

**Important**: Each subdirectory contains its own README file with detailed instructions. Please read the specific README files in each directory for complete setup and usage information.