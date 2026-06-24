"""Workflow Builder - Fluent API for building workflows."""

from typing import Dict, Any, List, Optional


class WorkflowBuilder:
    """
    Fluent builder for creating workflows.
    
    Provides a convenient API for defining workflows step by step.
    """
    
    def __init__(self, name: str, description: str = ""):
        """
        Initialize a workflow builder.
        
        Args:
            name: Workflow name
            description: Workflow description
        """
        self.name = name
        self.description = description
        self.steps: List[Dict[str, Any]] = []
        
    def add_step(self, 
                 agent: str, 
                 task: str, 
                 context: Optional[Dict[str, Any]] = None,
                 step_type: str = "sequential") -> "WorkflowBuilder":
        """
        Add a step to the workflow.
        
        Args:
            agent: Name of the agent to use for this step
            task: Task description for the agent
            context: Additional context for this step
            step_type: Type of step (sequential, parallel)
            
        Returns:
            Self for method chaining
        """
        step = {
            "agent": agent,
            "task": task,
            "type": step_type
        }
        
        if context:
            step["context"] = context
            
        self.steps.append(step)
        return self
    
    def add_sequential_step(self,
                           agent: str,
                           task: str,
                           context: Optional[Dict[str, Any]] = None) -> "WorkflowBuilder":
        """
        Add a sequential step (executes after previous step completes).
        
        Args:
            agent: Name of the agent to use
            task: Task description
            context: Additional context
            
        Returns:
            Self for method chaining
        """
        return self.add_step(agent, task, context, "sequential")
    
    def add_parallel_step(self,
                         agent: str,
                         task: str,
                         context: Optional[Dict[str, Any]] = None) -> "WorkflowBuilder":
        """
        Add a parallel step (can execute concurrently with other parallel steps).
        
        Args:
            agent: Name of the agent to use
            task: Task description
            context: Additional context
            
        Returns:
            Self for method chaining
        """
        return self.add_step(agent, task, context, "parallel")
    
    def build(self) -> Dict[str, Any]:
        """
        Build the workflow configuration.
        
        Returns:
            Workflow configuration dictionary
        """
        return {
            "name": self.name,
            "description": self.description,
            "steps": self.steps
        }
    
    def clear(self) -> "WorkflowBuilder":
        """
        Clear all steps.
        
        Returns:
            Self for method chaining
        """
        self.steps.clear()
        return self
    
    def get_step_count(self) -> int:
        """
        Get the number of steps in the workflow.
        
        Returns:
            Number of steps
        """
        return len(self.steps)
    
    def remove_last_step(self) -> "WorkflowBuilder":
        """
        Remove the last step from the workflow.
        
        Returns:
            Self for method chaining
        """
        if self.steps:
            self.steps.pop()
        return self
    
    def __repr__(self) -> str:
        return f"WorkflowBuilder(name='{self.name}', steps={len(self.steps)})"


# Pre-defined workflow templates
class WorkflowTemplates:
    """Common workflow templates."""
    
    @staticmethod
    def full_development_workflow(name: str = "full_development") -> WorkflowBuilder:
        """
        Create a complete development workflow.
        
        Args:
            name: Workflow name
            
        Returns:
            WorkflowBuilder configured with full development workflow
        """
        return (WorkflowBuilder(name, "Complete development lifecycle workflow")
                .add_step("planner", "Create project plan and task breakdown")
                .add_step("coder", "Implement core functionality based on plan")
                .add_step("debugger", "Review code and identify potential issues")
                .add_step("coder", "Fix identified issues and refactor")
                .add_step("builder", "Set up CI/CD pipeline and build configuration"))
    
    @staticmethod
    def code_review_workflow(name: str = "code_review") -> WorkflowBuilder:
        """
        Create a code review workflow.
        
        Args:
            name: Workflow name
            
        Returns:
            WorkflowBuilder configured with code review workflow
        """
        return (WorkflowBuilder(name, "Code review and improvement workflow")
                .add_step("coder", "Analyze code quality and structure")
                .add_step("debugger", "Identify bugs and potential issues")
                .add_step("coder", "Suggest improvements and refactoring"))
    
    @staticmethod
    def deployment_workflow(name: str = "deployment") -> WorkflowBuilder:
        """
        Create a deployment workflow.
        
        Args:
            name: Workflow name
            
        Returns:
            WorkflowBuilder configured with deployment workflow
        """
        return (WorkflowBuilder(name, "Application deployment workflow")
                .add_step("builder", "Run tests and build application")
                .add_step("builder", "Create deployment configuration")
                .add_step("builder", "Deploy to target environment"))
    
    @staticmethod
    def bug_fix_workflow(name: str = "bug_fix") -> WorkflowBuilder:
        """
        Create a bug fixing workflow.
        
        Args:
            name: Workflow name
            
        Returns:
            WorkflowBuilder configured with bug fixing workflow
        """
        return (WorkflowBuilder(name, "Bug identification and fixing workflow")
                .add_step("debugger", "Analyze error and identify root cause")
                .add_step("coder", "Implement fix for the identified issue")
                .add_step("debugger", "Verify fix and test edge cases")
                .add_step("builder", "Update tests and documentation"))
