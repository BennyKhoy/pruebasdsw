import unittest
from password_validator import validate_password


class TestPasswordValidator(unittest.TestCase):
    """Test suite to verify password validation rules and error handling."""

    def test_password_too_short_returns_error_message(self):
        """Checks that a short password returns the correct length error message."""
        result = validate_password("abc1")
        self.assertIn("Password must be at least 8 characters", result["errors"])

    def test_password_with_8_chars_passes_length_check(self):
        """Verifies that a password with 8 characters passes the length validation."""
        result = validate_password("abcdefgh")
        self.assertNotIn("Password must be at least 8 characters", result["errors"])

    def test_password_with_less_than_2_numbers_returns_error(self):
        """Ensures that fewer than two numbers triggers the appropriate error message."""
        result = validate_password("abcdefg1")
        self.assertIn("The password must contain at least 2 numbers", result["errors"])

    def test_password_with_2_numbers_passes_rule(self):
        """Checks that a password with exactly two numbers satisfies the rule."""
        result = validate_password("abcdef12")
        self.assertNotIn(
            "The password must contain at least 2 numbers", result["errors"]
        )

    def test_very_short_password_with_no_numbers_returns_both_errors(self):
        """Verifies that a very short password without numbers returns both error messages."""
        result = validate_password("abc")
        self.assertIn("Password must be at least 8 characters", result["errors"])
        self.assertIn("The password must contain at least 2 numbers", result["errors"])

    def test_invalid_password_returns_false_when_multiple_errors(self):
        """Ensures that a password with multiple violations is marked as invalid."""
        result = validate_password("abc")
        self.assertFalse(result["is_valid"])

    def test_errors_count_is_correct_for_two_violations(self):
        """Checks that the error list contains exactly two messages for two violations."""
        result = validate_password("abc")
        self.assertEqual(len(result["errors"]), 2)

    def test_errors_can_be_joined_with_newline_as_in_spec(self):
        """Verifies that error messages can be joined with newline formatting."""
        result = validate_password("somepass")
        combined = "\n".join(result["errors"])
        self.assertIn("The password must contain at least 2 numbers", combined)


if __name__ == "__main__":
    unittest.main()
