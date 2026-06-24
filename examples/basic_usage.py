#!/usr/bin/env python3
"""
Basic usage example of the Agent Factory Warehouse.

This example demonstrates:
1. Creating the factory
2. Registering agent types
3. Creating agents
4. Executing tasks with agents
"""

import sys
import os

# Add parent directory to path for imports
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from agent_factory import AgentFactory
from agent_factory.templates import CodingAgent, DebuggingAgent, PlanningAgent, BuildingAgent


def main():
    print("=" * 60)
    print("Agent Factory Warehouse - Basic Usage Example")
    print("=" * 60)
    print()
    
    # Create the factory
    factory = AgentFactory()
    print("✓ Created AgentFactory")
    
    # Register agent types
    factory.register_agent_type("coding", CodingAgent)
    factory.register_agent_type("debugging", DebuggingAgent)
    factory.register_agent_type("planning", PlanningAgent)
    factory.register_agent_type("building", BuildingAgent)
    print(f"✓ Registered {len(factory.list_available_types())} agent types")
    print(f"  Available types: {', '.join(factory.list_available_types())}")
    print()
    
    # Create a coding agent
    print("Creating a coding agent...")
    coding_agent = factory.create_agent(
        agent_type="coding",
        name="my_coding_agent",
        config={"languages": ["Python", "JavaScript"], "style_guide": "PEP8"}
    )
    print(f"✓ Created: {coding_agent}")
    print(f"  Capabilities: {', '.join(coding_agent.get_capabilities())}")
    print()
    
    # Execute a task with the coding agent
    print("Executing a coding task...")
    result = coding_agent.execute(
        task="Create a function to calculate fibonacci numbers",
        context={"language": "Python"}
    )
    print(f"✓ Task executed successfully!")
    print(f"  Language: {result['language']}")
    print(f"  Generated code:")
    print("-" * 60)
    print(result['code'])
    print("-" * 60)
    print()
    
    # Create a planning agent
    print("Creating a planning agent...")
    planning_agent = factory.create_agent(
        agent_type="planning",
        name="my_planning_agent",
        config={"methodology": "agile"}
    )
    print(f"✓ Created: {planning_agent}")
    print()
    
    # Execute a planning task
    print("Executing a planning task...")
    plan_result = planning_agent.execute(
        task="Build a web application with user authentication",
        context={"complexity": "medium", "deadline": "6 weeks"}
    )
    print(f"✓ Planning completed!")
    print(f"  Project: {plan_result['project']}")
    print(f"  Methodology: {plan_result['methodology']}")
    print(f"  Timeline: {plan_result['timeline']['total_weeks']} weeks")
    print(f"  Phases: {len(plan_result['phases'])}")
    for phase in plan_result['phases']:
        print(f"    - {phase['name']}: {phase['duration']}")
    print()
    
    # Create a debugging agent
    print("Creating a debugging agent...")
    debugging_agent = factory.create_agent(
        agent_type="debugging",
        name="my_debugging_agent"
    )
    print(f"✓ Created: {debugging_agent}")
    print()
    
    # Execute a debugging task
    print("Executing a debugging task...")
    debug_result = debugging_agent.execute(
        task="Fix NullPointerException in user login flow",
        context={"error_type": "NullPointerException", "code": "user.getName()"}
    )
    print(f"✓ Debugging completed!")
    print(f"  Error type: {debug_result['error_type']}")
    print(f"  Severity: {debug_result['severity']}")
    print(f"  Likely causes:")
    for cause in debug_result['analysis']['likely_causes']:
        print(f"    - {cause}")
    print(f"  Suggested fixes:")
    for fix in debug_result['suggested_fixes'][:3]:
        print(f"    - {fix}")
    print()
    
    # Show all active agents
    print("Active agents in factory:")
    for agent_name in factory.list_agents():
        info = factory.get_agent_info(agent_name)
        print(f"  - {agent_name} ({info['type']}): {info['execution_count']} executions")
    print()
    
    print("=" * 60)
    print("Example completed successfully!")
    print("=" * 60)


if __name__ == "__main__":
    main()
