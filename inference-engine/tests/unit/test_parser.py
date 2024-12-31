import unittest
from src.parsers.parser import LogicalExpressionParserWrapper

class TestLogicalExpressionParserWrapper(unittest.TestCase):
    def setUp(self):
        self.parser = LogicalExpressionParserWrapper()

    def test_parse_simple_expression(self):
        expression = "A AND B"
        result = self.parser.parse(expression)
        self.assertIn("tree", result)
        self.assertIsInstance(result["tree"], str)

    def test_parse_complex_expression(self):
        expression = "forall x (P(x) AND Q(x))"
        result = self.parser.parse(expression)
        self.assertIn("tree", result)
        self.assertIsInstance(result["tree"], str)

    def test_parse_invalid_expression(self):
        expression = "A XOR B"
        with self.assertRaises(Exception):
            self.parser.parse(expression)

if __name__ == '__main__':
    unittest.main()