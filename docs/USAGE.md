# How to Use Agent Factory Agents

This guide explains how to use agents from the Agent Factory Warehouse in your local repositories.

## Quick Start

### Copy Agents to Your Repository

The simplest way to use agents is to copy them to your repository's `.github/agents/` directory:

```powershell
# Navigate to your target repository
cd C:\path\to\your\project

# Create the agents directory
New-Item -ItemType Directory -Path .\.github\agents -Force

# Copy specific agent category
Copy-Item C:\path\to\agent-factory-warehouse\agents\Debugging\*.agent.md .\.github\agents\

# Or copy multiple categories
Copy-Item C:\path\to\agent-factory-warehouse\agents\Debugging\*.agent.md .\.github\agents\
Copy-Item C:\path\to\agent-factory-warehouse\agents\Testing\*.agent.md .\.github\agents\
Copy-Item C:\path\to\agent-factory-warehouse\agents\GitSync\*.agent.md .\.github\agents\

# Or copy all agents
Copy-Item C:\path\to\agent-factory-warehouse\agents\*\*.agent.md .\.github\agents\
```

### Verify Agents Are Available

1. Open your repository in VSCode
2. Open the Copilot Chat panel
3. Click the agent selector dropdown
4. You should see all copied agents listed

## Usage Methods

### Method 1: Direct Copy (Recommended for Local Use)

**Pros:**
- Simple and straightforward
- No dependencies on external repos
- Fast to set up
- Full control over agent versions

**Cons:**
- Need to manually update agents
- Duplicates files across projects

**Steps:**
```powershell
# From your project root
New-Item -ItemType Directory -Path .\.github\agents -Force
Copy-Item path\to\agent-factory-warehouse\agents\Debugging\Debug.agent.md .\.github\agents\
```

### Method 2: Scripted Installation (Fastest)

Use the provided PowerShell script for automated installation:

```powershell
# Run the installation script
C:\path\to\agent-factory-warehouse\scripts\InstallAgents.ps1 -TargetRepo "C:\path\to\your\project"

# Install specific categories
C:\path\to\agent-factory-warehouse\scripts\InstallAgents.ps1 `
    -TargetRepo "C:\path\to\your\project" `
    -Categories @("Debugging", "Testing", "GitSync")

# Install all agents
C:\path\to\agent-factory-warehouse\scripts\InstallAgents.ps1 `
    -TargetRepo "C:\path\to\your\project" `
    -InstallAll
```

### Method 3: Symbolic Links (Advanced)

Create symlinks for automatic updates:

```powershell
# Create symlink to entire agents directory
New-Item -ItemType SymbolicLink `
    -Path ".\.github\agents" `
    -Target "C:\path\to\agent-factory-warehouse\agents"

# Or create symlinks for specific agents
New-Item -ItemType Directory -Path .\.github\agents -Force
New-Item -ItemType SymbolicLink `
    -Path ".\.github\agents\Debug.agent.md" `
    -Target "C:\path\to\agent-factory-warehouse\agents\Debugging\Debug.agent.md"
```

**Note:** Requires administrator privileges on Windows.

## Agent Categories

### Planning
- **Planner** - Generate detailed implementation plans
- **Architect** - Design system architecture and documentation

**Use when:** Starting new features, refactoring, architectural decisions

### Debugging
- **Debug** - Systematic debugging across any language

**Use when:** Investigating bugs, test failures, runtime errors

### Testing
- **TestRunner** - Execute and analyze test suites

**Use when:** Running tests, validating changes, checking coverage

### Validation
- **CodeValidator** - Code quality and standards enforcement

**Use when:** Reviewing code, checking for issues, enforcing standards

### Git Operations
- **GitSync** - Git commit, push, pull, branch management

**Use when:** Version control operations, committing changes, managing branches

### Build Automation
- **RegressionBuilder** - Build execution and regression testing

**Use when:** Running builds, checking for regressions, CI/CD validation

## Recommended Agent Combinations

### Full Development Workflow
```powershell
Copy-Item C:\path\to\agent-factory-warehouse\agents\Planning\*.agent.md .\.github\agents\
Copy-Item C:\path\to\agent-factory-warehouse\agents\Debugging\*.agent.md .\.github\agents\
Copy-Item C:\path\to\agent-factory-warehouse\agents\Testing\*.agent.md .\.github\agents\
Copy-Item C:\path\to\agent-factory-warehouse\agents\Validation\*.agent.md .\.github\agents\
Copy-Item C:\path\to\agent-factory-warehouse\agents\GitSync\*.agent.md .\.github\agents\
Copy-Item C:\path\to\agent-factory-warehouse\agents\BuildAutomation\*.agent.md .\.github\agents\
```

