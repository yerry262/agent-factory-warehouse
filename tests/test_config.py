"""Tests for configuration management."""

import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
from agent_factory.config import ConfigLoader, ConfigValidator


class TestConfigLoader:
    """Test the ConfigLoader class."""
    
    def test_get_default_config(self):
        """Test getting default configuration."""
        config = ConfigLoader.get_default_config()
        
        assert config is not None
        assert "factory" in config
        assert "agents" in config
        assert "workflows" in config
        
    def test_load_from_dict(self):
        """Test loading configuration from dictionary."""
        test_config = {
            "factory": {"name": "TestFactory"},
            "agents": {"coding": {"languages": ["Python"]}}
        }
        
        config = ConfigLoader.load_from_dict(test_config)
        assert config["factory"]["name"] == "TestFactory"
        assert config["agents"]["coding"]["languages"] == ["Python"]


class TestConfigValidator:
    """Test the ConfigValidator class."""
    
    def test_validate_coding_config(self):
        """Test validating coding agent configuration."""
        valid_config = {
            "languages": ["Python", "JavaScript"],
            "style_guide": "PEP8"
        }
        
        result = ConfigValidator.validate_agent_config(valid_config, "coding")
        assert result["valid"] is True
        assert result["errors"] is None
        
    def test_validate_coding_config_invalid(self):
        """Test validating invalid coding agent configuration."""
        invalid_config = {
            "languages": "Python",  # Should be a list
            "style_guide": "PEP8"
        }
        
        result = ConfigValidator.validate_agent_config(invalid_config, "coding")
        assert result["valid"] is False
        assert len(result["errors"]) > 0
        
    def test_validate_debugging_config(self):
        """Test validating debugging agent configuration."""
        valid_config = {
            "strategies": ["print_debugging", "log_analysis"],
            "max_bugs_tracked": 100
        }
        
        result = ConfigValidator.validate_agent_config(valid_config, "debugging")
        assert result["valid"] is True
        
    def test_validate_planning_config(self):
        """Test validating planning agent configuration."""
        valid_config = {
            "methodology": "agile"
        }
        
        result = ConfigValidator.validate_agent_config(valid_config, "planning")
        assert result["valid"] is True
        
    def test_validate_planning_config_invalid(self):
        """Test validating invalid planning agent configuration."""
        invalid_config = {
            "methodology": "invalid_method"
        }
        
        result = ConfigValidator.validate_agent_config(invalid_config, "planning")
        assert result["valid"] is False
        
    def test_validate_factory_config(self):
        """Test validating factory configuration."""
        valid_config = {
            "factory": {
                "name": "TestFactory",
                "max_agents": 50
            },
            "workflows": {
                "timeout_seconds": 3600
            }
        }
        
        result = ConfigValidator.validate_factory_config(valid_config)
        assert result["valid"] is True
        
    def test_validate_factory_config_invalid(self):
        """Test validating invalid factory configuration."""
        invalid_config = {
            "factory": {
                "max_agents": -1  # Should be positive
            }
        }
        
        result = ConfigValidator.validate_factory_config(invalid_config)
        assert result["valid"] is False
        
    def test_validate_workflow_config(self):
        """Test validating workflow configuration."""
        valid_workflow = {
            "name": "test_workflow",
            "description": "Test workflow",
            "steps": [
                {"agent": "coder", "task": "Write code"},
                {"agent": "debugger", "task": "Debug code"}
            ]
        }
        
        result = ConfigValidator.validate_workflow_config(valid_workflow)
        assert result["valid"] is True
        
    def test_validate_workflow_config_missing_name(self):
        """Test validating workflow without name."""
        invalid_workflow = {
            "steps": [{"agent": "coder", "task": "Write code"}]
        }
        
        result = ConfigValidator.validate_workflow_config(invalid_workflow)
        assert result["valid"] is False
        
    def test_validate_workflow_config_missing_steps(self):
        """Test validating workflow without steps."""
        invalid_workflow = {
            "name": "test_workflow"
        }
        
        result = ConfigValidator.validate_workflow_config(invalid_workflow)
        assert result["valid"] is False


if __name__ == "__main__":
    # Run tests
    pytest.main([__file__, "-v"])
