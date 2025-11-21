"""Planning Agent - Specialized agent for project planning and task breakdown."""

from typing import Dict, Any, List, Optional
from ..core.base_agent import BaseAgent


class PlanningAgent(BaseAgent):
    """
    Agent specialized in project planning, task breakdown, and timeline estimation.
    
    Capabilities:
    - Break down complex projects into tasks
    - Estimate time and resources
    - Create project roadmaps
    - Identify dependencies
    - Risk assessment
    """
    
    def __init__(self, name: str, config: Optional[Dict[str, Any]] = None):
        """
        Initialize a planning agent.
        
        Args:
            name: Unique identifier for the agent
            config: Configuration including planning methodologies, etc.
        """
        super().__init__(name, config)
        self.methodology = config.get("methodology", "agile") if config else "agile"
        self.plans: List[Dict[str, Any]] = []
        
    def get_capabilities(self) -> List[str]:
        """Return the capabilities of the planning agent."""
        return [
            "project_decomposition",
            "task_breakdown",
            "timeline_estimation",
            "resource_planning",
            "dependency_mapping",
            "risk_assessment",
            "milestone_definition",
            "roadmap_creation"
        ]
    
    def execute(self, task: str, context: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """
        Execute a planning task.
        
        Args:
            task: Description of the project or feature to plan
            context: Additional context (requirements, constraints, resources, etc.)
            
        Returns:
            Dictionary containing the project plan
        """
        if not self.validate_input(task, context):
            return {
                "success": False,
                "error": "Invalid input provided",
                "plan": None
            }
        
        context = context or {}
        complexity = context.get("complexity", "medium")
        deadline = context.get("deadline", "not specified")
        
        result = {
            "success": True,
            "project": task,
            "methodology": self.methodology,
            "complexity": complexity,
            "deadline": deadline,
            "phases": self._create_phases(task, complexity),
            "tasks": self._breakdown_tasks(task, complexity),
            "timeline": self._estimate_timeline(task, complexity),
            "dependencies": self._identify_dependencies(task),
            "risks": self._assess_risks(task, complexity),
            "milestones": self._define_milestones(task),
            "resources": self._estimate_resources(task, complexity)
        }
        
        self.plans.append(result)
        self.log_execution(task, result)
        
        return result
    
    def _create_phases(self, project: str, complexity: str) -> List[Dict[str, str]]:
        """
        Create project phases.
        
        Args:
            project: Project description
            complexity: Complexity level
            
        Returns:
            List of project phases
        """
        if self.methodology == "agile":
            return [
                {"name": "Sprint Planning", "duration": "1 week"},
                {"name": "Development Sprint 1", "duration": "2 weeks"},
                {"name": "Development Sprint 2", "duration": "2 weeks"},
                {"name": "Testing & QA", "duration": "1 week"},
                {"name": "Deployment", "duration": "3 days"}
            ]
        else:  # waterfall
            return [
                {"name": "Requirements Analysis", "duration": "1 week"},
                {"name": "Design", "duration": "2 weeks"},
                {"name": "Implementation", "duration": "4 weeks"},
                {"name": "Testing", "duration": "2 weeks"},
                {"name": "Deployment", "duration": "1 week"}
            ]
    
    def _breakdown_tasks(self, project: str, complexity: str) -> List[Dict[str, Any]]:
        """
        Break down project into tasks.
        
        Args:
            project: Project description
            complexity: Complexity level
            
        Returns:
            List of tasks with details
        """
        task_count = {"low": 5, "medium": 10, "high": 20}.get(complexity, 10)
        
        tasks = [
            {
                "id": 1,
                "name": f"Research and analysis for {project}",
                "priority": "high",
                "estimated_hours": 8,
                "status": "pending"
            },
            {
                "id": 2,
                "name": "Design architecture and interfaces",
                "priority": "high",
                "estimated_hours": 16,
                "status": "pending"
            },
            {
                "id": 3,
                "name": "Implement core functionality",
                "priority": "high",
                "estimated_hours": 40,
                "status": "pending"
            },
            {
                "id": 4,
                "name": "Create unit tests",
                "priority": "medium",
                "estimated_hours": 16,
                "status": "pending"
            },
            {
                "id": 5,
                "name": "Integration testing",
                "priority": "medium",
                "estimated_hours": 12,
                "status": "pending"
            },
            {
                "id": 6,
                "name": "Documentation",
                "priority": "medium",
                "estimated_hours": 8,
                "status": "pending"
            },
            {
                "id": 7,
                "name": "Code review and refinement",
                "priority": "high",
                "estimated_hours": 8,
                "status": "pending"
            },
            {
                "id": 8,
                "name": "Deployment preparation",
                "priority": "medium",
                "estimated_hours": 4,
                "status": "pending"
            }
        ]
        
        return tasks[:task_count]
    
    def _estimate_timeline(self, project: str, complexity: str) -> Dict[str, Any]:
        """
        Estimate project timeline.
        
        Args:
            project: Project description
            complexity: Complexity level
            
        Returns:
            Timeline estimation
        """
        durations = {
            "low": {"weeks": 2, "hours": 80},
            "medium": {"weeks": 6, "hours": 240},
            "high": {"weeks": 12, "hours": 480}
        }
        
        duration = durations.get(complexity, durations["medium"])
        
        return {
            "total_weeks": duration["weeks"],
            "total_hours": duration["hours"],
            "team_size_recommended": 2 if complexity == "low" else 4 if complexity == "medium" else 6,
            "buffer_percentage": 20
        }
    
    def _identify_dependencies(self, project: str) -> List[Dict[str, Any]]:
        """
        Identify task dependencies.
        
        Args:
            project: Project description
            
        Returns:
            List of dependencies
        """
        return [
            {"task": "Design", "depends_on": ["Research"]},
            {"task": "Implementation", "depends_on": ["Design"]},
            {"task": "Testing", "depends_on": ["Implementation"]},
            {"task": "Deployment", "depends_on": ["Testing"]}
        ]
    
    def _assess_risks(self, project: str, complexity: str) -> List[Dict[str, str]]:
        """
        Assess project risks.
        
        Args:
            project: Project description
            complexity: Complexity level
            
        Returns:
            List of identified risks
        """
        risks = [
            {
                "risk": "Scope creep",
                "impact": "high",
                "probability": "medium",
                "mitigation": "Clear requirements and change management process"
            },
            {
                "risk": "Technical debt",
                "impact": "medium",
                "probability": "medium",
                "mitigation": "Regular code reviews and refactoring sprints"
            },
            {
                "risk": "Integration issues",
                "impact": "high",
                "probability": "low",
                "mitigation": "Early integration testing and API contracts"
            }
        ]
        
        if complexity == "high":
            risks.append({
                "risk": "Resource constraints",
                "impact": "high",
                "probability": "medium",
                "mitigation": "Buffer time and flexible team allocation"
            })
        
        return risks
    
    def _define_milestones(self, project: str) -> List[Dict[str, str]]:
        """
        Define project milestones.
        
        Args:
            project: Project description
            
        Returns:
            List of milestones
        """
        return [
            {"name": "Requirements Complete", "deliverable": "Requirements document"},
            {"name": "Design Approved", "deliverable": "Architecture and design docs"},
            {"name": "MVP Complete", "deliverable": "Minimum viable product"},
            {"name": "Testing Complete", "deliverable": "Test reports and fixes"},
            {"name": "Production Ready", "deliverable": "Deployed application"}
        ]
    
    def _estimate_resources(self, project: str, complexity: str) -> Dict[str, Any]:
        """
        Estimate required resources.
        
        Args:
            project: Project description
            complexity: Complexity level
            
        Returns:
            Resource estimation
        """
        return {
            "developers": 2 if complexity == "low" else 4 if complexity == "medium" else 6,
            "testers": 1 if complexity == "low" else 2,
            "project_manager": 0.5,  # Part-time
            "tools": ["IDE", "Version Control", "CI/CD", "Testing Framework"],
            "infrastructure": ["Development Environment", "Testing Environment", "Production Environment"]
        }
    
    def get_all_plans(self) -> List[Dict[str, Any]]:
        """
        Get all plans created by this agent.
        
        Returns:
            List of all plans
        """
        return self.plans.copy()
