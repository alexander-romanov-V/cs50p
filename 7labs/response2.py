"""Response Validation 2"""

import validators

# pip install validators


def main():
    """Main code"""
    email = input("What's your email address? ")
    print("Valid" if validate_email(email) else "Invalid")


def validate_email(email):
    """Validate email address"""
    return email == "" or validators.email(email) is True


if __name__ == "__main__":
    main()
