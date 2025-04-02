"""Unittest for Back to the Bank"""

from bank import value


def test_value_0():
    """Test good greetings"""
    assert value("Hello, mr") == 0
    assert value("Hello, My darling") == 0


def test_value_20():
    """Test average greetings"""
    assert value("Hi, mrs") == 20
    assert value("Hey, You") == 20
    assert value("Have a good day, mr") == 20


def test_value_100():
    """Test bad greetings"""
    assert value("What's up") == 100
    assert value("Welcome, sir") == 100
    assert value("Good day, sir") == 100


def test_value_empty():
    """Test no greeting"""
    assert value("") == 100


def test_value_non_str():
    """Test non str greetings"""
    assert value(5) == 100
    assert value(0.3) == 100
