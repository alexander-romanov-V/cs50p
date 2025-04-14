"""Response Validation"""

from validator_collection import validators, errors

# pip install validator-collection


def main():
    """Main code"""
    email = input("What's your email address? ")
    print("Valid" if validate_email(email) else "Invalid")


def validate_email(email):
    """Validate email address"""
    try:
        validators.email(email,allow_empty=True)
    except (errors.EmptyValueError, errors.InvalidEmailError):
        return False
    return True


if __name__ == "__main__":
    main()
