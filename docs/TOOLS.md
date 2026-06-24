# VSCode Agent Tools Reference

This document provides a comprehensive reference of all available tools that can be used in custom VSCode agents. Tools control what actions an agent can perform and what context it can access.

## Tool Specification

In your agent's YAML frontmatter, specify tools as an array:

```yaml
tools: ['search', 'codebase', 'edit/editFiles', 'runCommands']
```

You can also use wildcards:
- `*` - All available tools
- `mcp-server-name/*` - All tools from a specific MCP server

## Tool Categories

### Read-Only Tools (Analysis & Planning)

These tools allow agents to read and analyze code without making changes. Ideal for planning, review, and analysis agents.

| Tool | Description | Common Use Cases |
|------|-------------|------------------|
| `search` | Search for text patterns across the workspace | Find function definitions, locate specific code patterns |
| `codebase` | Access and analyze entire codebase structure | Understand project organization, identify dependencies |
| `usages` | Find all references to functions, classes, variables | Impact analysis, refactoring planning, dependency tracking |
| `fetch` | Retrieve content from web URLs | Research APIs, fetch documentation, gather external context |
| `githubRepo` | Search and analyze GitHub repositories | Research similar implementations, find code examples |
| `findTestFiles` | Locate test files in the workspace | Understand test coverage, plan test strategies |
| `problems` | Access diagnostics and error messages | Identify issues, understand error patterns |
| `testFailure` | Get details about failed test runs | Debug test failures, understand test issues |
| `changes` | View git diff of current changes | Review modifications, understand what changed |
| `terminalLastCommand` | Get output from the last terminal command | Analyze command results without re-running |
| `terminalSelection` | Access text selected in terminal | Work with specific terminal output |

### Editing Tools (Code Modification)

These tools allow agents to create and modify files. Use for implementation and refactoring agents.

| Tool | Description | Common Use Cases |
|------|-------------|------------------|
| `edit/editFiles` | Edit existing files in the workspace | Implement features, fix bugs, refactor code |
| `new` | Create new files and directories | Scaffold new components, add new modules |

### Execution Tools (Running Code & Commands)

These tools execute code, tests, and commands. Use for testing, debugging, and automation agents.

| Tool | Description | Common Use Cases |
|------|-------------|------------------|
| `runCommands` | Execute terminal commands | Build projects, run scripts, install dependencies |
| `runTests` | Execute test suites | Validate changes, run test coverage, debug test failures |
| `runTasks` | Execute VSCode tasks from tasks.json | Run build tasks, start dev servers, execute workflows |
| `runNotebooks` | Execute Jupyter notebook cells | Run data analysis, test notebook code |

### UI & Navigation Tools

These tools interact with VSCode's UI and provide navigation capabilities.

| Tool | Description | Common Use Cases |
|------|-------------|------------------|
| `vscodeAPI` | Access VSCode extension API | Advanced workspace manipulation, custom integrations |
| `extensions` | Query and interact with installed extensions | Check extension availability, leverage extension features |
| `openSimpleBrowser` | Open URLs in VSCode's embedded browser | Preview web content, view documentation |

### Search & Results Tools

Specialized search tools for different contexts.

| Tool | Description | Common Use Cases |
|------|-------------|------------------|
| `search/searchResults` | Access search view results | Work with existing search results |
| `search/codebase` | Semantic code search across workspace | Find relevant code by intent, not just text |

### External Service Tools

Tools for integrating with external services and APIs.

| Tool | Description | Common Use Cases |
|------|-------------|------------------|
| `github` | Interact with GitHub API | Create issues, review PRs, manage branches |
| `microsoft.docs.mcp` | Access Microsoft documentation | Look up best practices, API references |
| `giphy` | Search and retrieve GIFs | Add visual elements (rarely used in engineering agents) |

### MCP (Model Context Protocol) Tools

MCP servers provide custom tool sets. Reference them by server name:

| Pattern | Description | Example |
|---------|-------------|---------|
| `mcp-server-name/*` | All tools from an MCP server | `mcp-atlassian/*`, `mcp-jira/*` |
| `mcp-server-name/toolName` | Specific tool from MCP server | `mcp-database/query` |

## Recommended Tool Sets by Agent Type

### Planning Agents (Read-Only)
```yaml
tools: ['codebase', 'search', 'usages', 'fetch', 'githubRepo', 'findTestFiles', 'problems']
```
**Purpose:** Analyze and create plans without modifying code

### Implementation Agents (Full Access)
```yaml
tools: ['codebase', 'search', 'edit/editFiles', 'new', 'runTests', 'runCommands', 'problems']
```
**Purpose:** Execute changes, create files, validate implementations

