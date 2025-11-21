#!/usr/bin/env python3
"""
Workflow usage example for the Agent Factory Warehouse.

This example demonstrates:
1. Creating and using workflows
2. Orchestrating multiple agents
3. Using workflow templates
"""

import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from agent_factory import AgentFactory
from agent_factory.templates import CodingAgent, DebuggingAgent, PlanningAgent, BuildingAgent
from agent_factory.workflows import WorkflowManager, WorkflowBuilder, WorkflowTemplates


def main():
    print("=" * 60)
    print("Agent Factory Warehouse - Workflow Example")
    print("=" * 60)
    print()
    
    # Set up factory and agents
    factory = AgentFactory()
    factory.register_agent_type("coding", CodingAgent)
    factory.register_agent_type("debugging", DebuggingAgent)
    factory.register_agent_type("planning", PlanningAgent)
    factory.register_agent_type("building", BuildingAgent)
    
    # Create agents
    planner = factory.create_agent("planning", "planner")
    coder = factory.create_agent("coding", "coder")
    debugger = factory.create_agent("debugging", "debugger")
    builder = factory.create_agent("building", "builder")
    
    agents = {
        "planner": planner,
        "coder": coder,
        "debugger": debugger,
        "builder": builder
    }
    
    print("✓ Created 4 agents")
    print()
    
    # Create workflow manager
    workflow_manager = WorkflowManager()
    
    # Example 1: Using WorkflowBuilder
    print("Example 1: Custom workflow with WorkflowBuilder")
    print("-" * 60)
    
    custom_workflow = (WorkflowBuilder("api_development", "Build a REST API")
                      .add_step("planner", "Plan REST API architecture and endpoints")
                      .add_step("coder", "Implement API endpoints", {"language": "Python"})
                      .add_step("debugger", "Review code for potential issues")
                      .add_step("builder", "Set up CI/CD for API", {"platform": "GitHub Actions"})
                      .build())
    
    workflow_manager.create_workflow(
        custom_workflow["name"],
        custom_workflow["description"],
        custom_workflow["steps"]
    )
    
    print(f"Created workflow: {custom_workflow['name']}")
    print(f"Description: {custom_workflow['description']}")
    print(f"Steps: {len(custom_workflow['steps'])}")
    for i, step in enumerate(custom_workflow['steps'], 1):
        print(f"  {i}. {step['agent']}: {step['task']}")
    print()
    
    # Execute the workflow
    print("Executing workflow...")
    result = workflow_manager.execute_workflow("api_development", agents)
    
    print(f"✓ Workflow completed!")
    print(f"  Success: {result['success']}")
    print(f"  Steps completed: {result['steps_completed']}/{result['total_steps']}")
    print()
    
    # Example 2: Using pre-defined workflow template
    print("Example 2: Using pre-defined workflow template")
    print("-" * 60)
    
    bug_fix_workflow = WorkflowTemplates.bug_fix_workflow("fix_login_bug").build()
    
    workflow_manager.create_workflow(
        bug_fix_workflow["name"],
        bug_fix_workflow["description"],
        bug_fix_workflow["steps"]
    )
    
    print(f"Created workflow from template: {bug_fix_workflow['name']}")
    print(f"Description: {bug_fix_workflow['description']}")
    print()
    
    # Execute the bug fix workflow
    print("Executing bug fix workflow...")
    bug_fix_result = workflow_manager.execute_workflow(
        "fix_login_bug", 
        agents,
        initial_context={"bug_description": "User login fails with null pointer exception"}
    )
    
    print(f"✓ Bug fix workflow completed!")
    print(f"  Success: {bug_fix_result['success']}")
    print(f"  Steps completed: {bug_fix_result['steps_completed']}/{bug_fix_result['total_steps']}")
    print()
    
    # Show all workflows
    print("All workflows:")
    for workflow_name in workflow_manager.list_workflows():
        workflow = workflow_manager.get_workflow(workflow_name)
        print(f"  - {workflow_name}: {len(workflow['steps'])} steps")
    print()
    
    # Show workflow execution history
    print("Workflow execution history:")
    for i, execution in enumerate(workflow_manager.get_execution_history(), 1):
        print(f"  {i}. {execution['workflow']} - {'✓ Success' if execution['success'] else '✗ Failed'}")
    print()
    
    print("=" * 60)
    print("Workflow example completed successfully!")
    print("=" * 60)


if __name__ == "__main__":
    main()
