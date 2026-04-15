def validate_password(password: str) -> dict:
    """Validate password exercise 1"""
    errors = []

    if len(password) < 8:
        errors.append("Password must be at least 8 characters")

    return {"is_valid": len(errors) == 0, "errors": errors}
