"""Unit-test for Regular, um, Expressions"""

from um import count


def test_um():
    """Test um counting"""
    assert count("Um... hello") == 1
    assert count("I, um, do not know") == 1
    assert count("Suppose, um, I, um, can't, um, answer to you") == 3


def test_um_demo():
    """Test um count as cs50p demo"""
    assert count("hello, um, world") == 1
    assert count("um, hello, um, world") == 2
    assert count("um...") == 1
    assert count("yum") == 0
    assert count("yummy") == 0


def test_um_manual_test():
    """Test um count as cs50p manual test"""
    assert count("um") == 1
    assert count("um?") == 1
    assert count("Um, thanks for the album.") == 1
    assert count("Um, thanks, um...") == 2
