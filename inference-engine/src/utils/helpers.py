from typing import Dict
from ..inference.logical_expression import LogicalExpression

def parse_json_to_expression(json_data: Dict) -> LogicalExpression:
    """
    Converts JSON representation to LogicalExpression objects
    """
    if isinstance(json_data, str):
        return LogicalExpression(expression=json_data)
    
    expr_value = json_data.get("expression", "")
    return LogicalExpression(expression=expr_value)

def format_expression_to_json(expr: LogicalExpression) -> Dict:
    """
    Converts LogicalExpression objects to JSON format
    """
    return {
        "expression": expr.expression
    }