### Debug Agents (Diagnostic + Edit)
```yaml
tools: ['problems', 'testFailure', 'terminalLastCommand', 'search', 'codebase', 'edit/editFiles', 'runTests', 'runCommands', 'usages']
```
**Purpose:** Identify and fix bugs with full diagnostic access

### Code Review Agents (Read-Only + Diagnostics)
```yaml
tools: ['codebase', 'search', 'usages', 'changes', 'problems', 'testFailure', 'fetch']
```
**Purpose:** Review code quality without making changes

### Test Agents (Execution Focus)
```yaml
tools: ['findTestFiles', 'runTests', 'testFailure', 'codebase', 'search', 'edit/editFiles', 'problems']
```
**Purpose:** Run, analyze, and fix tests

### Git/Version Control Agents
```yaml
tools: ['changes', 'github', 'runCommands', 'terminalLastCommand', 'codebase', 'search']
```
**Purpose:** Manage version control operations

### Build Automation Agents
```yaml
tools: ['runCommands', 'runTasks', 'runTests', 'terminalLastCommand', 'problems', 'codebase']
```
**Purpose:** Execute build pipelines and validation

### Architecture Agents (Documentation Focus)
```yaml
tools: ['codebase', 'search', 'usages', 'fetch', 'new', 'problems']
```
**Purpose:** Create architecture documentation and diagrams

## Tool Selection Guidelines

### When to Restrict Tools

1. **Planning Phase:** Use read-only tools to prevent premature code changes
2. **Review Phase:** Limit to analysis tools to ensure objective review
3. **Learning/Mentoring:** Read-only tools encourage understanding before action
4. **Documentation:** Minimal tools focused on reading and creating docs

### When to Grant Full Access

1. **Implementation:** Need edit, create, and execution tools
2. **Debugging:** Need diagnostics, editing, and test execution
3. **Automation:** Need command execution and file manipulation
4. **Refactoring:** Need code analysis, editing, and validation

### Security Considerations

- **Principle of Least Privilege:** Grant only tools needed for the agent's purpose
- **Read-Only First:** Start with read-only tools; add editing tools only when necessary
- **Command Execution:** Be cautious with `runCommands` - it can execute arbitrary shell commands
- **External Access:** Tools like `fetch` and `github` access external resources

## Tool Combinations for Workflows

### Research → Plan → Implement
1. **Research Agent:** `['fetch', 'githubRepo', 'search', 'codebase']`
2. **Planning Agent:** `['codebase', 'search', 'usages', 'problems']`
3. **Implementation Agent:** `['edit/editFiles', 'new', 'runTests', 'codebase']`

### Debug → Fix → Validate
1. **Debug Agent:** `['problems', 'testFailure', 'terminalLastCommand', 'search', 'codebase']`
2. **Fix Agent:** `['edit/editFiles', 'codebase', 'search', 'runTests']`
3. **Validation Agent:** `['runTests', 'testFailure', 'problems', 'changes']`

### Review → Improve → Document
1. **Review Agent:** `['changes', 'problems', 'codebase', 'search']`
2. **Improvement Agent:** `['edit/editFiles', 'codebase', 'usages', 'runTests']`
3. **Documentation Agent:** `['codebase', 'search', 'new', 'fetch']`

## Examples from Agent Files

### Minimal Planning Agent
```yaml
---
description: "Generate implementation plans without making changes"
tools: ['codebase', 'search', 'usages']
---
```

### Full-Featured Debug Agent
```yaml
---
description: "Systematic debugging with diagnostic and editing capabilities"
tools: ['problems', 'testFailure', 'terminalLastCommand', 'search', 'codebase', 'edit/editFiles', 'runTests', 'runCommands', 'usages']
model: "Claude Sonnet 4"
---
```

### Test-Focused Agent
```yaml
---
description: "Run tests and analyze failures"
tools: ['findTestFiles', 'runTests', 'testFailure', 'problems', 'codebase']
model: "GPT-4.1"
---
```

## Additional Resources

- **VSCode Chat Tools Documentation:** https://code.visualstudio.com/docs/copilot/chat/chat-tools
- **Custom Agents Guide:** https://code.visualstudio.com/docs/copilot/customization/custom-agents
- **MCP Specification:** https://modelcontextprotocol.io

## Notes

- Tool availability may vary based on VSCode version and installed extensions
- MCP tools require appropriate MCP servers to be configured
- Some tools may have performance implications on large codebases
- Tool combinations can be customized per agent based on specific needs
