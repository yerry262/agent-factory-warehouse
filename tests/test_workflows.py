"""Tests for workflow functionality."""

import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
from agent_factory import AgentFactory
from agent_factory.templates import CodingAgent, DebuggingAgent
from agent_factory.workflows import WorkflowManager, WorkflowBuilder, WorkflowTemplates
from agent_factory.core.registry import AgentRegistry


@pytest.fixture(autouse=True)
def clear_registry():
    """Clear the registry before each test."""
    registry = AgentRegistry()
    registry.clear()
    yield
    registry.clear()


class TestWorkflowManager:
    """Test the WorkflowManager class."""
    
    def test_workflow_manager_creation(self):
        """Test creating a workflow manager."""
        manager = WorkflowManager()
        assert manager is not None
        assert len(manager.list_workflows()) == 0
        
    def test_create_workflow(self):
        """Test creating a workflow."""
        manager = WorkflowManager()
        
        steps = [
            {"agent": "coder", "task": "Write code"},
            {"agent": "debugger", "task": "Debug code"}
        ]
        
        workflow = manager.create_workflow("test_workflow", "Test workflow", steps)
        
        assert workflow["name"] == "test_workflow"
        assert workflow["description"] == "Test workflow"
        assert len(workflow["steps"]) == 2
        
    def test_list_workflows(self):
        """Test listing workflows."""
        manager = WorkflowManager()
        
        manager.create_workflow("workflow1", "First workflow", [])
        manager.create_workflow("workflow2", "Second workflow", [])
        
        workflows = manager.list_workflows()
        assert len(workflows) == 2
        assert "workflow1" in workflows
        assert "workflow2" in workflows
        
    def test_get_workflow(self):
        """Test getting a workflow."""
        manager = WorkflowManager()
        
        steps = [{"agent": "coder", "task": "Write code"}]
        manager.create_workflow("test_workflow", "Test", steps)
        
        workflow = manager.get_workflow("test_workflow")
        assert workflow is not None
        assert workflow["name"] == "test_workflow"
        
    def test_delete_workflow(self):
        """Test deleting a workflow."""
        manager = WorkflowManager()
        
        manager.create_workflow("test_workflow", "Test", [])
        assert "test_workflow" in manager.list_workflows()
        
        result = manager.delete_workflow("test_workflow")
        assert result is True
        assert "test_workflow" not in manager.list_workflows()
        
    def test_execute_workflow(self):
        """Test executing a workflow."""
        manager = WorkflowManager()
        factory = AgentFactory()
        
        # Set up agents
        factory.register_agent_type("coding", CodingAgent)
        coder = factory.create_agent("coding", "coder")
        
        agents = {"coder": coder}
        
        # Create and execute workflow
        steps = [
            {"agent": "coder", "task": "Write a function"}
        ]
        
        manager.create_workflow("simple_workflow", "Simple workflow", steps)
        result = manager.execute_workflow("simple_workflow", agents)
        
        assert result["success"] is True
        assert result["steps_completed"] == 1
        assert result["total_steps"] == 1


class TestWorkflowBuilder:
    """Test the WorkflowBuilder class."""
    
    def test_workflow_builder_creation(self):
        """Test creating a workflow builder."""
        builder = WorkflowBuilder("test_workflow", "Test description")
        
        assert builder.name == "test_workflow"
        assert builder.description == "Test description"
        assert builder.get_step_count() == 0
        
    def test_add_step(self):
        """Test adding a step to the workflow."""
        builder = WorkflowBuilder("test_workflow")
        builder.add_step("coder", "Write code")
        
        assert builder.get_step_count() == 1
        
    def test_add_multiple_steps(self):
        """Test adding multiple steps."""
        builder = (WorkflowBuilder("test_workflow")
                  .add_step("coder", "Write code")
                  .add_step("debugger", "Debug code")
                  .add_step("builder", "Build project"))
        
        assert builder.get_step_count() == 3
        
    def test_build_workflow(self):
        """Test building a workflow."""
        workflow = (WorkflowBuilder("test_workflow", "Test")
                   .add_step("coder", "Write code")
                   .add_step("debugger", "Debug code")
                   .build())
        
        assert workflow["name"] == "test_workflow"
        assert workflow["description"] == "Test"
        assert len(workflow["steps"]) == 2
        
    def test_clear_steps(self):
        """Test clearing workflow steps."""
        builder = (WorkflowBuilder("test_workflow")
                  .add_step("coder", "Write code")
                  .add_step("debugger", "Debug code"))
        
        assert builder.get_step_count() == 2
        
        builder.clear()
        assert builder.get_step_count() == 0
        
    def test_remove_last_step(self):
        """Test removing the last step."""
        builder = (WorkflowBuilder("test_workflow")
                  .add_step("coder", "Write code")
                  .add_step("debugger", "Debug code"))
        
        assert builder.get_step_count() == 2
        
        builder.remove_last_step()
        assert builder.get_step_count() == 1


class TestWorkflowTemplates:
    """Test the WorkflowTemplates class."""
    
    def test_full_development_workflow(self):
        """Test creating a full development workflow."""
        workflow = WorkflowTemplates.full_development_workflow().build()
        
        assert workflow["name"] == "full_development"
        assert len(workflow["steps"]) == 5
        
    def test_code_review_workflow(self):
        """Test creating a code review workflow."""
        workflow = WorkflowTemplates.code_review_workflow().build()
        
        assert workflow["name"] == "code_review"
        assert len(workflow["steps"]) == 3
        
    def test_deployment_workflow(self):
        """Test creating a deployment workflow."""
        workflow = WorkflowTemplates.deployment_workflow().build()
        
        assert workflow["name"] == "deployment"
        assert len(workflow["steps"]) == 3
        
    def test_bug_fix_workflow(self):
        """Test creating a bug fix workflow."""
        workflow = WorkflowTemplates.bug_fix_workflow().build()
        
        assert workflow["name"] == "bug_fix"
        assert len(workflow["steps"]) == 4


if __name__ == "__main__":
    # Run tests
    pytest.main([__file__, "-v"])
