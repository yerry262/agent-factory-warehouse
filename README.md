# Agent Factory Warehouse 🏭

A curated library of VSCode custom agents for software engineering workflows. Create, customize, and deploy AI agents specialized for debugging, testing, git operations, code validation, and more.

## 🚀 Quick Start

```powershell
# Copy agents to your project
New-Item -ItemType Directory -Path .\.github\agents -Force
Copy-Item C:\path\to\agent-factory-warehouse\agents\Debugging\Debug.agent.md .\.github\agents\
Copy-Item C:\path\to\agent-factory-warehouse\agents\Testing\TestRunner.agent.md .\.github\agents\
Copy-Item C:\path\to\agent-factory-warehouse\agents\GitSync\GitSync.agent.md .\.github\agents\
```

Or use the installation script:

```powershell
C:\path\to\agent-factory-warehouse\scripts\InstallAgents.ps1 -TargetRepo "C:\path\to\your\project"
```

## 📋 Available Agents

### Planning & Architecture

| Agent | Description | Key Tools |
|-------|-------------|-----------|
| **Planner** | Generate detailed implementation plans without making code changes | `codebase`, `search`, `usages`, `fetch` |
| **Architect** | Design system architecture and create technical documentation with diagrams | `codebase`, `search`, `fetch`, `new` |

**Use when:** Starting new features, refactoring, making architectural decisions

---

### Debugging

| Agent | Description | Key Tools |
|-------|-------------|-----------|
| **Debug** | Systematic debugging across any language or framework | `problems`, `testFailure`, `edit/editFiles`, `runTests` |

**Use when:** Investigating bugs, test failures, runtime errors, performance issues

---

### Testing

| Agent | Description | Key Tools |
|-------|-------------|-----------|
| **TestRunner** | Execute and analyze test suites across any testing framework | `runTests`, `testFailure`, `problems`, `codebase` |

**Use when:** Running tests, validating changes, analyzing test failures

---

### Code Quality

| Agent | Description | Key Tools |
|-------|-------------|-----------|
| **CodeValidator** | Code quality validation and standards enforcement (read-only) | `codebase`, `search`, `problems`, `changes` |

**Use when:** Reviewing code quality, checking for issues, enforcing standards

---

### Version Control

| Agent | Description | Key Tools |
|-------|-------------|-----------|
| **GitSync** | Git operations: commit, push, pull, branch management | `changes`, `runCommands`, `terminalLastCommand` |

**Use when:** Committing changes, managing branches, pushing to remote

---

### Build & CI/CD

| Agent | Description | Key Tools |
|-------|-------------|-----------|
| **RegressionBuilder** | Build execution and regression testing automation | `runCommands`, `runTests`, `runTasks`, `testFailure` |

**Use when:** Running builds, checking for regressions, CI/CD validation

---

## 🎯 Agent Workflows

Agents are designed to work together with handoff functionality:

### Full Development Workflow

```
@Planner → @agent (implementation) → @TestRunner → @GitSync
```

1. Plan feature with **Planner**
2. Implement with standard **@agent**
3. Validate with **TestRunner**
4. Commit with **GitSync**

### Debug & Fix Workflow

```
@Debug → @TestRunner → @GitSync
```

1. Debug issue with **Debug**
2. Validate fix with **TestRunner**
3. Commit fix with **GitSync**

### Quality Assurance Workflow

```
@CodeValidator → @Debug → @TestRunner → @RegressionBuilder
```

1. Review with **CodeValidator**
2. Fix issues with **Debug**
3. Run tests with **TestRunner**
4. Full regression with **RegressionBuilder**

## 📁 Repository Structure

```
agent-factory-warehouse/
├── agents/                    # Production-ready agents
│   ├── Planning/             # Planning and architecture agents
│   │   ├── Planner.agent.md
│   │   └── Architect.agent.md
│   ├── Debugging/            # Debug agents
│   │   └── Debug.agent.md
│   ├── Testing/              # Test execution agents
│   │   └── TestRunner.agent.md
│   ├── Validation/           # Code quality agents
│   │   └── CodeValidator.agent.md
│   ├── GitSync/              # Version control agents
│   │   └── GitSync.agent.md
│   └── BuildAutomation/      # Build and CI/CD agents
│       └── RegressionBuilder.agent.md
├── templates/                 # Agent templates and examples
│   ├── BasicAgentTemplate.agent.md
│   ├── ReadOnlyAgentTemplate.agent.md
│   ├── FullAccessAgentTemplate.agent.md
│   ├── ExampleDebugAgent.agent.md
│   └── ExamplePlanningAgent.agent.md
├── docs/                      # Documentation
│   ├── USAGE.md              # How to use agents in your projects
│   ├── CONTRIBUTING.md       # How to create and contribute agents
│   └── TOOLS.md              # Complete VSCode agent tools reference
├── scripts/                   # Utility scripts
│   └── InstallAgents.ps1     # Automated agent installation
├── CHANGELOG.md              # Version history and updates
├── LICENSE                   # MIT License
└── README.md                 # This file
```

## 🛠️ Installation Methods

### Method 1: Direct Copy (Recommended)

Copy specific agents to your project:

