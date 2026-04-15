import unittest
from password_validator import validate_password


class TestPasswordValidator(unittest.TestCase):
    """Test suite for validating password rules and error handling."""

    def test_password_too_short_is_invalid(self):
        """Checks that a password shorter than 8 characters is invalid."""
        result = validate_password("abc1")
        self.assertFalse(result["is_valid"])

    def test_password_too_short_returns_error_message(self):
        """Verifies that a short password returns the correct error message."""
        result = validate_password("abc1")
        self.assertIn("Password must be at least 8 characters", result["errors"])

    def test_password_with_8_chars_passes_length_check(self):
        """Ensures that a password with 8 characters passes the length validation."""
        result = validate_password("abcdefgh")
        self.assertNotIn("Password must be at least 8 characters", result["errors"])


if __name__ == "__main__":
    unittest.main()
