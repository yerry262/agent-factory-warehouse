# Changelog

All notable changes to Agent Factory Warehouse will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added

**Smart Contracts:**
- **SolidityMaster** - Expert Solidity smart contract development, auditing, and debugging agent. Specializes in writing secure smart contracts, identifying vulnerabilities, gas optimization, and comprehensive testing. Includes deep knowledge of DeFi protocols, security patterns, and common attack vectors.

## [1.0.0] - 2025-11-24

### 🎉 Initial Release

This is the first release of Agent Factory Warehouse - a curated library of VSCode custom agents for software engineering workflows.

### Added

#### Production Agents

**Planning & Architecture:**
- **Planner** - Generate detailed implementation plans without making code changes. Read-only agent for thorough analysis and planning.
- **Architect** - Design system architecture and create technical documentation with Mermaid diagrams. Focus on high-level design decisions.

**Debugging:**
- **Debug** - Systematic debugging agent for any language or framework. Methodical approach to identifying and resolving bugs with full diagnostic and editing capabilities.

**Testing:**
- **TestRunner** - Execute and analyze test suites across any testing framework. Fast execution with detailed failure analysis.

**Code Quality:**
- **CodeValidator** - Code quality validation and standards enforcement. Read-only agent that provides comprehensive code review and recommendations.

**Version Control:**
- **GitSync** - Git operations including commit, push, pull, and branch management. Handles all version control workflows with conventional commit messages.

**Build & CI/CD:**
- **RegressionBuilder** - Build execution and regression testing automation. Runs builds, detects regressions, and provides comprehensive validation reports.

#### Agent Templates

- **BasicAgentTemplate.agent.md** - General purpose agent template with standard structure
- **ReadOnlyAgentTemplate.agent.md** - Template for analysis and planning agents (no code modification)
- **FullAccessAgentTemplate.agent.md** - Template for implementation agents with full capabilities
- **ExampleDebugAgent.agent.md** - Complete example of a debugging agent with best practices
- **ExamplePlanningAgent.agent.md** - Complete example of a planning agent with detailed instructions

#### Documentation

- **README.md** - Comprehensive overview with quick start guide, agent catalog, and usage examples
- **docs/USAGE.md** - Complete usage guide with installation methods, agent workflows, and troubleshooting
- **docs/CONTRIBUTING.md** - Guidelines for creating and contributing agents, quality standards, and submission process
- **docs/TOOLS.md** - Comprehensive reference of all available VSCode agent tools with descriptions and use cases

#### Utilities

- **scripts/InstallAgents.ps1** - PowerShell script for automated agent installation with category selection and update capabilities

#### Repository Structure

```
agent-factory-warehouse/
├── agents/
│   ├── Planning/
│   ├── Debugging/
│   ├── Testing/
│   ├── Validation/
│   ├── GitSync/
│   └── BuildAutomation/
├── templates/
├── docs/
├── scripts/
└── CHANGELOG.md
```

### Features

- **Framework-Agnostic Agents** - All agents work across any programming language and framework
- **Intelligent Handoffs** - Agents can hand off to each other for seamless workflows
- **Comprehensive Tool Selection** - Each agent has carefully selected tools appropriate for its purpose
- **Read-Only vs Full-Access** - Proper separation between planning/analysis and implementation agents
- **Production-Ready** - All agents thoroughly documented and tested
- **Easy Installation** - Multiple installation methods (direct copy, script, symlinks)
- **Customizable** - Templates and examples for creating custom agents

### Workflows

Agents support comprehensive development workflows:

- **Planning → Implementation → Testing → Git** - Full feature development cycle
- **Debug → Test → Git** - Bug fixing workflow
- **Validate → Debug → Test → Build** - Quality assurance workflow
- **Architect → Plan → Implement** - Architecture-first development

### Notes

- All agents use CamelCase naming convention (e.g., `Debug.agent.md`, `GitSync.agent.md`)
- Agents reference each other in handoffs, so best practice is to install complete workflow sets
- Designed for local repository usage - copy agents to `.github/agents/` in your projects
- Compatible with VSCode with GitHub Copilot extension

---

## [Unreleased]

### Planned

- Additional specialized agents (Security, Performance, Documentation)
- Agent marketplace/catalog UI
- Automated agent testing framework
- Language/framework-specific agent variants
- Integration examples and tutorials
- Community-contributed agents

---

## Version History

- **[1.0.0]** - 2025-11-24 - Initial release with 7 production agents, templates, and documentation

---

## How to Update

When new versions are released:

### Manual Update

```powershell
# Navigate to agent-factory-warehouse
cd C:\path\to\agent-factory-warehouse

# Pull latest changes
git pull origin main

# Update agents in your projects
Remove-Item C:\path\to\your\project\.github\agents\*.agent.md
Copy-Item .\agents\*\*.agent.md C:\path\to\your\project\.github\agents\
```

### Script Update

```powershell
# Update agent-factory-warehouse
cd C:\path\to\agent-factory-warehouse
git pull origin main

# Update agents in your project
.\scripts\InstallAgents.ps1 -TargetRepo "C:\path\to\your\project" -InstallAll -Force
```

---

For detailed information about each release, see the sections above.
For usage instructions, see [docs/USAGE.md](docs/USAGE.md).
For contributing guidelines, see [docs/CONTRIBUTING.md](docs/CONTRIBUTING.md).
