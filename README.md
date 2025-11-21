# Agent Factory Warehouse

A powerful and extensible AI agent factory system that generates custom AI agent modules based on user requests. Build, configure, and orchestrate specialized agents for coding, debugging, planning, building, and more.

## 🌟 Features

- **Core Factory Engine**: Centralized system for creating and managing AI agents
- **Pre-built Agent Templates**: Ready-to-use agents for common tasks:
  - **CodingAgent**: Code generation, refactoring, and analysis
  - **DebuggingAgent**: Bug detection, error analysis, and fix suggestions
  - **PlanningAgent**: Project planning, task breakdown, and timeline estimation
  - **BuildingAgent**: Build automation, CI/CD pipelines, and deployment
- **Extensible Framework**: Easily create custom agent types
- **Modular Workflows**: Orchestrate multiple agents in complex workflows
- **Configuration Management**: Flexible configuration system with validation
- **Agent Registry**: Dynamic registration and discovery of agent types

## 📦 Installation

Clone the repository:

```bash
git clone https://github.com/yerry262/agent-factory-warehouse.git
cd agent-factory-warehouse
```

The system is written in Python and has minimal dependencies. No additional packages are required for basic usage.

Optional dependencies:
```bash
pip install pyyaml  # For YAML configuration support
```

## 🚀 Quick Start

### Basic Usage

```python
from agent_factory import AgentFactory
from agent_factory.templates import CodingAgent, DebuggingAgent

# Create the factory
factory = AgentFactory()

# Register agent types
factory.register_agent_type("coding", CodingAgent)
factory.register_agent_type("debugging", DebuggingAgent)

# Create an agent
coder = factory.create_agent(
    agent_type="coding",
    name="my_coder",
    config={"languages": ["Python", "JavaScript"]}
)

# Execute a task
result = coder.execute(
    task="Create a function to calculate factorial",
    context={"language": "Python"}
)

print(result["code"])
```

### Using Workflows

```python
from agent_factory.workflows import WorkflowBuilder, WorkflowManager

# Create a workflow
workflow = (WorkflowBuilder("development", "Full development cycle")
    .add_step("planner", "Plan the project architecture")
    .add_step("coder", "Implement the core functionality")
    .add_step("debugger", "Review and identify issues")
    .add_step("builder", "Set up CI/CD pipeline")
    .build())

# Execute the workflow
workflow_manager = WorkflowManager()
workflow_manager.create_workflow(
    workflow["name"],
    workflow["description"],
    workflow["steps"]
)

result = workflow_manager.execute_workflow("development", agents)
```

### Creating Custom Agents

```python
from agent_factory import BaseAgent
from typing import Dict, Any, List, Optional

class MyCustomAgent(BaseAgent):
    def get_capabilities(self) -> List[str]:
        return ["custom_capability_1", "custom_capability_2"]
    
    def execute(self, task: str, context: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        # Implement your agent logic here
        result = {
            "success": True,
            "task": task,
            "output": "Custom agent output"
        }
        self.log_execution(task, result)
        return result

# Register and use your custom agent
factory.register_agent_type("custom", MyCustomAgent)
custom_agent = factory.create_agent("custom", "my_custom_agent")
```

## 📚 Documentation

### Agent Templates

#### CodingAgent
Specialized in code generation, refactoring, and analysis.

**Capabilities:**
- Code generation from specifications
- Code refactoring
- Code quality analysis
- Syntax checking
- Code optimization
- Documentation generation
- Unit test generation

**Configuration:**
```python
config = {
    "languages": ["Python", "JavaScript", "Java", "C++", "Go", "Rust"],
    "style_guide": "PEP8"  # or "Google", "Airbnb", etc.
}
```

#### DebuggingAgent
Specialized in finding and fixing bugs, error analysis.

**Capabilities:**
- Error message analysis
- Stack trace parsing
- Bug identification
- Fix suggestions
- Root cause analysis
- Debugging strategy recommendations
- Bug tracking

**Configuration:**
```python
config = {
    "strategies": ["print_debugging", "breakpoint_analysis", "log_analysis"],
    "max_bugs_tracked": 1000
}
```

#### PlanningAgent
Specialized in project planning and task breakdown.

**Capabilities:**
- Project decomposition
- Task breakdown
- Timeline estimation
- Resource planning
- Dependency mapping
- Risk assessment
- Milestone definition
- Roadmap creation

**Configuration:**
```python
config = {
    "methodology": "agile"  # or "waterfall", "kanban", "scrum"
}
```

#### BuildingAgent
Specialized in build automation and CI/CD.

**Capabilities:**
- Build configuration
- CI/CD pipeline creation
- Dependency management
- Automated testing setup
- Deployment automation
- Container orchestration
- Build optimization
- Artifact management

**Configuration:**
```python
config = {
    "build_tools": ["Maven", "Gradle", "npm", "pip", "Docker"],
    "platforms": ["GitHub Actions", "Jenkins", "GitLab CI", "CircleCI"]
}
```

