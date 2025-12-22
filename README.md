# LevelUpSpeckit-Plus - Student Guide

Welcome to **LevelUpSpeckit-Plus**! This repository contains a collection of tools, scripts, and techniques designed to enhance your productivity during hackathons and coding projects using AI agents (Qwen, Claude, etc.).

## 📚 Table of Contents

- [Introduction](#introduction)
- [Core Components](#core-components)
  - [Agent Coordination](#agent-coordination)
  - [Espeak Audio Notifications](#espeak-audio-notifications)
  - [Token Refresh System](#token-refresh-system)
  - [Skills & Sub-Agents](#skills--sub-agents)
- [Quick Start Guide](#quick-start-guide)


## Introduction

This repository serves as a comprehensive toolkit for students working with AI agents in coding projects. It includes solutions for multi-agent coordination, audio notifications, token management, and specialized AI skills to enhance productivity during hackathons and development sprints.

## Quick Start Guide

### For New Students

1. **Start with Agent Coordination**: If you need to use multiple AI agents (Qwen, Claude) in your project, read `AgentCoordination/README.md` first.

2. **Set up Audio Notifications**: Follow instructions in `Espeak/Readme.md` to set up audio feedback for your workflow.

3. **Configure Token Refresh**: Use the scripts in `RefreshToken/` to automate token management if you're using Claude Code Router.

4. **Explore Skills System**: Review `Skill+SubAgents/README.md` to understand how to use specialized AI capabilities.

### Using Specific Tools

- **Multi-Agent Coordination**: Follow the 4-step process in `AgentCoordination/README.md`
- **Audio Notifications**: Copy scripts to `.specify/scripts/bash/` and call them from your commands
- **Token Refresh**: Run `python refresh_token.py` or use with VSCode code runner
- **Project Organization**: Copy `ProjectOrganizer.md` content and use as a Claude prompt
- **Skill Creation**: Use `SkillCreator.md` to generate new specialized agents

## Troubleshooting

- **Agent switching issues**: See `AgentCoordination/README.md` for the workaround
- **Token expiration**: Use the automated refresh script in `RefreshToken/`
- **Skill conflicts**: Follow the progressive disclosure pattern to keep instructions concise

## Additional Resources

- [AIChat Template](AgentCoordination/AIChat/README.md) - For multi-agent communication
- [Qdrant RAG Implementation Guide](Skill+SubAgents/qdrant-rag-skill/README.md) - For vector database integration
- [CCR Shortcuts](RefreshToken/Readme.md) - Quick reference for Claude Code Router commands

---

**Important**: Each subdirectory contains its own README file with detailed instructions. Please read the specific README files in each directory for complete setup and usage information.