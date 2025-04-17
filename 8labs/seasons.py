"""Lab 8.1 - Seasons of Love"""

# pip install inflect

import sys
from datetime import date
import inflect


def main():
    """Main code"""
    birthday = prompt_birthday()
    age_in_minutes = get_age_in_minutes(birthday)
    print(text_age_in_minutes(age_in_minutes))


def prompt_birthday():
    """Promt user hes date of birth in format YYYY-MM-DD"""
    text = input("Date of Birth: ").strip()
    try:
        return date.fromisoformat(text)
    except (TypeError, ValueError):
        sys.exit("Invalid date")


def get_age_in_minutes(birthday):
    """Returns age in minutes from today"""
    age = date.today() - birthday
    return age.days * 1440


def text_age_in_minutes(age_in_minutes):
    """Returns a string of age_in_minutes in English words"""
    p = inflect.engine()
    return f"{p.number_to_words(age_in_minutes, andword="",).capitalize()} minutes"  # type: ignore


if __name__ == "__main__":
    main()
