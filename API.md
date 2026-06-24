# API Documentation

## Table of Contents

1. [Core Components](#core-components)
2. [Agent Templates](#agent-templates)
3. [Workflows](#workflows)
4. [Configuration](#configuration)
5. [Utilities](#utilities)

---

## Core Components

### BaseAgent (Abstract)

**Location:** `agent_factory.core.base_agent`

Abstract base class for all agent types. All custom agents must inherit from this class.

#### Constructor

```python
BaseAgent(name: str, config: Optional[Dict[str, Any]] = None)
```

**Parameters:**
- `name` (str): Unique identifier for the agent
- `config` (dict, optional): Configuration dictionary for the agent

#### Abstract Methods

##### execute()

```python
def execute(self, task: str, context: Optional[Dict[str, Any]] = None) -> Dict[str, Any]
```

Execute the agent's primary task. Must be implemented by subclasses.

**Parameters:**
- `task` (str): Description of the task to perform
- `context` (dict, optional): Additional context information

**Returns:**
- dict: Dictionary containing execution results

##### get_capabilities()

```python
def get_capabilities(self) -> List[str]
```

Return a list of capabilities this agent has.

**Returns:**
- list: List of capability strings

#### Public Methods

##### get_info()

```python
def get_info(self) -> Dict[str, Any]
```

Get information about this agent.

**Returns:**
- dict: Agent information including name, type, capabilities, config, metadata, and execution count

##### get_history()

```python
def get_history(self) -> List[Dict[str, Any]]
```

Get the execution history of this agent.

**Returns:**
- list: List of execution log entries

##### update_config()

```python
def update_config(self, new_config: Dict[str, Any])
```

Update the agent's configuration.

**Parameters:**
- `new_config` (dict): New configuration dictionary

##### export_state()

```python
def export_state(self) -> str
```

Export the agent's state as JSON.

**Returns:**
- str: JSON string representing the agent's state

---

### AgentFactory

**Location:** `agent_factory.core.factory`

Main factory class for creating and managing AI agents.

#### Constructor

```python
AgentFactory()
```

#### Methods

##### register_agent_type()

```python
def register_agent_type(self, agent_type: str, agent_class: Type[BaseAgent])
```

Register a new agent type with the factory.

**Parameters:**
- `agent_type` (str): String identifier for the agent type
- `agent_class` (class): Class that implements BaseAgent

##### create_agent()

```python
def create_agent(self, agent_type: str, name: str, config: Optional[Dict[str, Any]] = None) -> BaseAgent
```

Create a new agent instance.

**Parameters:**
- `agent_type` (str): Type of agent to create (must be registered)
- `name` (str): Unique name for the agent instance
- `config` (dict, optional): Configuration dictionary for the agent

**Returns:**
- BaseAgent: Created agent instance

**Raises:**
- ValueError: If agent_type is not registered or name is already in use

##### get_agent()

```python
def get_agent(self, name: str) -> Optional[BaseAgent]
```

Get an active agent by name.

**Parameters:**
- `name` (str): Name of the agent to retrieve

**Returns:**
- BaseAgent or None: Agent instance or None if not found

##### list_agents()

```python
def list_agents(self) -> List[str]
```

List all active agent names.

**Returns:**
- list: List of active agent names

##### remove_agent()

```python
def remove_agent(self, name: str) -> bool
```

Remove an agent from active agents.

**Parameters:**
- `name` (str): Name of the agent to remove

**Returns:**
- bool: True if removed, False if not found

##### execute_agent_task()

```python
def execute_agent_task(self, name: str, task: str, context: Optional[Dict[str, Any]] = None) -> Dict[str, Any]
```

Execute a task using a specific agent.

**Parameters:**
- `name` (str): Name of the agent to use
- `task` (str): Task description
- `context` (dict, optional): Optional context for the task

**Returns:**
- dict: Task execution result

**Raises:**
- ValueError: If agent is not found

---

### AgentRegistry

**Location:** `agent_factory.core.registry`

Registry for managing available agent types. Implements singleton pattern.

#### Methods

##### register()

```python
def register(self, agent_type: str, agent_class: Type[BaseAgent])
```

Register a new agent type.

**Parameters:**
- `agent_type` (str): String identifier for the agent type
- `agent_class` (class): Class that implements BaseAgent

**Raises:**
- ValueError: If agent_type is already registered
- TypeError: If agent_class doesn't inherit from BaseAgent

##### get()

```python
def get(self, agent_type: str) -> Optional[Type[BaseAgent]]
```

Get an agent class by type.

**Parameters:**
- `agent_type` (str): String identifier for the agent type

**Returns:**
- class or None: Agent class or None if not found

##### list_types()

```python
def list_types(self) -> List[str]
```

List all registered agent types.

**Returns:**
- list: List of registered agent type identifiers

---

## Agent Templates

### CodingAgent

**Location:** `agent_factory.templates.coding_agent`

Agent specialized in code generation, refactoring, and analysis.

#### Capabilities

- `code_generation`
- `code_refactoring`
- `code_analysis`
- `syntax_checking`
- `code_optimization`
- `documentation_generation`
- `unit_test_generation`

#### Configuration

```python
config = {
    "languages": ["Python", "JavaScript", "Java", "C++", "Go", "Rust"],
    "style_guide": "default"  # or "PEP8", "Google", "Airbnb", etc.
}
```

#### Example

```python
agent = CodingAgent("my_coder", config={"languages": ["Python"], "style_guide": "PEP8"})
result = agent.execute("Create a function to sort a list", context={"language": "Python"})
print(result["code"])
```

---

### DebuggingAgent

**Location:** `agent_factory.templates.debugging_agent`

Agent specialized in debugging, error analysis, and bug fixing.

#### Capabilities

- `error_analysis`
- `stack_trace_parsing`
- `bug_identification`
- `fix_suggestion`
- `root_cause_analysis`
- `debugging_strategy_recommendation`
- `bug_tracking`

#### Configuration

```python
config = {
    "strategies": ["print_debugging", "breakpoint_analysis", "log_analysis", "unit_testing"],
    "max_bugs_tracked": 1000
}
```

#### Example

```python
agent = DebuggingAgent("my_debugger")
result = agent.execute(
    "Fix null pointer exception",
    context={"error_type": "NullPointerException", "code": "user.getName()"}
)
print(result["suggested_fixes"])
```

---

### PlanningAgent

**Location:** `agent_factory.templates.planning_agent`

Agent specialized in project planning and task breakdown.

#### Capabilities

- `project_decomposition`
- `task_breakdown`
- `timeline_estimation`
- `resource_planning`
- `dependency_mapping`
- `risk_assessment`
- `milestone_definition`
- `roadmap_creation`

#### Configuration

```python
config = {
    "methodology": "agile"  # or "waterfall", "kanban", "scrum"
}
```

#### Example

```python
agent = PlanningAgent("my_planner", config={"methodology": "agile"})
result = agent.execute(
    "Build a REST API",
    context={"complexity": "medium", "deadline": "4 weeks"}
)
print(result["phases"])
```

---

### BuildingAgent

**Location:** `agent_factory.templates.building_agent`

Agent specialized in build automation and CI/CD.

#### Capabilities

- `build_configuration`
- `ci_cd_pipeline_creation`
- `dependency_management`
- `automated_testing`
- `deployment_automation`
- `container_orchestration`
- `build_optimization`
- `artifact_management`

#### Configuration

```python
config = {
    "build_tools": ["Maven", "Gradle", "npm", "pip", "Docker"],
    "platforms": ["GitHub Actions", "Jenkins", "GitLab CI", "CircleCI"]
}
```

#### Example

```python
agent = BuildingAgent("my_builder")
result = agent.execute(
    "Set up CI/CD pipeline",
    context={"platform": "GitHub Actions", "language": "Python"}
)
print(result["build_config"])
```

---

## Workflows

### WorkflowManager

**Location:** `agent_factory.workflows.workflow_manager`

Manage and execute workflows that involve multiple agents.

#### Methods

##### create_workflow()

```python
def create_workflow(self, name: str, description: str, steps: List[Dict[str, Any]]) -> Dict[str, Any]
```

Create a new workflow.

**Parameters:**
- `name` (str): Unique name for the workflow
- `description` (str): Description of what the workflow does
- `steps` (list): List of workflow steps

**Returns:**
- dict: Created workflow configuration

##### execute_workflow()

```python
def execute_workflow(self, name: str, agents: Dict[str, BaseAgent], initial_context: Optional[Dict[str, Any]] = None) -> Dict[str, Any]
```

Execute a workflow.

**Parameters:**
- `name` (str): Name of the workflow to execute
- `agents` (dict): Dictionary mapping agent names to agent instances
- `initial_context` (dict, optional): Initial context for the workflow

**Returns:**
- dict: Workflow execution results

---

### WorkflowBuilder

**Location:** `agent_factory.workflows.workflow_builder`

Fluent builder for creating workflows.

#### Methods

##### add_step()

```python
def add_step(self, agent: str, task: str, context: Optional[Dict[str, Any]] = None, step_type: str = "sequential") -> "WorkflowBuilder"
```

Add a step to the workflow.

**Parameters:**
- `agent` (str): Name of the agent to use for this step
- `task` (str): Task description for the agent
- `context` (dict, optional): Additional context for this step
- `step_type` (str): Type of step (sequential, parallel)

**Returns:**
- WorkflowBuilder: Self for method chaining

##### build()

```python
def build(self) -> Dict[str, Any]
```

Build the workflow configuration.

**Returns:**
- dict: Workflow configuration dictionary

#### Example

```python
workflow = (WorkflowBuilder("development", "Full dev cycle")
    .add_step("planner", "Plan the project")
    .add_step("coder", "Implement features")
    .add_step("debugger", "Review code")
    .build())
```

---

### WorkflowTemplates

**Location:** `agent_factory.workflows.workflow_builder`

Pre-defined workflow templates for common scenarios.

#### Static Methods

##### full_development_workflow()

```python
@staticmethod
def full_development_workflow(name: str = "full_development") -> WorkflowBuilder
```

Create a complete development workflow.

##### code_review_workflow()

```python
@staticmethod
def code_review_workflow(name: str = "code_review") -> WorkflowBuilder
```

Create a code review workflow.

##### deployment_workflow()

```python
@staticmethod
def deployment_workflow(name: str = "deployment") -> WorkflowBuilder
```

Create a deployment workflow.

##### bug_fix_workflow()

```python
@staticmethod
def bug_fix_workflow(name: str = "bug_fix") -> WorkflowBuilder
```

Create a bug fixing workflow.

---

## Configuration

### ConfigLoader

**Location:** `agent_factory.config.config_loader`

Load and parse configuration files for agents and the factory.

#### Static Methods

##### load_from_file()

```python
@staticmethod
def load_from_file(file_path: str) -> Dict[str, Any]
```

Load configuration from a JSON or YAML file.

##### get_default_config()

```python
@staticmethod
def get_default_config() -> Dict[str, Any]
```

Get default configuration for the agent factory.

##### save_to_file()

```python
@staticmethod
def save_to_file(config: Dict[str, Any], file_path: str, format: str = "json")
```

Save configuration to a file.

---

### ConfigValidator

**Location:** `agent_factory.config.config_validator`

Validate configuration dictionaries for agents and factory.

#### Static Methods

##### validate_agent_config()

```python
@staticmethod
def validate_agent_config(config: Dict[str, Any], agent_type: str) -> Dict[str, Any]
```

Validate agent configuration.

**Returns:**
- dict: Validation result with 'valid' boolean and optional 'errors' list

##### validate_factory_config()

```python
@staticmethod
def validate_factory_config(config: Dict[str, Any]) -> Dict[str, Any]
```

Validate factory configuration.

##### validate_workflow_config()

```python
@staticmethod
def validate_workflow_config(workflow: Dict[str, Any]) -> Dict[str, Any]
```

Validate workflow configuration.

---

## Utilities

### Logger

**Location:** `agent_factory.utils.logger`

Logger utility for the agent factory.

#### Functions

##### setup_logger()

```python
def setup_logger(name: str = "agent_factory", level: int = logging.INFO, log_file: Optional[str] = None) -> logging.Logger
```

Set up a logger for the agent factory.

---

### Serializer

**Location:** `agent_factory.utils.serializer`

Serialization utilities for agents.

#### Functions

##### serialize_agent()

```python
def serialize_agent(agent: BaseAgent) -> str
```

Serialize an agent to JSON string.

##### deserialize_agent()

```python
def deserialize_agent(json_str: str, agent_class: Type[BaseAgent]) -> BaseAgent
```

Deserialize an agent from JSON string.
