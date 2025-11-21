"""Tests for the Agent Factory Warehouse system."""

import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
from agent_factory import AgentFactory, BaseAgent
from agent_factory.templates import CodingAgent, DebuggingAgent, PlanningAgent, BuildingAgent
from agent_factory.core.registry import AgentRegistry


@pytest.fixture(autouse=True)
def clear_registry():
    """Clear the registry before each test."""
    registry = AgentRegistry()
    registry.clear()
    yield
    registry.clear()


class TestAgentFactory:
    """Test the AgentFactory class."""
    
    def test_factory_creation(self):
        """Test creating a factory instance."""
        factory = AgentFactory()
        assert factory is not None
        assert isinstance(factory.registry, AgentRegistry)
        
    def test_register_agent_type(self):
        """Test registering an agent type."""
        factory = AgentFactory()
        factory.register_agent_type("coding", CodingAgent)
        assert "coding" in factory.list_available_types()
        
    def test_create_agent(self):
        """Test creating an agent."""
        factory = AgentFactory()
        factory.register_agent_type("coding", CodingAgent)
        
        agent = factory.create_agent("coding", "test_agent")
        assert agent is not None
        assert agent.name == "test_agent"
        assert isinstance(agent, CodingAgent)
        
    def test_get_agent(self):
        """Test retrieving an agent."""
        factory = AgentFactory()
        factory.register_agent_type("coding", CodingAgent)
        
        agent = factory.create_agent("coding", "test_agent")
        retrieved = factory.get_agent("test_agent")
        
        assert retrieved is agent
        
    def test_list_agents(self):
        """Test listing agents."""
        factory = AgentFactory()
        factory.register_agent_type("coding", CodingAgent)
        
        factory.create_agent("coding", "agent1")
        factory.create_agent("coding", "agent2")
        
        agents = factory.list_agents()
        assert len(agents) == 2
        assert "agent1" in agents
        assert "agent2" in agents
        
    def test_remove_agent(self):
        """Test removing an agent."""
        factory = AgentFactory()
        factory.register_agent_type("coding", CodingAgent)
        
        factory.create_agent("coding", "test_agent")
        assert "test_agent" in factory.list_agents()
        
        result = factory.remove_agent("test_agent")
        assert result is True
        assert "test_agent" not in factory.list_agents()


class TestCodingAgent:
    """Test the CodingAgent class."""
    
    def test_coding_agent_creation(self):
        """Test creating a coding agent."""
        agent = CodingAgent("test_coder")
        assert agent.name == "test_coder"
        assert agent.agent_type == "CodingAgent"
        
    def test_coding_agent_capabilities(self):
        """Test coding agent capabilities."""
        agent = CodingAgent("test_coder")
        capabilities = agent.get_capabilities()
        
        assert "code_generation" in capabilities
        assert "code_refactoring" in capabilities
        assert "code_analysis" in capabilities
        
    def test_coding_agent_execute(self):
        """Test executing a coding task."""
        agent = CodingAgent("test_coder")
        result = agent.execute(
            "Create a hello world function",
            context={"language": "Python"}
        )
        
        assert result["success"] is True
        assert "code" in result
        assert result["language"] == "Python"


class TestDebuggingAgent:
    """Test the DebuggingAgent class."""
    
    def test_debugging_agent_creation(self):
        """Test creating a debugging agent."""
        agent = DebuggingAgent("test_debugger")
        assert agent.name == "test_debugger"
        assert agent.agent_type == "DebuggingAgent"
        
    def test_debugging_agent_capabilities(self):
        """Test debugging agent capabilities."""
        agent = DebuggingAgent("test_debugger")
        capabilities = agent.get_capabilities()
        
        assert "error_analysis" in capabilities
        assert "bug_identification" in capabilities
        assert "fix_suggestion" in capabilities
        
    def test_debugging_agent_execute(self):
        """Test executing a debugging task."""
        agent = DebuggingAgent("test_debugger")
        result = agent.execute(
            "Fix null pointer exception",
            context={"error_type": "NullPointerException"}
        )
        
        assert result["success"] is True
        assert result["error_type"] == "NullPointerException"
        assert "analysis" in result
        assert "suggested_fixes" in result


class TestPlanningAgent:
    """Test the PlanningAgent class."""
    
    def test_planning_agent_creation(self):
        """Test creating a planning agent."""
        agent = PlanningAgent("test_planner")
        assert agent.name == "test_planner"
        assert agent.agent_type == "PlanningAgent"
        
    def test_planning_agent_capabilities(self):
        """Test planning agent capabilities."""
        agent = PlanningAgent("test_planner")
        capabilities = agent.get_capabilities()
        
        assert "project_decomposition" in capabilities
        assert "task_breakdown" in capabilities
        assert "timeline_estimation" in capabilities
        
    def test_planning_agent_execute(self):
        """Test executing a planning task."""
        agent = PlanningAgent("test_planner")
        result = agent.execute(
            "Build a web application",
            context={"complexity": "medium"}
        )
        
        assert result["success"] is True
        assert "phases" in result
        assert "tasks" in result
        assert "timeline" in result


class TestBuildingAgent:
    """Test the BuildingAgent class."""
    
    def test_building_agent_creation(self):
        """Test creating a building agent."""
        agent = BuildingAgent("test_builder")
        assert agent.name == "test_builder"
        assert agent.agent_type == "BuildingAgent"
        
    def test_building_agent_capabilities(self):
        """Test building agent capabilities."""
        agent = BuildingAgent("test_builder")
        capabilities = agent.get_capabilities()
        
        assert "build_configuration" in capabilities
        assert "ci_cd_pipeline_creation" in capabilities
        assert "deployment_automation" in capabilities
        
    def test_building_agent_execute(self):
        """Test executing a building task."""
        agent = BuildingAgent("test_builder")
        result = agent.execute(
            "Set up CI/CD pipeline",
            context={"platform": "GitHub Actions", "language": "Python"}
        )
        
        assert result["success"] is True
        assert result["platform"] == "GitHub Actions"
        assert "build_config" in result
        assert "pipeline" in result


class TestBaseAgent:
    """Test the BaseAgent functionality."""
    
    def test_agent_info(self):
        """Test getting agent info."""
        agent = CodingAgent("test_agent")
        info = agent.get_info()
        
        assert info["name"] == "test_agent"
        assert info["type"] == "CodingAgent"
        assert "capabilities" in info
        assert "created_at" in info
        
    def test_agent_history(self):
        """Test agent execution history."""
        agent = CodingAgent("test_agent")
        
        # Execute some tasks
        agent.execute("task 1", {"language": "Python"})
        agent.execute("task 2", {"language": "JavaScript"})
        
        history = agent.get_history()
        assert len(history) == 2
        assert history[0]["task"] == "task 1"
        assert history[1]["task"] == "task 2"
        
    def test_agent_export_state(self):
        """Test exporting agent state."""
        agent = CodingAgent("test_agent")
        agent.execute("test task", {"language": "Python"})
        
        state = agent.export_state()
        assert state is not None
        assert "test_agent" in state
        assert "CodingAgent" in state


if __name__ == "__main__":
    # Run tests
    pytest.main([__file__, "-v"])
