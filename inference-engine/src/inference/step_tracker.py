from typing import List, Dict
from .logical_expression import LogicalExpression
from ..utils.helpers import format_expression_to_json

class StepTracker:
    def __init__(self):
        self.steps = []

    def add_step(self, step: Dict):
        """
        Adds an inference step to the tracker
        """
        self.steps.append({
            "step_number": len(self.steps) + 1,
            "rule": step["rule"],
            "premises": [format_expression_to_json(p) for p in step["premises"]],
            "conclusion": format_expression_to_json(step["conclusion"])
        })

    def get_steps(self) -> List[Dict]:
        """
        Returns all tracked steps
        """
        return self.steps