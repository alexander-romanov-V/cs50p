"""Unittest for hello"""

from hello import hello


def test_default():
    """Check hello default argument"""
    assert hello() == "hello, world"


def test_argument():
    """Check hello arguments"""
    # ALWAYS KEEP test SIMPLER, and avoid some comprehencive approach
    for name in ["Hermione", "Harry", "Ron"]:
        assert hello(name) == f"hello, {name}"
