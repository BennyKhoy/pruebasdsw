import string


def validate_password(password: str) -> dict:
    """Validate password exercise 5"""
    errors = []

    if len(password) < 8:
        errors.append("Password must be at least 8 characters")

    digits = sum(1 for c in password if c.isdigit())
    if digits < 2:
        errors.append("The password must contain at least 2 numbers")

    if not any(c.isupper() for c in password):
        errors.append("password must contain at least one capital letter")

    special_chars = set(string.punctuation)
    if not any(c in special_chars for c in password):
        errors.append("password must contain at least one special character")

    return {
        "is_valid": len(errors) == 0,
        "errors": errors
    }
