import unittest
from src.inference.rules import InferenceRules, LogicalExpression

class TestInferenceRules(unittest.TestCase):
    def setUp(self):
        self.rules = InferenceRules()

    def test_modus_ponens(self):
        # IF P THEN Q
        premise1 = LogicalExpression("IF P THEN Q")
        # P
        premise2 = LogicalExpression("P")
        
        result = self.rules.modus_ponens(premise1, premise2)
        self.assertIsNotNone(result)
        self.assertEqual(result.expression, "X")

    def test_modus_tollens(self):
        # IF X THEN Q
        premise1 = LogicalExpression("IF X THEN Q")
        # Q
        premise2 = LogicalExpression("Q")
        
        result = self.rules.modus_tollens(premise1, premise2)
        self.assertIsNotNone(result)
        self.assertEqual(result.expression, "NOT X")

if __name__ == '__main__':
    unittest.main()