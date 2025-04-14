"""Unit-test for Response Validation 2"""

from response2 import validate_email


def test_validate_email_ok():
    """Valid emails"""
    assert validate_email("malan@harvard.edu") is True
    assert validate_email("") is True


def test_validate_email_nok():
    """Invalid emails"""
    assert validate_email("malan@@@harvard.edu") is False
    assert validate_email("my@email..com") is False
