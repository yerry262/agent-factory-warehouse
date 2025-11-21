"""Base Agent class - Foundation for all agent types."""

from abc import ABC, abstractmethod
from typing import Dict, Any, List, Optional
import json
from datetime import datetime


class BaseAgent(ABC):
    """
    Abstract base class for all agent types in the factory.
    
    All custom agents should inherit from this class and implement
    the required abstract methods.
    """
    
    def __init__(self, name: str, config: Optional[Dict[str, Any]] = None):
        """
        Initialize a base agent.
        
        Args:
            name: Unique identifier for the agent
            config: Configuration dictionary for the agent
        """
        self.name = name
        self.config = config or {}
        self.agent_type = self.__class__.__name__
        self.created_at = datetime.now().isoformat()
        self.metadata = {
            "version": "1.0.0",
            "capabilities": self.get_capabilities()
        }
        self.history: List[Dict[str, Any]] = []
        
    @abstractmethod
    def execute(self, task: str, context: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """
        Execute the agent's primary task.
        
        Args:
            task: Description of the task to perform
            context: Additional context information
            
        Returns:
            Dictionary containing execution results
        """
        pass
    
    @abstractmethod
    def get_capabilities(self) -> List[str]:
        """
        Return a list of capabilities this agent has.
        
        Returns:
            List of capability strings
        """
        pass
    
    def validate_input(self, task: str, context: Optional[Dict[str, Any]] = None) -> bool:
        """
        Validate input before execution.
        
        Args:
            task: Task description to validate
            context: Context to validate
            
        Returns:
            True if input is valid, False otherwise
        """
        if task is None or not isinstance(task, str):
            return False
        if context is not None and not isinstance(context, dict):
            return False
        return True
    
    def log_execution(self, task: str, result: Dict[str, Any]):
        """
        Log an execution in the agent's history.
        
        Args:
            task: The task that was executed
            result: The result of the execution
        """
        log_entry = {
            "timestamp": datetime.now().isoformat(),
            "task": task,
            "result": result,
            "agent_type": self.agent_type
        }
        self.history.append(log_entry)
    
    def get_history(self) -> List[Dict[str, Any]]:
        """
        Get the execution history of this agent.
        
        Returns:
            List of execution log entries
        """
        return self.history.copy()
    
    def get_info(self) -> Dict[str, Any]:
        """
        Get information about this agent.
        
        Returns:
            Dictionary containing agent information
        """
        return {
            "name": self.name,
            "type": self.agent_type,
            "created_at": self.created_at,
            "capabilities": self.get_capabilities(),
            "config": self.config,
            "metadata": self.metadata,
            "execution_count": len(self.history)
        }
    
    def update_config(self, new_config: Dict[str, Any]):
        """
        Update the agent's configuration.
        
        Args:
            new_config: New configuration dictionary
        """
        self.config.update(new_config)
    
    def export_state(self) -> str:
        """
        Export the agent's state as JSON.
        
        Returns:
            JSON string representing the agent's state
        """
        state = {
            "name": self.name,
            "type": self.agent_type,
            "config": self.config,
            "created_at": self.created_at,
            "metadata": self.metadata,
            "history": self.history
        }
        return json.dumps(state, indent=2)
    
    def __repr__(self) -> str:
        return f"{self.agent_type}(name='{self.name}', capabilities={len(self.get_capabilities())})"