```powershell
# Create agents directory
New-Item -ItemType Directory -Path .\.github\agents -Force

# Copy specific agents
Copy-Item C:\path\to\agent-factory-warehouse\agents\Debugging\Debug.agent.md .\.github\agents\
Copy-Item C:\path\to\agent-factory-warehouse\agents\Testing\TestRunner.agent.md .\.github\agents\

# Or copy entire categories
Copy-Item C:\path\to\agent-factory-warehouse\agents\Debugging\*.agent.md .\.github\agents\

# Or copy all agents
Copy-Item C:\path\to\agent-factory-warehouse\agents\*\*.agent.md .\.github\agents\
```

### Method 2: Automated Script

Use the installation script for easier management:

```powershell
# Install all agents
.\scripts\InstallAgents.ps1 -TargetRepo "C:\path\to\your\project" -InstallAll

# Install specific categories
.\scripts\InstallAgents.ps1 -TargetRepo "C:\path\to\your\project" -Categories @("Debugging", "Testing", "GitSync")

# Update existing agents
.\scripts\InstallAgents.ps1 -TargetRepo "C:\path\to\your\project" -InstallAll -Force
```

### Method 3: Symbolic Links (Advanced)

For automatic updates (requires admin privileges):

```powershell
New-Item -ItemType SymbolicLink `
    -Path ".\.github\agents\Debug.agent.md" `
    -Target "C:\path\to\agent-factory-warehouse\agents\Debugging\Debug.agent.md"
```

## 💡 Usage Examples

### Planning a Feature

```
@Planner I need to add user authentication with JWT tokens
```

### Debugging an Issue

```
@Debug The application crashes when submitting the payment form
```

### Running Tests

```
@TestRunner Run all tests and provide detailed failure analysis
```

### Validating Code Quality

```
@CodeValidator Review the recent changes in src/services/ for quality issues
```

### Committing Changes

```
@GitSync Review and commit the authentication feature with appropriate message
```

### Build & Regression Testing

```
@RegressionBuilder Run full build and regression test suite
```

## 🎨 Creating Custom Agents

Start with a template from `templates/`:

1. Choose appropriate template (Basic, ReadOnly, or FullAccess)
2. Copy to your project's `.github/agents/` directory
3. Customize YAML frontmatter and instructions
4. Test in your project

See `docs/CONTRIBUTING.md` for detailed guidelines.

## 📚 Documentation

- **[USAGE.md](docs/USAGE.md)** - Complete usage guide with installation methods and examples
- **[CONTRIBUTING.md](docs/CONTRIBUTING.md)** - Guidelines for creating and contributing agents
- **[TOOLS.md](docs/TOOLS.md)** - Comprehensive reference of all available VSCode agent tools
- **[CHANGELOG.md](CHANGELOG.md)** - Version history and updates

## 🌟 Key Features

### Framework-Agnostic

All agents are designed to work across any programming language and framework. Whether you're working with JavaScript, Python, Java, C#, Go, or any other language, these agents adapt to your project.

### Language-Universal Tools

Agents use universal debugging principles, testing patterns, and development workflows that apply regardless of your tech stack.

### Intelligent Handoffs

Agents can hand off to each other, creating seamless workflows:
- Debug → TestRunner → GitSync
- Planner → Implementation → CodeValidator
- RegressionBuilder → Debug (on failures)

### Read-Only vs Full-Access

- **Planning agents** (Planner, Architect, CodeValidator) are read-only for safety
- **Implementation agents** (Debug) have edit capabilities
- **Automation agents** (TestRunner, GitSync, RegressionBuilder) have execution permissions

### Comprehensive Tool Access

Each agent has carefully selected tools appropriate for its purpose. See `docs/TOOLS.md` for complete tool reference.

## 🔄 Updating Agents

Check `CHANGELOG.md` for updates and new features.

To update agents in your project:

```powershell
# Manual update
Remove-Item .\.github\agents\*.agent.md
Copy-Item C:\path\to\agent-factory-warehouse\agents\*\*.agent.md .\.github\agents\

# Or use script
.\scripts\InstallAgents.ps1 -TargetRepo "C:\path\to\your\project" -InstallAll -Force
```

## 🤝 Contributing

We welcome contributions! See [CONTRIBUTING.md](docs/CONTRIBUTING.md) for guidelines.

To contribute a new agent:

1. Review existing agents and templates
2. Create your agent in the appropriate `agents/` subdirectory
3. Follow naming conventions (CamelCase)
4. Test thoroughly
5. Update README.md and CHANGELOG.md
6. Submit a pull request

## 📖 Additional Resources

- [VSCode Custom Agents Documentation](https://code.visualstudio.com/docs/copilot/customization/custom-agents)
- [VSCode Chat Tools Reference](https://code.visualstudio.com/docs/copilot/chat/chat-tools)
- [GitHub Copilot Documentation](https://docs.github.com/en/copilot)

## 📄 License

MIT License - see [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

Built for the VSCode and GitHub Copilot community. Inspired by software engineering best practices and the need for specialized AI agents in development workflows.

---

**Made with ❤️ for developers who want AI agents that actually understand their workflow.**
