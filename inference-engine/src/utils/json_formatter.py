from typing import Any, Dict, List
import json
from datetime import datetime

class JsonFormatter:
    @staticmethod
    def format_inference_result(
        input_expression: Dict,
        steps: List[Dict],
        result: Dict,
        performance_data: Dict
    ) -> Dict:
        """
        Formats the complete inference process result as JSON
        """
        return {
            "timestamp": datetime.now().isoformat(),
            "input": input_expression,
            "steps": [JsonFormatter.format_step(step) for step in steps],
            "result": result,
            "performance": performance_data
        }

    @staticmethod
    def format_step(step: Dict) -> Dict:
        """
        Formats a single inference step
        """
        return {
            "step_number": step.get("step_number"),
            "rule_applied": step.get("rule"),
            "premises": step.get("premises", []),
            "conclusion": step.get("conclusion"),
            "explanation": step.get("explanation", "")
        }

    @staticmethod
    def to_human_readable(data: Dict) -> str:
        """
        Converts JSON data to human-readable format
        """
        return json.dumps(data, indent=2, ensure_ascii=False)

    @staticmethod
    def validate_json_structure(data: Dict, schema: Dict) -> bool:
        """
        Validates JSON structure against a schema
        """
        try:
            # Simple schema validation
            for key, expected_type in schema.items():
                if key not in data:
                    return False
                if not isinstance(data[key], expected_type):
                    return False
            return True
        except Exception:
            return False
