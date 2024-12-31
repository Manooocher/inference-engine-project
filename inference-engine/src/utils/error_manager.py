from dataclasses import dataclass
from typing import Dict, Optional, List
import json
from enum import Enum
import traceback

class ErrorType(Enum):
    SYNTAX_ERROR = "syntax_error"
    LOGICAL_ERROR = "logical_error"
    VALIDATION_ERROR = "validation_error"
    RUNTIME_ERROR = "runtime_error"

@dataclass
class InferenceError:
    type: ErrorType
    message: str
    details: Optional[Dict] = None
    traceback: Optional[str] = None

class ErrorManager:
    def __init__(self):
        self.errors: List[InferenceError] = []

    def add_error(self, error_type: ErrorType, message: str, details: Optional[Dict] = None) -> None:
        """
        Adds a new error to the error list with optional details
        """
        error = InferenceError(
            type=error_type,
            message=message,
            details=details,
            traceback=traceback.format_exc()
        )
        self.errors.append(error)

    def has_errors(self) -> bool:
        """
        Checks if any errors have been recorded
        """
        return len(self.errors) > 0

    def get_error_report(self) -> Dict:
        """
        Generates a JSON-formatted error report
        """
        return {
            "has_errors": self.has_errors(),
            "error_count": len(self.errors),
            "errors": [
                {
                    "type": error.type.value,
                    "message": error.message,
                    "details": error.details,
                    "traceback": error.traceback
                }
                for error in self.errors
            ]
        }

    def validate_input(self, expression: Dict) -> bool:
        """
        Validates input expression format
        """
        try:
            required_fields = ["type", "value"]
            if not all(field in expression for field in required_fields):
                self.add_error(
                    ErrorType.VALIDATION_ERROR,
                    "Missing required fields in expression",
                    {"expression": expression}
                )
                return False
            return True
        except Exception as e:
            self.add_error(
                ErrorType.RUNTIME_ERROR,
                f"Error validating input: {str(e)}",
                {"expression": expression}
            )
            return False
