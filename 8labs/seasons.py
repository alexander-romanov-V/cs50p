"""Lab 8.1 - Seasons of Love"""

# pip install inflect

import sys
from datetime import date
import inflect


def main():
    """Main code"""
    birthday = prompt_birthday()
    age_in_minute = how_old_in_minutes(birthday)
    p = inflect.engine()
    print(p.number_to_words(age_in_minute), "minutes")  # type: ignore


def prompt_birthday():
    """Promt user hes date of birth in format YYYY-MM-DD"""
    text = input("Date of Birth: ").strip()
    try:
        return date.fromisoformat(text)
    except ValueError:
        sys.exit("Invalid date")


def how_old_in_minutes(birthday):
    """Returns age in minutes from today"""
    age = date.today() - birthday
    return age.days * 24 * 60


if __name__ == "__main__":
    main()
