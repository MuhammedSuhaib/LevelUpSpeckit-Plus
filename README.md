# LevelUpSpeckit-Plus - Student Guide

Welcome to **LevelUpSpeckit-Plus**! This repository contains a collection of tools, scripts, and techniques designed to enhance your productivity during hackathons and coding projects using AI agents (Qwen, Claude, etc.).


## Introduction

This repository serves as a comprehensive toolkit for students working with AI agents in coding projects. It includes solutions for multi-agent coordination, audio notifications, token management, and specialized AI skills to enhance productivity during hackathons and development sprints.

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

**Important**: Each subdirectory contains its own README file with detailed instructions. Please read the specific README files in each directory for complete setup and usage information.