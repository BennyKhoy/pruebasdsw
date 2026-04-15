import unittest
from password_validator import validate_password


class TestPasswordValidator(unittest.TestCase):
    """Test suite to validate password rules including length, numbers, and uppercase requirements."""

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

    def test_multiple_violations_return_all_errors(self):
        """Verifies that multiple validation errors are all returned."""
        result = validate_password("abc")
        self.assertIn("Password must be at least 8 characters", result["errors"])
        self.assertIn("The password must contain at least 2 numbers", result["errors"])

    def test_password_without_uppercase_is_invalid(self):
        """Checks that a password without uppercase letters is invalid."""
        result = validate_password("abcdef12")
        self.assertFalse(result["is_valid"])

    def test_password_without_uppercase_returns_correct_error(self):
        """Ensures that missing uppercase letters returns the correct error message."""
        result = validate_password("abcdef12")
        self.assertIn(
            "password must contain at least one capital letter", result["errors"]
        )

    def test_password_with_only_uppercase_passes_rule(self):
        """Verifies that a password with at least one uppercase letter passes the rule."""
        result = validate_password("Abcdef12")
        self.assertNotIn(
            "password must contain at least one capital letter", result["errors"]
        )

    def test_password_with_multiple_uppercase_passes_rule(self):
        """Checks that multiple uppercase letters satisfy the uppercase requirement."""
        result = validate_password("ABcdef12")
        self.assertNotIn(
            "password must contain at least one capital letter", result["errors"]
        )


if __name__ == "__main__":
    unittest.main()
