"""Workflow Manager - Orchestrate multiple agents in workflows."""

from typing import Dict, Any, List, Optional
from ..core.base_agent import BaseAgent


class WorkflowManager:
    """
    Manage and execute workflows that involve multiple agents.
    
    Workflows allow complex tasks to be broken down and executed
    by different specialized agents in sequence or parallel.
    """
    
    def __init__(self):
        """Initialize the workflow manager."""
        self.workflows: Dict[str, Dict[str, Any]] = {}
        self.execution_history: List[Dict[str, Any]] = []
        
    def create_workflow(self, 
                       name: str, 
                       description: str, 
                       steps: List[Dict[str, Any]]) -> Dict[str, Any]:
        """
        Create a new workflow.
        
        Args:
            name: Unique name for the workflow
            description: Description of what the workflow does
            steps: List of workflow steps, each containing agent and task info
            
        Returns:
            Created workflow configuration
            
        Raises:
            ValueError: If workflow name already exists
        """
        if name in self.workflows:
            raise ValueError(f"Workflow '{name}' already exists")
        
        workflow = {
            "name": name,
            "description": description,
            "steps": steps,
            "status": "created"
        }
        
        self.workflows[name] = workflow
        return workflow
    
    def execute_workflow(self, 
                        name: str, 
                        agents: Dict[str, BaseAgent],
                        initial_context: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """
        Execute a workflow.
        
        Args:
            name: Name of the workflow to execute
            agents: Dictionary mapping agent names to agent instances
            initial_context: Initial context for the workflow
            
        Returns:
            Workflow execution results
            
        Raises:
            ValueError: If workflow doesn't exist
        """
        if name not in self.workflows:
            raise ValueError(f"Workflow '{name}' not found")
        
        workflow = self.workflows[name]
        context = initial_context or {}
        results = []
        
        for i, step in enumerate(workflow["steps"]):
            agent_name = step.get("agent")
            task = step.get("task")
            step_type = step.get("type", "sequential")
            
            if agent_name not in agents:
                return {
                    "success": False,
                    "error": f"Agent '{agent_name}' not found for step {i+1}",
                    "results": results
                }
            
            agent = agents[agent_name]
            
            # Execute the step
            try:
                step_context = {**context, **step.get("context", {})}
                result = agent.execute(task, step_context)
                
                step_result = {
                    "step": i + 1,
                    "agent": agent_name,
                    "task": task,
                    "result": result,
                    "success": result.get("success", True)
                }
                
                results.append(step_result)
                
                # Update context with results for next step
                if result.get("success", True):
                    context.update(result.get("output_context", {}))
                else:
                    # If a step fails, stop the workflow
                    break
                    
            except Exception as e:
                results.append({
                    "step": i + 1,
                    "agent": agent_name,
                    "task": task,
                    "success": False,
                    "error": str(e)
                })
                break
        
        execution_result = {
            "workflow": name,
            "success": all(r.get("success", False) for r in results),
            "steps_completed": len(results),
            "total_steps": len(workflow["steps"]),
            "results": results,
            "final_context": context
        }
        
        self.execution_history.append(execution_result)
        return execution_result
    
    def get_workflow(self, name: str) -> Optional[Dict[str, Any]]:
        """
        Get a workflow by name.
        
        Args:
            name: Workflow name
            
        Returns:
            Workflow configuration or None if not found
        """
        return self.workflows.get(name)
    
    def list_workflows(self) -> List[str]:
        """
        List all workflow names.
        
        Returns:
            List of workflow names
        """
        return list(self.workflows.keys())
    
    def delete_workflow(self, name: str) -> bool:
        """
        Delete a workflow.
        
        Args:
            name: Workflow name
            
        Returns:
            True if deleted, False if not found
        """
        if name in self.workflows:
            del self.workflows[name]
            return True
        return False
    
    def get_execution_history(self) -> List[Dict[str, Any]]:
        """
        Get workflow execution history.
        
        Returns:
            List of workflow execution results
        """
        return self.execution_history.copy()
    
    def validate_workflow(self, name: str, available_agents: List[str]) -> Dict[str, Any]:
        """
        Validate that a workflow can be executed with available agents.
        
        Args:
            name: Workflow name
            available_agents: List of available agent names
            
        Returns:
            Validation result
        """
        if name not in self.workflows:
            return {
                "valid": False,
                "error": f"Workflow '{name}' not found"
            }
        
        workflow = self.workflows[name]
        missing_agents = []
        
        for step in workflow["steps"]:
            agent_name = step.get("agent")
            if agent_name not in available_agents:
                missing_agents.append(agent_name)
        
        if missing_agents:
            return {
                "valid": False,
                "error": "Missing required agents",
                "missing_agents": missing_agents
            }
        
        return {
            "valid": True,
            "message": "Workflow is valid and can be executed"
        }
