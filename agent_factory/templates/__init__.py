"""Agent templates - Pre-built agent types for common tasks."""

from .coding_agent import CodingAgent
from .debugging_agent import DebuggingAgent
from .planning_agent import PlanningAgent
from .building_agent import BuildingAgent

__all__ = ["CodingAgent", "DebuggingAgent", "PlanningAgent", "BuildingAgent"]
