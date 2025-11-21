"""Serialization utilities for agents."""

import json
from typing import Dict, Any, Type
from ..core.base_agent import BaseAgent


def serialize_agent(agent: BaseAgent) -> str:
    """
    Serialize an agent to JSON string.
    
    Args:
        agent: Agent instance to serialize
        
    Returns:
        JSON string representation of the agent
    """
    return agent.export_state()


def deserialize_agent(json_str: str, agent_class: Type[BaseAgent]) -> BaseAgent:
    """
    Deserialize an agent from JSON string.
    
    Args:
        json_str: JSON string representing an agent
        agent_class: Class of the agent to instantiate
        
    Returns:
        Restored agent instance
    """
    state = json.loads(json_str)
    
    # Create new agent instance
    agent = agent_class(
        name=state.get("name", "restored_agent"),
        config=state.get("config", {})
    )
    
    # Restore state
    agent.created_at = state.get("created_at", agent.created_at)
    agent.history = state.get("history", [])
    agent.metadata = state.get("metadata", agent.metadata)
    
    return agent


def agent_to_dict(agent: BaseAgent) -> Dict[str, Any]:
    """
    Convert an agent to a dictionary.
    
    Args:
        agent: Agent instance
        
    Returns:
        Dictionary representation of the agent
    """
    return json.loads(agent.export_state())


def dict_to_agent(agent_dict: Dict[str, Any], agent_class: Type[BaseAgent]) -> BaseAgent:
    """
    Create an agent from a dictionary.
    
    Args:
        agent_dict: Dictionary representing an agent
        agent_class: Class of the agent to instantiate
        
    Returns:
        Agent instance
    """
    return deserialize_agent(json.dumps(agent_dict), agent_class)
