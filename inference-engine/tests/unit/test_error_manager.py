import unittest
from src.utils.error_manager import ErrorManager, ErrorType

class TestErrorManager(unittest.TestCase):
    def setUp(self):
        self.error_manager = ErrorManager()

    def test_error_validation(self):
        # Test invalid input
        invalid_expression = {"type": "invalid"}
        self.assertFalse(self.error_manager.validate_input(invalid_expression))
        
        # Test valid input
        valid_expression = {"type": "proposition", "value": "P"}
        self.assertTrue(self.error_manager.validate_input(valid_expression))

    def test_error_report(self):
        self.error_manager.add_error(
            ErrorType.SYNTAX_ERROR,
            "Invalid syntax",
            {"line": 1, "position": 5}
        )
        
        report = self.error_manager.get_error_report()
        self.assertTrue(report["has_errors"])
        self.assertEqual(len(report["errors"]), 1)
        self.assertEqual(report["errors"][0]["type"], "syntax_error")
