# Contributing to Agent Factory Warehouse

Thank you for your interest in contributing to Agent Factory Warehouse! This guide will help you get started.

## Getting Started

### Prerequisites

- Python 3.7 or higher
- Git

### Setting Up Development Environment

1. Clone the repository:
```bash
git clone https://github.com/yerry262/agent-factory-warehouse.git
cd agent-factory-warehouse
```

2. Install development dependencies:
```bash
pip install -r requirements.txt
```

3. Run tests to ensure everything works:
```bash
python3 -m pytest tests/ -v
```

## How to Contribute

### Creating a New Agent Template

To create a new agent template:

1. Create a new file in `agent_factory/templates/`:
```python
# agent_factory/templates/my_new_agent.py

from typing import Dict, Any, List, Optional
from ..core.base_agent import BaseAgent


class MyNewAgent(BaseAgent):
    """
    Agent specialized in [describe purpose].
    
    Capabilities:
    - [list capabilities]
    """
    
    def __init__(self, name: str, config: Optional[Dict[str, Any]] = None):
        super().__init__(name, config)
        # Initialize any agent-specific attributes
        
    def get_capabilities(self) -> List[str]:
        """Return the capabilities of this agent."""
        return [
            "capability_1",
            "capability_2",
            # Add more capabilities
        ]
    
    def execute(self, task: str, context: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """
        Execute a task.
        
        Args:
            task: Description of the task
            context: Additional context
            
        Returns:
            Dictionary containing execution results
        """
        if not self.validate_input(task, context):
            return {"success": False, "error": "Invalid input"}
        
        # Implement your agent logic here
        result = {
            "success": True,
            "task": task,
            # Add your results
        }
        
        self.log_execution(task, result)
        return result
```

2. Export your agent in `agent_factory/templates/__init__.py`:
```python
from .my_new_agent import MyNewAgent

__all__ = [..., "MyNewAgent"]
```

3. Create tests in `tests/test_agents.py`:
```python
class TestMyNewAgent:
    def test_creation(self):
        agent = MyNewAgent("test_agent")
        assert agent.name == "test_agent"
    
    def test_capabilities(self):
        agent = MyNewAgent("test_agent")
        capabilities = agent.get_capabilities()
        assert "capability_1" in capabilities
    
    def test_execute(self):
        agent = MyNewAgent("test_agent")
        result = agent.execute("test task")
        assert result["success"] is True
```

4. Add documentation to `API.md`

### Creating a New Workflow Template

To add a new workflow template in `agent_factory/workflows/workflow_builder.py`:

```python
@staticmethod
def my_new_workflow(name: str = "my_workflow") -> WorkflowBuilder:
    """
    Create a [describe workflow purpose].
    
    Args:
        name: Workflow name
        
    Returns:
        WorkflowBuilder configured with the workflow
    """
    return (WorkflowBuilder(name, "Description of workflow")
            .add_step("agent1", "Task for agent 1")
            .add_step("agent2", "Task for agent 2")
            # Add more steps
            )
```

### Adding Configuration Options

To add new configuration options:

1. Update the default configuration in `agent_factory/config/config_loader.py`:
```python
def get_default_config():
    return {
        # ... existing config
        "my_new_section": {
            "option1": "value1",
            "option2": "value2"
        }
    }
```

2. Add validation in `agent_factory/config/config_validator.py`:
```python
def _validate_my_config(self, config: Dict[str, Any]) -> List[str]:
    errors = []
    # Add validation logic
    return errors
```

## Code Style Guidelines

- Follow PEP 8 style guide for Python code
- Use type hints for function parameters and return values
- Include docstrings for all classes and public methods
- Keep functions focused and single-purpose
- Add comments for complex logic

### Docstring Format

```python
def function_name(param1: type1, param2: type2) -> return_type:
    """
    Brief description of what the function does.
    
    Args:
        param1: Description of param1
        param2: Description of param2
        
    Returns:
        Description of return value
        
    Raises:
        ExceptionType: When this exception is raised
    """
    pass
```

## Testing Guidelines

- Write tests for all new features
- Aim for high test coverage
- Use descriptive test names
- Test both success and failure cases
- Use fixtures to set up test data

### Running Tests

```bash
# Run all tests
python3 -m pytest tests/ -v

# Run specific test file
python3 -m pytest tests/test_agents.py -v

# Run with coverage
python3 -m pytest tests/ --cov=agent_factory --cov-report=html
```

## Documentation Guidelines

When adding new features:

1. Update `README.md` with usage examples
2. Add API documentation to `API.md`
3. Update `STRUCTURE.md` if adding new modules
4. Include inline code comments for complex logic
5. Create example scripts in `examples/` directory

## Pull Request Process

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Make your changes
4. Run tests and ensure they pass
5. Update documentation
6. Commit your changes (`git commit -m 'Add amazing feature'`)
7. Push to the branch (`git push origin feature/amazing-feature`)
8. Open a Pull Request

### Pull Request Checklist

- [ ] Code follows the style guidelines
- [ ] Tests added for new features
- [ ] All tests pass
- [ ] Documentation updated
- [ ] Example scripts created (if applicable)
- [ ] Commit messages are clear and descriptive

## Example Contributions

### Easy Contributions (Good First Issues)

- Add new agent templates (e.g., TestingAgent, SecurityAgent)
- Add more workflow templates
- Improve documentation with examples
- Add more configuration validation
- Create tutorial notebooks

### Medium Contributions

- Add parallel workflow execution
- Implement agent communication
- Add metrics and monitoring
- Create web interface
- Add persistence layer

### Advanced Contributions

- Integrate with LLM APIs
- Add distributed agent execution
- Implement agent learning/adaptation
- Create agent marketplace
- Add real-time collaboration

## Questions or Need Help?

- Open an issue for bugs or feature requests
- Use discussions for questions
- Check existing issues and documentation first

## Code of Conduct

- Be respectful and inclusive
- Focus on constructive feedback
- Help others learn and grow
- Follow the project's coding standards

Thank you for contributing to Agent Factory Warehouse! 🎉