### Core Components

#### AgentFactory
The main factory class for creating and managing agents.

**Key Methods:**
- `create_agent(agent_type, name, config)`: Create a new agent
- `get_agent(name)`: Retrieve an agent by name
- `list_agents()`: List all active agents
- `register_agent_type(agent_type, agent_class)`: Register a new agent type
- `execute_agent_task(name, task, context)`: Execute a task with an agent

#### WorkflowManager
Orchestrate multiple agents in workflows.

**Key Methods:**
- `create_workflow(name, description, steps)`: Define a new workflow
- `execute_workflow(name, agents, initial_context)`: Execute a workflow
- `list_workflows()`: List all workflows
- `validate_workflow(name, available_agents)`: Validate a workflow

#### WorkflowBuilder
Fluent API for building workflows.

**Key Methods:**
- `add_step(agent, task, context)`: Add a step to the workflow
- `add_sequential_step(agent, task)`: Add a sequential step
- `add_parallel_step(agent, task)`: Add a parallel step
- `build()`: Build the workflow configuration

### Configuration

#### Loading Configuration

```python
from agent_factory.config import ConfigLoader

# Load from file
config = ConfigLoader.load_from_file("config.json")

# Get default configuration
default_config = ConfigLoader.get_default_config()

# Save configuration
ConfigLoader.save_to_file(config, "config.json", format="json")
```

#### Validating Configuration

```python
from agent_factory.config import ConfigValidator

# Validate agent configuration
validation = ConfigValidator.validate_agent_config(config, "coding")
if validation["valid"]:
    print("Configuration is valid!")
else:
    print("Errors:", validation["errors"])
```

## 🎯 Examples

Run the example scripts to see the system in action:

```bash
# Basic usage example
python examples/basic_usage.py

# Workflow example
python examples/workflow_example.py

# Custom agent example
python examples/custom_agent.py
```

## 🏗️ Architecture

```
agent_factory/
├── core/                 # Core factory engine
│   ├── base_agent.py    # Abstract base class for agents
│   ├── factory.py       # Main factory class
│   └── registry.py      # Agent type registry
├── templates/           # Pre-built agent templates
│   ├── coding_agent.py
│   ├── debugging_agent.py
│   ├── planning_agent.py
│   └── building_agent.py
├── workflows/           # Workflow orchestration
│   ├── workflow_manager.py
│   └── workflow_builder.py
├── config/              # Configuration management
│   ├── config_loader.py
│   └── config_validator.py
└── utils/               # Utility functions
    ├── logger.py
    └── serializer.py
```

## 🔧 Advanced Usage

### Agent Serialization

```python
from agent_factory.utils import serialize_agent, deserialize_agent

# Serialize an agent
json_state = serialize_agent(agent)

# Deserialize an agent
restored_agent = deserialize_agent(json_state, CodingAgent)
```

### Workflow Templates

```python
from agent_factory.workflows import WorkflowTemplates

# Use pre-defined templates
dev_workflow = WorkflowTemplates.full_development_workflow().build()
bug_fix_workflow = WorkflowTemplates.bug_fix_workflow().build()
deployment_workflow = WorkflowTemplates.deployment_workflow().build()
```

### Custom Configuration

```python
# Create custom configuration
custom_config = {
    "factory": {
        "name": "MyFactory",
        "max_agents": 50
    },
    "agents": {
        "coding": {
            "languages": ["Python", "Go"],
            "style_guide": "custom"
        }
    }
}

# Validate and use
validation = ConfigValidator.validate_factory_config(custom_config)
```

## 🤝 Contributing

Contributions are welcome! To add a new agent type:

1. Create a new class inheriting from `BaseAgent`
2. Implement `get_capabilities()` and `execute()` methods
3. Register your agent with the factory
4. Add tests and documentation

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🎓 Use Cases

- **Software Development**: Automate coding, testing, and deployment workflows
- **Code Review**: Automated code analysis and improvement suggestions
- **Project Planning**: Break down complex projects into manageable tasks
- **Bug Fixing**: Systematic debugging and issue resolution
- **CI/CD Setup**: Automated build and deployment pipeline configuration
- **Documentation**: Generate comprehensive project documentation
- **Learning**: Understand software development best practices through AI assistance

## 🚀 Roadmap

- [ ] Add more pre-built agent templates (Testing, Documentation, Security)
- [ ] Implement parallel workflow execution
- [ ] Add web interface for agent management
- [ ] Support for agent communication and collaboration
- [ ] Integration with popular AI/LLM APIs
- [ ] Real-time agent monitoring and metrics
- [ ] Agent marketplace for sharing custom agents

## 📧 Contact

For questions, issues, or suggestions, please open an issue on GitHub.

---

Made with ❤️ by the Agent Factory Warehouse team
