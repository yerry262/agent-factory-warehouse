"""Building Agent - Specialized agent for build automation and CI/CD tasks."""

from typing import Dict, Any, List, Optional
from ..core.base_agent import BaseAgent


class BuildingAgent(BaseAgent):
    """
    Agent specialized in build automation, CI/CD, and deployment tasks.
    
    Capabilities:
    - Configure build systems
    - Create CI/CD pipelines
    - Manage dependencies
    - Automate testing
    - Handle deployments
    """
    
    def __init__(self, name: str, config: Optional[Dict[str, Any]] = None):
        """
        Initialize a building agent.
        
        Args:
            name: Unique identifier for the agent
            config: Configuration including build tools, platforms, etc.
        """
        super().__init__(name, config)
        self.build_tools = config.get("build_tools", [
            "Maven", "Gradle", "npm", "pip", "Docker"
        ]) if config else ["Maven", "Gradle", "npm", "pip", "Docker"]
        self.platforms = config.get("platforms", [
            "Jenkins", "GitHub Actions", "GitLab CI", "CircleCI"
        ]) if config else ["Jenkins", "GitHub Actions", "GitLab CI", "CircleCI"]
        self.build_history: List[Dict[str, Any]] = []
        
    def get_capabilities(self) -> List[str]:
        """Return the capabilities of the building agent."""
        return [
            "build_configuration",
            "ci_cd_pipeline_creation",
            "dependency_management",
            "automated_testing",
            "deployment_automation",
            "container_orchestration",
            "build_optimization",
            "artifact_management"
        ]
    
    def execute(self, task: str, context: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """
        Execute a building/deployment task.
        
        Args:
            task: Description of the build task
            context: Additional context (platform, language, environment, etc.)
            
        Returns:
            Dictionary containing build configuration and results
        """
        if not self.validate_input(task, context):
            return {
                "success": False,
                "error": "Invalid input provided",
                "build": None
            }
        
        context = context or {}
        platform = context.get("platform", "GitHub Actions")
        language = context.get("language", "Python")
        environment = context.get("environment", "production")
        
        result = {
            "success": True,
            "task": task,
            "platform": platform,
            "language": language,
            "environment": environment,
            "build_config": self._generate_build_config(platform, language),
            "pipeline": self._create_pipeline(platform, language, environment),
            "dependencies": self._manage_dependencies(language),
            "tests": self._configure_tests(language),
            "deployment": self._configure_deployment(platform, environment),
            "optimization_tips": self._suggest_optimizations(platform)
        }
        
        self.build_history.append(result)
        self.log_execution(task, result)
        
        return result
    
    def _generate_build_config(self, platform: str, language: str) -> Dict[str, Any]:
        """
        Generate build configuration.
        
        Args:
            platform: CI/CD platform
            language: Programming language
            
        Returns:
            Build configuration
        """
        configs = {
            "GitHub Actions": self._github_actions_config(language),
            "Jenkins": self._jenkins_config(language),
            "GitLab CI": self._gitlab_ci_config(language),
            "CircleCI": self._circleci_config(language)
        }
        
        return configs.get(platform, configs["GitHub Actions"])
    
    def _github_actions_config(self, language: str) -> Dict[str, Any]:
        """Generate GitHub Actions configuration."""
        config = {
            "name": "CI/CD Pipeline",
            "on": ["push", "pull_request"],
            "jobs": {
                "build": {
                    "runs-on": "ubuntu-latest",
                    "steps": []
                }
            }
        }
        
        if language == "Python":
            config["jobs"]["build"]["steps"] = [
                {"name": "Checkout code", "uses": "actions/checkout@v3"},
                {"name": "Set up Python", "uses": "actions/setup-python@v4", "with": {"python-version": "3.9"}},
                {"name": "Install dependencies", "run": "pip install -r requirements.txt"},
                {"name": "Run tests", "run": "pytest"},
                {"name": "Build", "run": "python setup.py build"}
            ]
        elif language == "JavaScript":
            config["jobs"]["build"]["steps"] = [
                {"name": "Checkout code", "uses": "actions/checkout@v3"},
                {"name": "Set up Node.js", "uses": "actions/setup-node@v3", "with": {"node-version": "18"}},
                {"name": "Install dependencies", "run": "npm install"},
                {"name": "Run tests", "run": "npm test"},
                {"name": "Build", "run": "npm run build"}
            ]
        
        return config
    
    def _jenkins_config(self, language: str) -> Dict[str, Any]:
        """Generate Jenkins pipeline configuration."""
        return {
            "pipeline": "declarative",
            "agent": "any",
            "stages": [
                {"name": "Checkout", "steps": ["checkout scm"]},
                {"name": "Build", "steps": [f"Build for {language}"]},
                {"name": "Test", "steps": ["Run tests"]},
                {"name": "Deploy", "steps": ["Deploy to environment"]}
            ]
        }
    
    def _gitlab_ci_config(self, language: str) -> Dict[str, Any]:
        """Generate GitLab CI configuration."""
        return {
            "image": f"{language.lower()}:latest",
            "stages": ["build", "test", "deploy"],
            "build_job": {
                "stage": "build",
                "script": [f"Build {language} project"]
            },
            "test_job": {
                "stage": "test",
                "script": ["Run tests"]
            }
        }
    
    def _circleci_config(self, language: str) -> Dict[str, Any]:
        """Generate CircleCI configuration."""
        return {
            "version": 2.1,
            "jobs": {
                "build": {
                    "docker": [{"image": f"circleci/{language.lower()}:latest"}],
                    "steps": ["checkout", "run: Install dependencies", "run: Build", "run: Test"]
                }
            }
        }
    
    def _create_pipeline(self, platform: str, language: str, environment: str) -> List[Dict[str, str]]:
        """
        Create a CI/CD pipeline.
        
        Args:
            platform: CI/CD platform
            language: Programming language
            environment: Deployment environment
            
        Returns:
            List of pipeline stages
        """
        return [
            {"stage": "Source", "action": "Checkout code from repository"},
            {"stage": "Build", "action": f"Compile {language} code and create artifacts"},
            {"stage": "Test", "action": "Run unit tests and integration tests"},
            {"stage": "Quality", "action": "Code quality analysis and security scanning"},
            {"stage": "Deploy", "action": f"Deploy to {environment} environment"},
            {"stage": "Verify", "action": "Smoke tests and health checks"}
        ]
    
    def _manage_dependencies(self, language: str) -> Dict[str, Any]:
        """
        Manage project dependencies.
        
        Args:
            language: Programming language
            
        Returns:
            Dependency management configuration
        """
        dependency_files = {
            "Python": "requirements.txt",
            "JavaScript": "package.json",
            "Java": "pom.xml",
            "Go": "go.mod",
            "Rust": "Cargo.toml"
        }
        
        return {
            "file": dependency_files.get(language, "dependencies.txt"),
            "package_manager": self._get_package_manager(language),
            "install_command": self._get_install_command(language),
            "update_strategy": "semantic versioning"
        }
    
    def _get_package_manager(self, language: str) -> str:
        """Get package manager for a language."""
        managers = {
            "Python": "pip",
            "JavaScript": "npm",
            "Java": "maven",
            "Go": "go modules",
            "Rust": "cargo"
        }
        return managers.get(language, "unknown")
    
    def _get_install_command(self, language: str) -> str:
        """Get dependency install command for a language."""
        commands = {
            "Python": "pip install -r requirements.txt",
            "JavaScript": "npm install",
            "Java": "mvn install",
            "Go": "go mod download",
            "Rust": "cargo build"
        }
        return commands.get(language, "install dependencies")
    
    def _configure_tests(self, language: str) -> Dict[str, Any]:
        """
        Configure automated testing.
        
        Args:
            language: Programming language
            
        Returns:
            Test configuration
        """
        test_frameworks = {
            "Python": {"framework": "pytest", "command": "pytest"},
            "JavaScript": {"framework": "Jest", "command": "npm test"},
            "Java": {"framework": "JUnit", "command": "mvn test"},
            "Go": {"framework": "testing", "command": "go test ./..."},
            "Rust": {"framework": "cargo test", "command": "cargo test"}
        }
        
        framework_config = test_frameworks.get(language, {"framework": "unknown", "command": "test"})
        
        return {
            "framework": framework_config["framework"],
            "command": framework_config["command"],
            "coverage": "enabled",
            "coverage_threshold": 80,
            "test_types": ["unit", "integration", "e2e"]
        }
    
    def _configure_deployment(self, platform: str, environment: str) -> Dict[str, Any]:
        """
        Configure deployment strategy.
        
        Args:
            platform: CI/CD platform
            environment: Target environment
            
        Returns:
            Deployment configuration
        """
        return {
            "strategy": "blue-green" if environment == "production" else "rolling",
            "environment": environment,
            "approval_required": environment == "production",
            "rollback_enabled": True,
            "health_checks": ["api_endpoint", "database_connection"],
            "monitoring": ["logs", "metrics", "alerts"]
        }
    
    def _suggest_optimizations(self, platform: str) -> List[str]:
        """
        Suggest build optimizations.
        
        Args:
            platform: CI/CD platform
            
        Returns:
            List of optimization suggestions
        """
        return [
            "Enable caching for dependencies",
            "Parallelize test execution",
            "Use build matrix for multiple environments",
            "Implement incremental builds",
            "Optimize Docker layer caching",
            "Use artifact storage for build outputs"
        ]
    
    def get_build_history(self) -> List[Dict[str, Any]]:
        """
        Get build history.
        
        Returns:
            List of all builds executed by this agent
        """
        return self.build_history.copy()
    
    def analyze_build_performance(self) -> Dict[str, Any]:
        """
        Analyze build performance metrics.
        
        Returns:
            Build performance analysis
        """
        if not self.build_history:
            return {"message": "No build history available"}
        
        return {
            "total_builds": len(self.build_history),
            "platforms_used": list(set(build["platform"] for build in self.build_history)),
            "languages_built": list(set(build["language"] for build in self.build_history)),
            "success_rate": "100%"  # Simulated
        }
