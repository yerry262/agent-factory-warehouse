"""Debugging Agent - Specialized agent for finding and fixing bugs."""

from typing import Dict, Any, List, Optional
from ..core.base_agent import BaseAgent


class DebuggingAgent(BaseAgent):
    """
    Agent specialized in debugging, error analysis, and bug fixing.
    
    Capabilities:
    - Analyze error messages and stack traces
    - Suggest fixes for common bugs
    - Identify potential issues in code
    - Provide debugging strategies
    - Track and log bugs
    """
    
    def __init__(self, name: str, config: Optional[Dict[str, Any]] = None):
        """
        Initialize a debugging agent.
        
        Args:
            name: Unique identifier for the agent
            config: Configuration including debugging strategies, tools, etc.
        """
        super().__init__(name, config)
        self.debugging_strategies = config.get("strategies", [
            "print_debugging",
            "breakpoint_analysis",
            "log_analysis",
            "unit_testing"
        ]) if config else ["print_debugging", "breakpoint_analysis", "log_analysis", "unit_testing"]
        self.bug_database: List[Dict[str, Any]] = []
        
    def get_capabilities(self) -> List[str]:
        """Return the capabilities of the debugging agent."""
        return [
            "error_analysis",
            "stack_trace_parsing",
            "bug_identification",
            "fix_suggestion",
            "root_cause_analysis",
            "debugging_strategy_recommendation",
            "bug_tracking"
        ]
    
    def execute(self, task: str, context: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """
        Execute a debugging task.
        
        Args:
            task: Description of the debugging task or error message
            context: Additional context (code, stack trace, environment, etc.)
            
        Returns:
            Dictionary containing debugging analysis and suggested fixes
        """
        if not self.validate_input(task, context):
            return {
                "success": False,
                "error": "Invalid input provided",
                "analysis": None
            }
        
        context = context or {}
        error_type = context.get("error_type", "unknown")
        code = context.get("code", "")
        stack_trace = context.get("stack_trace", "")
        
        result = {
            "success": True,
            "task": task,
            "error_type": error_type,
            "analysis": self._analyze_error(task, error_type, stack_trace),
            "suggested_fixes": self._suggest_fixes(task, error_type, code),
            "debugging_strategy": self._recommend_strategy(error_type),
            "severity": self._assess_severity(error_type),
            "similar_bugs": self._find_similar_bugs(task)
        }
        
        # Log the bug
        self._log_bug(task, error_type, result)
        self.log_execution(task, result)
        
        return result
    
    def _analyze_error(self, error_msg: str, error_type: str, stack_trace: str) -> Dict[str, Any]:
        """
        Analyze an error message and stack trace.
        
        Args:
            error_msg: Error message
            error_type: Type of error
            stack_trace: Stack trace if available
            
        Returns:
            Analysis results
        """
        return {
            "error_message": error_msg,
            "error_type": error_type,
            "likely_causes": self._identify_causes(error_type),
            "stack_trace_summary": self._parse_stack_trace(stack_trace),
            "affected_components": ["module_to_be_determined"]
        }
    
    def _identify_causes(self, error_type: str) -> List[str]:
        """
        Identify likely causes for an error type.
        
        Args:
            error_type: Type of error
            
        Returns:
            List of likely causes
        """
        common_causes = {
            "NullPointerException": ["Uninitialized variable", "Null return value", "Missing null check"],
            "IndexError": ["Array out of bounds", "Empty collection access", "Off-by-one error"],
            "TypeError": ["Wrong data type", "Invalid operation", "Missing type conversion"],
            "SyntaxError": ["Typo in code", "Missing bracket/parenthesis", "Invalid syntax"],
            "unknown": ["Check input data", "Review recent changes", "Verify dependencies"]
        }
        return common_causes.get(error_type, common_causes["unknown"])
    
    def _suggest_fixes(self, error_msg: str, error_type: str, code: str) -> List[str]:
        """
        Suggest potential fixes for the error.
        
        Args:
            error_msg: Error message
            error_type: Type of error
            code: Code that caused the error
            
        Returns:
            List of suggested fixes
        """
        return [
            "Add null/None checks before accessing objects",
            "Validate input parameters",
            "Add try-catch/try-except blocks",
            "Check array/list bounds before access",
            "Review initialization sequence",
            "Add defensive programming checks"
        ]
    
    def _recommend_strategy(self, error_type: str) -> str:
        """
        Recommend a debugging strategy.
        
        Args:
            error_type: Type of error
            
        Returns:
            Recommended debugging strategy
        """
        strategies = {
            "NullPointerException": "Use breakpoint debugging to track variable initialization",
            "IndexError": "Add logging to track collection sizes and access patterns",
            "TypeError": "Add type hints and use a type checker",
            "SyntaxError": "Use IDE syntax highlighting and linting tools"
        }
        return strategies.get(error_type, "Use systematic print/log debugging")
    
    def _assess_severity(self, error_type: str) -> str:
        """
        Assess the severity of an error.
        
        Args:
            error_type: Type of error
            
        Returns:
            Severity level (critical, high, medium, low)
        """
        critical_errors = ["MemoryError", "StackOverflowError", "SecurityException"]
        high_errors = ["NullPointerException", "IndexError"]
        
        if error_type in critical_errors:
            return "critical"
        elif error_type in high_errors:
            return "high"
        else:
            return "medium"
    
    def _parse_stack_trace(self, stack_trace: str) -> str:
        """
        Parse and summarize a stack trace.
        
        Args:
            stack_trace: Stack trace string
            
        Returns:
            Summary of the stack trace
        """
        if not stack_trace:
            return "No stack trace provided"
        
        lines = stack_trace.split('\n')
        return f"Stack trace has {len(lines)} frames. Review the most recent calls."
    
    def _log_bug(self, description: str, error_type: str, analysis: Dict[str, Any]):
        """
        Log a bug to the internal database.
        
        Args:
            description: Bug description
            error_type: Type of error
            analysis: Analysis results
        """
        self.bug_database.append({
            "description": description,
            "error_type": error_type,
            "analysis": analysis,
            "timestamp": self.created_at
        })
    
    def _find_similar_bugs(self, description: str) -> List[str]:
        """
        Find similar bugs in the database.
        
        Args:
            description: Bug description
            
        Returns:
            List of similar bug descriptions
        """
        # Simple similarity check (in production, use more sophisticated matching)
        similar = []
        for bug in self.bug_database[-5:]:  # Check last 5 bugs
            if any(word in bug["description"].lower() for word in description.lower().split()):
                similar.append(bug["description"][:100])
        return similar
    
    def get_bug_statistics(self) -> Dict[str, Any]:
        """
        Get statistics about bugs found by this agent.
        
        Returns:
            Dictionary with bug statistics
        """
        return {
            "total_bugs": len(self.bug_database),
            "error_types": list(set(bug["error_type"] for bug in self.bug_database)),
            "recent_bugs": self.bug_database[-5:]
        }
