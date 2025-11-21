"""Agent Registry - Manages registration and discovery of agent types."""

from typing import Dict, Type, List, Optional
from .base_agent import BaseAgent


class AgentRegistry:
    """
    Registry for managing available agent types.
    
    Provides a centralized system for registering, discovering, and
    instantiating different types of agents.
    """
    
    _instance = None
    _agents: Dict[str, Type[BaseAgent]] = {}
    
    def __new__(cls):
        """Singleton pattern to ensure only one registry exists."""
        if cls._instance is None:
            cls._instance = super(AgentRegistry, cls).__new__(cls)
        return cls._instance
    
    def register(self, agent_type: str, agent_class: Type[BaseAgent]):
        """
        Register a new agent type.
        
        Args:
            agent_type: String identifier for the agent type
            agent_class: Class that implements BaseAgent
            
        Raises:
            ValueError: If agent_type is already registered
            TypeError: If agent_class doesn't inherit from BaseAgent
        """
        if not issubclass(agent_class, BaseAgent):
            raise TypeError(f"{agent_class.__name__} must inherit from BaseAgent")
        
        if agent_type in self._agents:
            raise ValueError(f"Agent type '{agent_type}' is already registered")
        
        self._agents[agent_type] = agent_class
        
    def unregister(self, agent_type: str):
        """
        Unregister an agent type.
        
        Args:
            agent_type: String identifier for the agent type to remove
        """
        if agent_type in self._agents:
            del self._agents[agent_type]
    
    def get(self, agent_type: str) -> Optional[Type[BaseAgent]]:
        """
        Get an agent class by type.
        
        Args:
            agent_type: String identifier for the agent type
            
        Returns:
            Agent class or None if not found
        """
        return self._agents.get(agent_type)
    
    def list_types(self) -> List[str]:
        """
        List all registered agent types.
        
        Returns:
            List of registered agent type identifiers
        """
        return list(self._agents.keys())
    
    def is_registered(self, agent_type: str) -> bool:
        """
        Check if an agent type is registered.
        
        Args:
            agent_type: String identifier for the agent type
            
        Returns:
            True if registered, False otherwise
        """
        return agent_type in self._agents
    
    def get_all(self) -> Dict[str, Type[BaseAgent]]:
        """
        Get all registered agent types.
        
        Returns:
            Dictionary mapping agent types to their classes
        """
        return self._agents.copy()
    
    def clear(self):
        """Clear all registered agent types (useful for testing)."""
        self._agents.clear()
