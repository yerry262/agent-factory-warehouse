# Contributing to Agent Factory Warehouse

Thank you for your interest in contributing to the Agent Factory Warehouse! This guide will help you create high-quality agents that benefit the entire community.

## Table of Contents

- [Getting Started](#getting-started)
- [Agent Creation Guidelines](#agent-creation-guidelines)
- [Agent File Structure](#agent-file-structure)
- [Quality Standards](#quality-standards)
- [Testing Your Agent](#testing-your-agent)
- [Submission Process](#submission-process)
- [Agent Categories](#agent-categories)

## Getting Started

### Prerequisites

1. VSCode with GitHub Copilot
2. Understanding of custom agents (see [VSCode docs](https://code.visualstudio.com/docs/copilot/customization/custom-agents))
3. Familiarity with YAML and Markdown
4. Review existing agents in `agents/` directory

### Review Resources

Before creating an agent:

1. **Read `docs/TOOLS.md`** - Understand available tools
2. **Review `templates/`** - See agent templates and examples
3. **Study existing agents** - Learn from production agents
4. **Check `agents/` categories** - See where your agent fits

## Agent Creation Guidelines

### 1. Identify the Need

Ask yourself:
- What problem does this agent solve?
- Is there already a similar agent?
- What makes this agent unique?
- Who will use this agent?

### 2. Choose the Right Category

Place your agent in the appropriate directory:

- **`Planning/`** - Analysis, planning, architecture (read-only)
- **`Debugging/`** - Bug investigation and fixing
- **`Testing/`** - Test execution and analysis
- **`Validation/`** - Code quality and standards
- **`GitSync/`** - Version control operations
- **`BuildAutomation/`** - Build and CI/CD tasks

If none fit, propose a new category in your pull request.

### 3. Use Appropriate Templates

Start with a template from `templates/`:

- **`BasicAgentTemplate.agent.md`** - General purpose agent
- **`ReadOnlyAgentTemplate.agent.md`** - Analysis/planning agents
- **`FullAccessAgentTemplate.agent.md`** - Implementation agents

Or reference examples:
- **`ExampleDebugAgent.agent.md`** - Full-featured debug agent
- **`ExamplePlanningAgent.agent.md`** - Read-only planning agent

## Agent File Structure

### File Naming

Use CamelCase for agent file names:

```
Good:
- Debug.agent.md
- CodeValidator.agent.md
- TestRunner.agent.md
- GitSync.agent.md

Bad:
- debug-agent.agent.md
- code_validator.agent.md
- test-runner.agent.md
```

### YAML Frontmatter

Required fields:

```yaml
---
description: "Brief description shown in chat placeholder"
name: "AgentName"
tools: ['tool1', 'tool2', 'tool3']
model: "Claude Sonnet 4" or "GPT-4.1"
---
```

Optional fields:

```yaml
target: "vscode"  # Default is vscode
argument-hint: "Hint text for users"
handoffs:
  - label: "Button Text"
    agent: "TargetAgentName"
    prompt: "Pre-filled prompt"
    send: false  # or true for auto-submit
```

**Important Notes:**
- `version` field is NOT supported by VSCode - use CHANGELOG.md instead
- Agent names in handoffs must match exact agent names
- Tool names must be valid (see `docs/TOOLS.md`)

### Instruction Body

Use clear Markdown structure:

```markdown
# Agent Name

[Brief description of agent's purpose]

## Core Principles

- Principle 1
- Principle 2
- Principle 3

## [Main sections describing agent behavior]

## Best Practices

[Specific guidelines]

## Remember

[Key takeaways]
```

## Quality Standards

### Instructions Quality

✅ **Good Instructions:**
- Clear and specific
- Actionable guidance
- Examples included
- Structured with headings
- Appropriate length (not too brief, not too verbose)

❌ **Poor Instructions:**
- Vague or ambiguous
- Overly complex
- Missing examples
- Unstructured wall of text
- Too short or too long

### Tool Selection

✅ **Good Tool Selection:**
- Minimal necessary tools
- Appropriate for agent's purpose
- Read-only for planning agents
- Edit tools only when needed
- Execution tools for automation agents

❌ **Poor Tool Selection:**
- All tools (`*`) without justification
- Execution tools on read-only agents
- Missing essential tools
- Unnecessary tools

### Model Selection

**Claude Sonnet 4:**
- Complex analysis tasks
- Detailed planning
- Code review and validation
- Architecture design
- Comprehensive debugging

**GPT-4.1:**
- Fast execution tasks
- Simple automation
- Git operations
- Test running
- Build execution

### Handoffs

✅ **Good Handoffs:**
- Natural workflow progression
- Clear prompt context
- Appropriate target agents
- Helpful but optional

❌ **Poor Handoffs:**
- Circular handoffs
- Missing target agents
- Vague prompts
- Too many handoffs

## Testing Your Agent

### 1. Local Testing

Copy your agent to a test repository:

```powershell
Copy-Item .\agents\YourCategory\YourAgent.agent.md C:\path\to\test-repo\.github\agents\
```

### 2. Functional Testing

Test your agent by:

1. **Basic Usage:** Can it handle simple requests?
2. **Tool Usage:** Does it use tools appropriately?
3. **Edge Cases:** How does it handle unusual inputs?
4. **Handoffs:** Do handoffs work correctly?
5. **Cross-Language:** Does it work with different languages/frameworks?

### 3. Quality Checks

- [ ] YAML frontmatter is valid
- [ ] Tools are appropriate for the task
- [ ] Instructions are clear and actionable
- [ ] Examples are included where helpful
- [ ] Handoffs reference existing agents
- [ ] Agent works in different project types
- [ ] No obvious errors or issues

### 4. Documentation Review

- [ ] Description is clear and concise
- [ ] Instructions explain what the agent does
- [ ] Tool usage is documented
- [ ] Best practices are included
- [ ] Response format is specified (if applicable)

## Submission Process

### 1. Prepare Your Agent

1. Create your agent in appropriate `agents/` subdirectory
2. Follow naming conventions (CamelCase)
3. Test thoroughly in multiple projects
4. Document any special considerations

### 2. Update Documentation

Add your agent to README.md agent catalog:

```markdown
| AgentName | Category | Description | Key Tools |
|-----------|----------|-------------|-----------|
| YourAgent | YourCategory | Brief description | tool1, tool2 |
```

### 3. Update CHANGELOG

Add entry to `CHANGELOG.md`:

```markdown
## [Unreleased]

### Added
- **YourAgent** (Category): Brief description of what it does and why it's useful
```

### 4. Create Pull Request

Include in your PR:

- Agent file in correct directory
- README.md update
- CHANGELOG.md update
- Description of agent's purpose
- Example usage
- Testing notes

### 5. PR Description Template

```markdown
## Agent: YourAgent

**Category:** YourCategory
**Purpose:** [What problem does this solve?]

### Description
[Detailed description of the agent]

### Key Features
- Feature 1
- Feature 2
- Feature 3

### Testing
[How you tested it, what projects you used]

### Example Usage
[Example of using the agent with expected behavior]

### Checklist
- [ ] Agent follows naming conventions
- [ ] YAML frontmatter is valid
- [ ] Tools are appropriate
- [ ] Instructions are clear
- [ ] Tested in multiple projects
- [ ] README.md updated
- [ ] CHANGELOG.md updated
```

## Agent Categories

### Planning Agents

**Purpose:** Analysis, planning, architecture, design
**Tools:** Read-only (`codebase`, `search`, `usages`, `fetch`)
**Model:** Claude Sonnet 4

**Examples:**
- Planner - Implementation planning
- Architect - Architecture design

### Debugging Agents

**Purpose:** Bug identification and fixing
**Tools:** Diagnostics + Edit (`problems`, `testFailure`, `edit/editFiles`)
**Model:** Claude Sonnet 4

**Examples:**
- Debug - Systematic debugging

### Testing Agents

**Purpose:** Test execution and analysis
**Tools:** Execution + Analysis (`runTests`, `testFailure`, `problems`)
**Model:** GPT-4.1

**Examples:**
- TestRunner - Test execution

### Validation Agents

**Purpose:** Code quality and standards
**Tools:** Read-only + Diagnostics (`codebase`, `problems`, `changes`)
**Model:** Claude Sonnet 4

**Examples:**
- CodeValidator - Code quality review

### GitSync Agents

**Purpose:** Version control operations
**Tools:** Git + Commands (`changes`, `runCommands`)
**Model:** GPT-4.1

**Examples:**
- GitSync - Git operations

### Build Automation Agents

**Purpose:** Build and CI/CD tasks
**Tools:** Execution + Diagnostics (`runCommands`, `runTests`, `runTasks`)
**Model:** GPT-4.1

**Examples:**
- RegressionBuilder - Build and regression testing

## Best Practices for Contributors

### Do's

✅ Test your agent thoroughly
✅ Provide clear, actionable instructions
✅ Include examples in instructions
✅ Use appropriate tools for the task
✅ Follow existing naming conventions
✅ Document special considerations
✅ Make agents framework-agnostic when possible

### Don'ts

❌ Grant excessive tool permissions
❌ Create overly complex agents
❌ Duplicate existing agent functionality
❌ Use vague or ambiguous instructions
❌ Skip testing in real projects
❌ Forget to update documentation

## Code of Conduct

- Be respectful and constructive
- Focus on quality over quantity
- Help improve existing agents
- Share knowledge and best practices
- Provide helpful feedback on PRs

## Questions?

- Review existing agents for examples
- Check `docs/TOOLS.md` for tool reference
- Read VSCode custom agents documentation
- Open an issue for discussion before major contributions

## Thank You!

Your contributions help make agent-factory-warehouse a valuable resource for the entire VSCode community. Every agent you create helps developers work more efficiently and effectively.
