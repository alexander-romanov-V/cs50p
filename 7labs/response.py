"""Response Validation"""

from validator_collection import validators, errors

# pip install validator-collection  [this code]
# or
# pip install validators


def main():
    """Main code"""
    email = input("What's your email address? ")
    try:
        validators.email(email)
        print("Valid")
    except (errors.EmptyValueError, errors.InvalidEmailError):
        print("Invalid")


if __name__ == "__main__":
    main()
