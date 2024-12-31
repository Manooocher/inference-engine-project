from dataclasses import dataclass
from typing import List, Optional, Dict
from enum import Enum

class RuleType(Enum):
    MODUS_PONENS = "modus_ponens"
    MODUS_TOLLENS = "modus_tollens"
    CONTRADICTION = "contradiction"

@dataclass
class LogicalExpression:
    type: str
    value: str
    left: Optional['LogicalExpression'] = None
    right: Optional['LogicalExpression'] = None

class InferenceRules:
    @staticmethod
    def modus_ponens(premise1: LogicalExpression, premise2: LogicalExpression) -> Optional[LogicalExpression]:
        """
        Applies Modus Ponens rule: if P → Q and P, then Q
        """
        if premise1.type == "implication" and premise1.left == premise2:
            return premise1.right
        return None

    @staticmethod
    def modus_tollens(premise1: LogicalExpression, premise2: LogicalExpression) -> Optional[LogicalExpression]:
        """
        Applies Modus Tollens rule: if P → Q and ¬Q, then ¬P
        """
        if (premise1.type == "implication" and 
            premise2.type == "negation" and 
            premise2.value == premise1.right.value):
            return LogicalExpression(type="negation", value=premise1.left.value)
        return None

    @staticmethod
    def contradiction_elimination(premise: LogicalExpression) -> Optional[LogicalExpression]:
        """
        Applies Contradiction Elimination: if P ∧ ¬P, then Q (for any Q)
        """
        if (premise.type == "and" and
            premise.left.type == "proposition" and
            premise.right.type == "negation" and
            premise.left.value == premise.right.value):
            return LogicalExpression(type="proposition", value="TRUE")
        return None
