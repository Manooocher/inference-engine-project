from sympy import symbols, And, Or, Not
from typing import List, Dict
from .logical_expression import LogicalExpression
from .step_tracker import StepTracker

class RuleType:
    MODUS_PONENS = "Modus Ponens"
    MODUS_TOLLENS = "Modus Tollens"

class InferenceRules:
    def modus_ponens(self, p1: LogicalExpression, p2: LogicalExpression) -> LogicalExpression:
        # پیاده‌سازی قانون Modus Ponens
        if p1.expression == f"IF {p2.expression} THEN X":
            return LogicalExpression("X")
        return None

    def modus_tollens(self, p1: LogicalExpression, p2: LogicalExpression) -> LogicalExpression:
        # پیاده‌سازی قانون Modus Tollens
        if p1.expression == f"IF X THEN {p2.expression}":
            return LogicalExpression("NOT X")
        return None

class InferenceEngine:
    def __init__(self):
        self.knowledge_base = set()
        self.rules = InferenceRules()
        self.step_tracker = StepTracker()

    def add_fact(self, fact: str):
        self.knowledge_base.add(fact.upper())

    def add_rule(self, if_clause: str, then_clause: str):
        self.rules.append({
            'if': if_clause.upper(),
            'then': then_clause.upper()
        })

    def evaluate(self, expression: str) -> dict:
        expression = expression.upper()
        parts = expression.split()

        try:
            result = self._evaluate_expression(parts)
            return {
                'success': True,
                'result': result,
                'knowledge_base': list(self.knowledge_base)
            }
        except Exception as e:
            return {
                'success': False,
                'error': str(e)
            }

    def _evaluate_expression(self, parts: list) -> bool:
        if not parts:
            return False

        if 'AND' in parts:
            idx = parts.index('AND')
            left = parts[:idx]
            right = parts[idx + 1:]
            return self._evaluate_expression(left) and self._evaluate_expression(right)

        if 'OR' in parts:
            idx = parts.index('OR')
            left = parts[:idx]
            right = parts[idx + 1:]
            return self._evaluate_expression(left) or self._evaluate_expression(right)

        if 'NOT' in parts:
            return not self._evaluate_expression(parts[1:])

        return ' '.join(parts) in self.knowledge_base

    def apply_rules(self, premises: List[LogicalExpression]) -> List[Dict]:
        """
        Applies inference rules to the given premises and tracks steps
        """
        results = []
        for i, p1 in enumerate(premises):
            for j, p2 in enumerate(premises[i+1:], i+1):
                # Try Modus Ponens
                result = self.rules.modus_ponens(p1, p2)
                if result:
                    step = {
                        "rule": RuleType.MODUS_PONENS,
                        "premises": [p1, p2],
                        "conclusion": result
                    }
                    self.step_tracker.add_step(step)
                    results.append(result)

                # Try Modus Tollens
                result = self.rules.modus_tollens(p1, p2)
                if result:
                    step = {
                        "rule": RuleType.MODUS_TOLLENS,
                        "premises": [p1, p2],
                        "conclusion": result
                    }
                    self.step_tracker.add_step(step)
                    results.append(result)
        return results