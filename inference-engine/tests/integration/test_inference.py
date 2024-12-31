import unittest
from src.inference.engine import InferenceEngine
from src.utils.helpers import parse_json_to_expression

class TestInferenceEngine(unittest.TestCase):
    def setUp(self):
        self.engine = InferenceEngine()

    def test_full_inference_process(self):
        # Test data
        premises_json = [
            {
                "type": "implication",
                "value": "implies",
                "left": {"type": "proposition", "value": "P"},
                "right": {"type": "proposition", "value": "Q"}
            },
            {"type": "proposition", "value": "P"}
        ]
        
        # Convert JSON to LogicalExpression objects
        premises = [parse_json_to_expression(p) for p in premises_json]
        
        # Apply rules
        results = self.engine.apply_rules(premises)
        
        # Verify results
        self.assertTrue(len(results) > 0)
        self.assertEqual(results[0].value, "Q")
        
        # Verify steps were tracked
        steps = self.engine.step_tracker.get_steps()
        self.assertEqual(len(steps), 1)
        self.assertEqual(steps[0]["rule"], "modus_ponens")

if __name__ == '__main__':
    unittest.main()