def validate_user(user):
    required_keys = ["firstname", "lastname", "username", "email"]
    if not all(key in user for key in required_keys):
        return None

    # Proceed with other operations if all keys are present
    return user
