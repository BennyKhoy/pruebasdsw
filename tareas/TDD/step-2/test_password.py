import unittest
from password_validator import validate_password


class TestPasswordValidator(unittest.TestCase):

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

    def test_password_with_no_numbers_is_invalid(self):
        """Checks that a password without numbers is invalid."""
        result = validate_password("abcdefgh")
        self.assertFalse(result["is_valid"])

    def test_password_with_one_number_is_invalid(self):
        """Verifies that a password with only one number is invalid."""
        result = validate_password("abcdefg1")
        self.assertFalse(result["is_valid"])

    def test_password_with_less_than_2_numbers_returns_error(self):
        """Ensures that having fewer than two numbers returns the correct error message."""
        result = validate_password("abcdefg1")
        self.assertIn("The password must contain at least 2 numbers", result["errors"])

    def test_password_with_exactly_2_numbers_passes_rule(self):
        """Checks that a password with exactly two numbers passes the validation rule."""
        result = validate_password("abcdef12")
        self.assertNotIn("The password must contain at least 2 numbers", result["errors"])

    def test_password_with_more_than_2_numbers_passes_rule(self):
        """Verifies that a password with more than two numbers passes the validation rule."""
        result = validate_password("abcd1234")
        self.assertNotIn("The password must contain at least 2 numbers", result["errors"])


if __name__ == "__main__":
    unittest.main()
