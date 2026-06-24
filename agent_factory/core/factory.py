"""Agent Factory - Core engine for creating and managing agents."""

from typing import Dict, Any, List, Optional, Type
from .base_agent import BaseAgent
from .registry import AgentRegistry


class AgentFactory:
    """
    Main factory class for creating and managing AI agents.
    
    This is the core engine that orchestrates agent creation, configuration,
    and lifecycle management.
    """
    
    def __init__(self):
        """Initialize the agent factory."""
        self.registry = AgentRegistry()
        self.active_agents: Dict[str, BaseAgent] = {}
        
    def create_agent(self, 
                    agent_type: str, 
                    name: str, 
                    config: Optional[Dict[str, Any]] = None) -> BaseAgent:
        """
        Create a new agent instance.
        
        Args:
            agent_type: Type of agent to create (must be registered)
            name: Unique name for the agent instance
            config: Configuration dictionary for the agent
            
        Returns:
            Created agent instance
            
        Raises:
            ValueError: If agent_type is not registered or name is already in use
        """
        if not self.registry.is_registered(agent_type):
            raise ValueError(
                f"Agent type '{agent_type}' is not registered. "
                f"Available types: {self.registry.list_types()}"
            )
        
        if name in self.active_agents:
            raise ValueError(f"Agent with name '{name}' already exists")
        
        agent_class = self.registry.get(agent_type)
        agent = agent_class(name=name, config=config)
        self.active_agents[name] = agent
        
        return agent
    
    def get_agent(self, name: str) -> Optional[BaseAgent]:
        """
        Get an active agent by name.
        
        Args:
            name: Name of the agent to retrieve
            
        Returns:
            Agent instance or None if not found
        """
        return self.active_agents.get(name)
    
    def list_agents(self) -> List[str]:
        """
        List all active agent names.
        
        Returns:
            List of active agent names
        """
        return list(self.active_agents.keys())
    
    def remove_agent(self, name: str) -> bool:
        """
        Remove an agent from active agents.
        
        Args:
            name: Name of the agent to remove
            
        Returns:
            True if removed, False if not found
        """
        if name in self.active_agents:
            del self.active_agents[name]
            return True
        return False
    
    def get_agent_info(self, name: str) -> Optional[Dict[str, Any]]:
        """
        Get information about an agent.
        
        Args:
            name: Name of the agent
            
        Returns:
            Agent information dictionary or None if not found
        """
        agent = self.get_agent(name)
        if agent:
            return agent.get_info()
        return None
    
    def list_available_types(self) -> List[str]:
        """
        List all available agent types that can be created.
        
        Returns:
            List of registered agent type names
        """
        return self.registry.list_types()
    
    def register_agent_type(self, agent_type: str, agent_class: Type[BaseAgent]):
        """
        Register a new agent type with the factory.
        
        Args:
            agent_type: String identifier for the agent type
            agent_class: Class that implements BaseAgent
        """
        self.registry.register(agent_type, agent_class)
    
    def get_all_agents_info(self) -> Dict[str, Dict[str, Any]]:
        """
        Get information about all active agents.
        
        Returns:
            Dictionary mapping agent names to their info
        """
        return {name: agent.get_info() for name, agent in self.active_agents.items()}
    
    def execute_agent_task(self, 
                          name: str, 
                          task: str, 
                          context: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """
        Execute a task using a specific agent.
        
        Args:
            name: Name of the agent to use
            task: Task description
            context: Optional context for the task
            
        Returns:
            Task execution result
            
        Raises:
            ValueError: If agent is not found
        """
        agent = self.get_agent(name)
        if not agent:
            raise ValueError(f"Agent '{name}' not found")
        
        return agent.execute(task, context)
    
    def clear_all_agents(self):
        """Remove all active agents."""
        self.active_agents.clear()
