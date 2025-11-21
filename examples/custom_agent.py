#!/usr/bin/env python3
"""
Custom agent creation example.

This example demonstrates how to create custom agent types
by extending the BaseAgent class.
"""

import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from typing import Dict, Any, List, Optional
from agent_factory import AgentFactory, BaseAgent


class DocumentationAgent(BaseAgent):
    """
    Custom agent for generating and managing documentation.
    """
    
    def __init__(self, name: str, config: Optional[Dict[str, Any]] = None):
        super().__init__(name, config)
        self.doc_format = config.get("format", "markdown") if config else "markdown"
        
    def get_capabilities(self) -> List[str]:
        return [
            "api_documentation",
            "user_guide_generation",
            "code_documentation",
            "readme_generation",
            "changelog_generation"
        ]
    
    def execute(self, task: str, context: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        if not self.validate_input(task, context):
            return {"success": False, "error": "Invalid input"}
        
        context = context or {}
        doc_type = context.get("type", "general")
        
        result = {
            "success": True,
            "task": task,
            "doc_type": doc_type,
            "format": self.doc_format,
            "content": self._generate_documentation(task, doc_type),
            "metadata": {
                "word_count": 500,  # Simulated
                "sections": 5
            }
        }
        
        self.log_execution(task, result)
        return result
    
    def _generate_documentation(self, task: str, doc_type: str) -> str:
        """Generate documentation based on task and type."""
        templates = {
            "api": f"# API Documentation\n\n## Overview\n{task}\n\n## Endpoints\n- GET /api/resource\n- POST /api/resource",
            "readme": f"# {task}\n\n## Description\nProject documentation\n\n## Installation\n```bash\npip install package\n```",
            "general": f"# Documentation\n\n{task}\n\n## Details\nDetailed documentation here."
        }
        return templates.get(doc_type, templates["general"])


class TestingAgent(BaseAgent):
    """
    Custom agent for test generation and management.
    """
    
    def __init__(self, name: str, config: Optional[Dict[str, Any]] = None):
        super().__init__(name, config)
        self.test_framework = config.get("framework", "pytest") if config else "pytest"
        
    def get_capabilities(self) -> List[str]:
        return [
            "unit_test_generation",
            "integration_test_generation",
            "test_coverage_analysis",
            "test_data_generation",
            "test_automation"
        ]
    
    def execute(self, task: str, context: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        if not self.validate_input(task, context):
            return {"success": False, "error": "Invalid input"}
        
        context = context or {}
        test_type = context.get("test_type", "unit")
        
        result = {
            "success": True,
            "task": task,
            "test_type": test_type,
            "framework": self.test_framework,
            "test_code": self._generate_test_code(task, test_type),
            "test_count": 5,  # Simulated
            "coverage": "85%"
        }
        
        self.log_execution(task, result)
        return result
    
    def _generate_test_code(self, task: str, test_type: str) -> str:
        """Generate test code."""
        if self.test_framework == "pytest":
            return f'''import pytest

def test_{task.replace(" ", "_").lower()}():
    """Test for {task}"""
    # Arrange
    expected = True
    
    # Act
    result = function_under_test()
    
    # Assert
    assert result == expected
'''
        return "# Test code here"


def main():
    print("=" * 60)
    print("Agent Factory Warehouse - Custom Agent Example")
    print("=" * 60)
    print()
    
    # Create factory
    factory = AgentFactory()
    
    # Register custom agent types
    factory.register_agent_type("documentation", DocumentationAgent)
    factory.register_agent_type("testing", TestingAgent)
    
    print("✓ Registered custom agent types:")
    print(f"  - DocumentationAgent")
    print(f"  - TestingAgent")
    print()
    
    # Create custom agents
    print("Creating custom agents...")
    doc_agent = factory.create_agent(
        "documentation",
        "doc_writer",
        config={"format": "markdown"}
    )
    
    test_agent = factory.create_agent(
        "testing",
        "test_generator",
        config={"framework": "pytest"}
    )
    
    print(f"✓ Created: {doc_agent}")
    print(f"  Capabilities: {', '.join(doc_agent.get_capabilities()[:3])}...")
    print(f"✓ Created: {test_agent}")
    print(f"  Capabilities: {', '.join(test_agent.get_capabilities()[:3])}...")
    print()
    
    # Use documentation agent
    print("Generating API documentation...")
    doc_result = doc_agent.execute(
        "User Management API",
        context={"type": "api"}
    )
    
    print(f"✓ Documentation generated!")
    print(f"  Format: {doc_result['format']}")
    print(f"  Type: {doc_result['doc_type']}")
    print(f"  Content preview:")
    print("-" * 60)
    print(doc_result['content'][:200] + "...")
    print("-" * 60)
    print()
    
    # Use testing agent
    print("Generating unit tests...")
    test_result = test_agent.execute(
        "user authentication",
        context={"test_type": "unit"}
    )
    
    print(f"✓ Tests generated!")
    print(f"  Framework: {test_result['framework']}")
    print(f"  Test count: {test_result['test_count']}")
    print(f"  Coverage: {test_result['coverage']}")
    print(f"  Test code preview:")
    print("-" * 60)
    print(test_result['test_code'][:300] + "...")
    print("-" * 60)
    print()
    
    print("=" * 60)
    print("Custom agent example completed successfully!")
    print("=" * 60)


if __name__ == "__main__":
    main()
