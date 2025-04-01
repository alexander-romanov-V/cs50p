"""Unittest for hello"""

from hello import hello


def test_default():
    """Check hello default argument"""
    assert hello() == "hello, world"


def test_argument():
    """Check hello arguments"""
    assert hello("David") == "hello, David"