### Minimal Setup (Debug + Test + Git)
```powershell
Copy-Item C:\path\to\agent-factory-warehouse\agents\Debugging\Debug.agent.md .\.github\agents\
Copy-Item C:\path\to\agent-factory-warehouse\agents\Testing\TestRunner.agent.md .\.github\agents\
Copy-Item C:\path\to\agent-factory-warehouse\agents\GitSync\GitSync.agent.md .\.github\agents\
```

### Quality Focus (Validation + Testing + Build)
```powershell
Copy-Item C:\path\to\agent-factory-warehouse\agents\Validation\CodeValidator.agent.md .\.github\agents\
Copy-Item C:\path\to\agent-factory-warehouse\agents\Testing\TestRunner.agent.md .\.github\agents\
Copy-Item C:\path\to\agent-factory-warehouse\agents\BuildAutomation\RegressionBuilder.agent.md .\.github\agents\
```

## Using Agents

### Selecting an Agent

1. Open VSCode Copilot Chat
2. Click the agent dropdown (defaults to `@agent`)
3. Select your desired agent (e.g., `@Debug`, `@Planner`, `@TestRunner`)

### Agent Handoffs

Agents are configured with handoff workflows. After an agent completes its task, you'll see handoff buttons:

**Example workflow:**
1. Use `@Debug` to fix a bug
2. Click "Run Tests" → switches to `@TestRunner`
3. Tests pass → Click "Commit Fix" → switches to `@GitSync`
4. Git operations complete → workflow done!

### Example Usage

**Planning a new feature:**
```
@Planner I need to add user authentication with JWT tokens
```

**Debugging an issue:**
```
@Debug The application crashes when submitting the form
```

**Running tests:**
```
@TestRunner Run all tests and report results
```

**Validating code quality:**
```
@CodeValidator Review the recent changes for quality issues
```

**Committing changes:**
```
@GitSync Commit these changes with appropriate message
```

**Building and testing:**
```
@RegressionBuilder Run full build and regression tests
```

## Updating Agents

When agent-factory-warehouse releases new versions:

### Manual Update

```powershell
# Delete old agents
Remove-Item .\.github\agents\*.agent.md

# Copy updated agents
Copy-Item C:\path\to\agent-factory-warehouse\agents\*\*.agent.md .\.github\agents\
```

### Scripted Update

```powershell
C:\path\to\agent-factory-warehouse\scripts\InstallAgents.ps1 `
    -TargetRepo "C:\path\to\your\project" `
    -InstallAll `
    -Force
```

### Check for Updates

Check the agent-factory-warehouse `CHANGELOG.md` for version updates and new features.

## Customizing Agents

You can customize copied agents for your specific needs:

1. Copy the agent to your `.github/agents/` directory
2. Edit the `.agent.md` file
3. Modify:
   - Description
   - Tools available
   - Instructions
   - Handoff targets

**Example customization:**
```yaml
---
description: "Custom debug agent for our Python project"
name: "DebugPython"
tools: ['problems', 'testFailure', 'search', 'codebase', 'edit/editFiles', 'runTests']
model: "Claude Sonnet 4"
---

# Custom Python Debug Agent

[Your custom instructions focusing on Python-specific debugging...]
```

## Troubleshooting

### Agents Don't Appear in Dropdown

1. Verify `.github/agents/` directory exists
2. Ensure `.agent.md` files are in the directory (not subdirectories)
3. Check file extensions are exactly `.agent.md`
4. Reload VSCode window (Ctrl+Shift+P → "Developer: Reload Window")

### Handoffs Don't Work

- Handoff target agents must also be in `.github/agents/`
- Verify agent names match exactly (case-sensitive)
- Check YAML frontmatter syntax is correct

### Agent Not Behaving as Expected

1. Check the agent's instruction content
2. Verify tools list includes needed tools
3. Review tool reference in `docs/TOOLS.md`
4. Consider customizing the agent for your use case

## Best Practices

### Organization

- Keep `.github/agents/` directory clean
- Only install agents you actually use
- Remove unused agents to reduce clutter

### Maintenance

- Periodically check for agent updates
- Review CHANGELOG.md for improvements
- Test new agent versions before full deployment

### Customization

- Document any customizations you make
- Keep custom agents in version control
- Share useful customizations back to agent-factory-warehouse

### Workflow

- Start with planning agents (@Planner, @Architect)
- Use implementation agents for coding
- Validate with quality agents (@CodeValidator, @TestRunner)
- Finish with git agents (@GitSync)

## Additional Resources

- **Agent Templates:** `templates/` directory for creating custom agents
- **Tool Reference:** `docs/TOOLS.md` for all available tools
- **Contributing Guide:** `docs/CONTRIBUTING.md` for adding new agents
- **VSCode Docs:** https://code.visualstudio.com/docs/copilot/customization/custom-agents

## Support

For issues or questions:
1. Check documentation in `docs/` directory
2. Review existing agent implementations
3. Refer to VSCode custom agents documentation
4. Open an issue in agent-factory-warehouse repository
