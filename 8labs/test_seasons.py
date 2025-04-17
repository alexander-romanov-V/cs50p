"""Lab 8.1 - Seasons of Love. Unit-test"""

from datetime import date
from datetime import timedelta
import pytest
from seasons import get_age_in_minutes
from seasons import text_age_in_minutes


def test_get_age_in_minutes_cs50p_demo():
    """Test age in minutes as cs50p demo"""
    with pytest.raises(TypeError):
        get_age_in_minutes("January 1, 1999")
    assert (
        get_age_in_minutes(date(1999, 1, 1))
        == (date.today() - date(1999, 1, 1)).days * 1440
    )
    assert (
        get_age_in_minutes(date(1999, 12, 31))
        == (date.today() - date(1999, 12, 31)).days * 1440
    )
    assert (
        get_age_in_minutes(date(1970, 1, 1))
        == (date.today() - date(1970, 1, 1)).days * 1440
    )


def test_text_age_in_minutes_cs50p_demo():
    """Test string of age_in_minutes in English words as cs50p demo"""
    assert (
        text_age_in_minutes(525600)
        == "Five hundred twenty-five thousand, six hundred minutes"
    )
    assert text_age_in_minutes(1440) == "One thousand, four hundred forty minutes"
    assert (
        text_age_in_minutes(15778080)
        == "Fifteen million, seven hundred seventy-eight thousand eighty minutes"
    )


def test_get_age_in_minutes_cs50p_manual_test():
    """Test age in minutes as cs50p manual test"""
    assert (
        get_age_in_minutes(date(1988, 5, 16))
        == (date.today() - date(1988, 5, 16)).days * 1440
    )
    assert get_age_in_minutes(date.today() - timedelta(days=365 * 2)) == 365 * 2 * 1440
    with pytest.raises(TypeError):
        get_age_in_minutes("May 16, 1988")


def test_text_age_in_minutes_cs50p_manual_test():
    """Test string of age_in_minutes in English words as cs50p manual test"""
    assert (
        text_age_in_minutes(19418400)
        == "Nineteen million, four hundred eighteen thousand, four hundred minutes"
    )
    assert (
        text_age_in_minutes(1052640)
        == "One million, fifty-two thousand, six hundred forty minutes"
    )
