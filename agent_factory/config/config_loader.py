"""Configuration loader for loading agent and factory configurations."""

import json
import yaml
from typing import Dict, Any, Optional
from pathlib import Path


class ConfigLoader:
    """
    Load and parse configuration files for agents and the factory.
    
    Supports JSON and YAML formats.
    """
    
    @staticmethod
    def load_from_file(file_path: str) -> Dict[str, Any]:
        """
        Load configuration from a file.
        
        Args:
            file_path: Path to the configuration file
            
        Returns:
            Configuration dictionary
            
        Raises:
            FileNotFoundError: If file doesn't exist
            ValueError: If file format is not supported
        """
        path = Path(file_path)
        
        if not path.exists():
            raise FileNotFoundError(f"Configuration file not found: {file_path}")
        
        if path.suffix == ".json":
            return ConfigLoader.load_json(file_path)
        elif path.suffix in [".yaml", ".yml"]:
            return ConfigLoader.load_yaml(file_path)
        else:
            raise ValueError(f"Unsupported file format: {path.suffix}")
    
    @staticmethod
    def load_json(file_path: str) -> Dict[str, Any]:
        """
        Load configuration from a JSON file.
        
        Args:
            file_path: Path to the JSON file
            
        Returns:
            Configuration dictionary
        """
        with open(file_path, 'r') as f:
            return json.load(f)
    
    @staticmethod
    def load_yaml(file_path: str) -> Dict[str, Any]:
        """
        Load configuration from a YAML file.
        
        Args:
            file_path: Path to the YAML file
            
        Returns:
            Configuration dictionary
        """
        try:
            with open(file_path, 'r') as f:
                return yaml.safe_load(f)
        except NameError:
            # yaml module not available
            raise ImportError("PyYAML is required to load YAML files. Install it with: pip install pyyaml")
    
    @staticmethod
    def load_from_dict(config_dict: Dict[str, Any]) -> Dict[str, Any]:
        """
        Load configuration from a dictionary.
        
        Args:
            config_dict: Configuration dictionary
            
        Returns:
            Configuration dictionary (validated copy)
        """
        return config_dict.copy()
    
    @staticmethod
    def save_to_file(config: Dict[str, Any], file_path: str, format: str = "json"):
        """
        Save configuration to a file.
        
        Args:
            config: Configuration dictionary
            file_path: Path to save the file
            format: File format (json or yaml)
        """
        path = Path(file_path)
        path.parent.mkdir(parents=True, exist_ok=True)
        
        if format == "json":
            with open(file_path, 'w') as f:
                json.dump(config, f, indent=2)
        elif format in ["yaml", "yml"]:
            try:
                with open(file_path, 'w') as f:
                    yaml.dump(config, f, default_flow_style=False)
            except NameError:
                raise ImportError("PyYAML is required to save YAML files")
        else:
            raise ValueError(f"Unsupported format: {format}")
    
    @staticmethod
    def get_default_config() -> Dict[str, Any]:
        """
        Get default configuration for the agent factory.
        
        Returns:
            Default configuration dictionary
        """
        return {
            "factory": {
                "name": "AgentFactory",
                "version": "1.0.0",
                "max_agents": 100
            },
            "agents": {
                "coding": {
                    "languages": ["Python", "JavaScript", "Java", "C++", "Go"],
                    "style_guide": "default"
                },
                "debugging": {
                    "strategies": ["print_debugging", "breakpoint_analysis", "log_analysis"],
                    "max_bugs_tracked": 1000
                },
                "planning": {
                    "methodology": "agile",
                    "default_complexity": "medium"
                },
                "building": {
                    "build_tools": ["Maven", "Gradle", "npm", "pip"],
                    "platforms": ["GitHub Actions", "Jenkins", "GitLab CI"]
                }
            },
            "workflows": {
                "timeout_seconds": 3600,
                "max_concurrent_workflows": 10
            }
        }
