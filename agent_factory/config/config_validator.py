"""Configuration validator for validating agent configurations."""

from typing import Dict, Any, List, Optional


class ConfigValidator:
    """
    Validate configuration dictionaries for agents and factory.
    """
    
    @staticmethod
    def validate_agent_config(config: Dict[str, Any], agent_type: str) -> Dict[str, Any]:
        """
        Validate agent configuration.
        
        Args:
            config: Configuration dictionary to validate
            agent_type: Type of agent (coding, debugging, planning, building)
            
        Returns:
            Validation result with 'valid' boolean and optional 'errors' list
        """
        errors = []
        
        if not isinstance(config, dict):
            return {
                "valid": False,
                "errors": ["Configuration must be a dictionary"]
            }
        
        # Validate based on agent type
        if agent_type == "coding":
            errors.extend(ConfigValidator._validate_coding_config(config))
        elif agent_type == "debugging":
            errors.extend(ConfigValidator._validate_debugging_config(config))
        elif agent_type == "planning":
            errors.extend(ConfigValidator._validate_planning_config(config))
        elif agent_type == "building":
            errors.extend(ConfigValidator._validate_building_config(config))
        
        return {
            "valid": len(errors) == 0,
            "errors": errors if errors else None
        }
    
    @staticmethod
    def _validate_coding_config(config: Dict[str, Any]) -> List[str]:
        """Validate coding agent configuration."""
        errors = []
        
        if "languages" in config:
            if not isinstance(config["languages"], list):
                errors.append("'languages' must be a list")
            elif not all(isinstance(lang, str) for lang in config["languages"]):
                errors.append("All languages must be strings")
        
        if "style_guide" in config:
            if not isinstance(config["style_guide"], str):
                errors.append("'style_guide' must be a string")
        
        return errors
    
    @staticmethod
    def _validate_debugging_config(config: Dict[str, Any]) -> List[str]:
        """Validate debugging agent configuration."""
        errors = []
        
        if "strategies" in config:
            if not isinstance(config["strategies"], list):
                errors.append("'strategies' must be a list")
        
        if "max_bugs_tracked" in config:
            if not isinstance(config["max_bugs_tracked"], int) or config["max_bugs_tracked"] < 0:
                errors.append("'max_bugs_tracked' must be a non-negative integer")
        
        return errors
    
    @staticmethod
    def _validate_planning_config(config: Dict[str, Any]) -> List[str]:
        """Validate planning agent configuration."""
        errors = []
        
        if "methodology" in config:
            valid_methodologies = ["agile", "waterfall", "kanban", "scrum"]
            if config["methodology"] not in valid_methodologies:
                errors.append(f"'methodology' must be one of: {', '.join(valid_methodologies)}")
        
        return errors
    
    @staticmethod
    def _validate_building_config(config: Dict[str, Any]) -> List[str]:
        """Validate building agent configuration."""
        errors = []
        
        if "build_tools" in config:
            if not isinstance(config["build_tools"], list):
                errors.append("'build_tools' must be a list")
        
        if "platforms" in config:
            if not isinstance(config["platforms"], list):
                errors.append("'platforms' must be a list")
        
        return errors
    
    @staticmethod
    def validate_factory_config(config: Dict[str, Any]) -> Dict[str, Any]:
        """
        Validate factory configuration.
        
        Args:
            config: Factory configuration dictionary
            
        Returns:
            Validation result
        """
        errors = []
        
        if not isinstance(config, dict):
            return {
                "valid": False,
                "errors": ["Configuration must be a dictionary"]
            }
        
        # Validate factory section
        if "factory" in config:
            if not isinstance(config["factory"], dict):
                errors.append("'factory' section must be a dictionary")
            else:
                if "max_agents" in config["factory"]:
                    if not isinstance(config["factory"]["max_agents"], int) or config["factory"]["max_agents"] < 1:
                        errors.append("'max_agents' must be a positive integer")
        
        # Validate workflows section
        if "workflows" in config:
            if not isinstance(config["workflows"], dict):
                errors.append("'workflows' section must be a dictionary")
            else:
                if "timeout_seconds" in config["workflows"]:
                    if not isinstance(config["workflows"]["timeout_seconds"], int) or config["workflows"]["timeout_seconds"] < 1:
                        errors.append("'timeout_seconds' must be a positive integer")
        
        return {
            "valid": len(errors) == 0,
            "errors": errors if errors else None
        }
    
    @staticmethod
    def validate_workflow_config(workflow: Dict[str, Any]) -> Dict[str, Any]:
        """
        Validate workflow configuration.
        
        Args:
            workflow: Workflow configuration dictionary
            
        Returns:
            Validation result
        """
        errors = []
        
        if not isinstance(workflow, dict):
            return {
                "valid": False,
                "errors": ["Workflow must be a dictionary"]
            }
        
        # Required fields
        if "name" not in workflow:
            errors.append("Workflow must have a 'name' field")
        elif not isinstance(workflow["name"], str):
            errors.append("Workflow 'name' must be a string")
        
        if "steps" not in workflow:
            errors.append("Workflow must have a 'steps' field")
        elif not isinstance(workflow["steps"], list):
            errors.append("Workflow 'steps' must be a list")
        else:
            # Validate each step
            for i, step in enumerate(workflow["steps"]):
                if not isinstance(step, dict):
                    errors.append(f"Step {i+1} must be a dictionary")
                    continue
                
                if "agent" not in step:
                    errors.append(f"Step {i+1} must have an 'agent' field")
                
                if "task" not in step:
                    errors.append(f"Step {i+1} must have a 'task' field")
        
        return {
            "valid": len(errors) == 0,
            "errors": errors if errors else None
        }
