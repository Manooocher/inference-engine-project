import unittest
from src.utils.json_formatter import JsonFormatter

class TestJsonFormatter(unittest.TestCase):
    def setUp(self):
        self.formatter = JsonFormatter()
        self.test_data = {
            "input": {"type": "proposition", "value": "P"},
            "steps": [{"step_number": 1, "rule": "modus_ponens"}],
            "result": {"type": "proposition", "value": "Q"},
            "performance": {"execution_time_ms": 100}
        }

    def test_format_inference_result(self):
        result = self.formatter.format_inference_result(
            self.test_data["input"],
            self.test_data["steps"],
            self.test_data["result"],
            self.test_data["performance"]
        )
        
        self.assertIn("timestamp", result)
        self.assertEqual(result["input"], self.test_data["input"])
        self.assertEqual(len(result["steps"]), 1)
