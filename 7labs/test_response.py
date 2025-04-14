"""Unit-test for Response Validation"""

from response import validate_email


def test_validate_email_ok():
    """Valid emails"""
    assert validate_email("malan@harvard.edu") is True
    assert validate_email("") is True


def test_validate_email_nok():
    """Invalid emails"""
    assert validate_email("malan@@@harvard.edu") is False
    assert validate_email("my@email..com") is False
