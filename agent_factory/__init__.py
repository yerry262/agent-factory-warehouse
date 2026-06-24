"""
Agent Factory Warehouse - A system for generating custom AI agent modules.

This package provides a factory engine for creating and managing various types
of AI agents with extensible templates and modular workflows.
"""

from .core.factory import AgentFactory
from .core.base_agent import BaseAgent
from .core.registry import AgentRegistry

__version__ = "1.0.0"
__all__ = ["AgentFactory", "BaseAgent", "AgentRegistry"]
