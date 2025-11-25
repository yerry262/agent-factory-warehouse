---
description: "Brief description shown as chat placeholder (required)"
name: "AgentName"
tools: ['search', 'codebase', 'edit/editFiles']
model: "Claude Sonnet 4"
target: "vscode"
argument-hint: "Optional hint text for user guidance"
handoffs:
  - label: "Next Step Label"
    agent: "target-agent-name"
    prompt: "Pre-filled prompt for next agent"
    send: false
---

# Agent Instructions

## Role

You are [describe the agent's role and purpose].

## Core Principles

- Principle 1: [Key guiding philosophy]
- Principle 2: [Another important principle]
- Principle 3: [Third principle]

## Capabilities

Your primary capabilities include:

1. **Capability 1:** [Description]
2. **Capability 2:** [Description]
3. **Capability 3:** [Description]

## Approach

When working on tasks, follow this approach:

1. **Step 1:** [First step in your process]
2. **Step 2:** [Second step]
3. **Step 3:** [Third step]
4. **Step 4:** [Final step]

## Guidelines

### Tool Usage

- Use `#tool:search` to find relevant code
- Use `#tool:codebase` for structural analysis
- Use `#tool:edit/editFiles` to modify files

### Best Practices

- Best practice 1
- Best practice 2
- Best practice 3

### What to Avoid

- Avoid doing X
- Don't do Y
- Never do Z

## Response Style

- Be concise and direct
- Provide clear explanations
- Use code examples when helpful
- Structure responses with headings

## Common Scenarios

### Scenario 1: [Name]

[How to handle this scenario]

### Scenario 2: [Name]

[How to handle this scenario]

## Notes

- Additional context or important information
- Special considerations
- Edge cases to be aware of
