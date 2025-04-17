"""Lab 8.2 - Cookie Jar. Unit-test"""

import pytest
from jar import Jar


def test_jar_init():
    """Test init of Jar class"""

    # default capacity = 12
    assert Jar().capacity == 12
    # manual set capacity = 4
    assert Jar(capacity=4).capacity == 4
    # try to set negative capacity
    with pytest.raises(ValueError):
        Jar(-1)
    # try to set zero capacity
    with pytest.raises(ValueError):
        Jar(0)


def test_jar_str():
    """Test text representation of Jar class"""

    # empty jar
    assert str(Jar()) == ""
    # jar with 3 cookies
    assert str(Jar().deposit(3)) == "🍪🍪🍪"


def test_jar_deposit():
    """Test deposit cookies"""
    jar = Jar(capacity=5)

    # try add negative cookies into empty jar
    with pytest.raises(ValueError):
        jar.deposit(-1)

    # add 5 cookies
    jar.deposit(5)
    assert jar.size == 5

    # add zero cookies
    jar.deposit(0)
    assert jar.size == 5

    # try to add 6th cookies (over capacity)
    with pytest.raises(ValueError):
        jar.deposit(1)

    # try to add negative cookies (with full capacity)
    with pytest.raises(ValueError):
        jar.deposit(-1)


def test_jar_withdraw():
    """Test withdraw cookies"""
    jar = Jar(capacity=5)

    # try withdraw 1 cookie from empty jar
    with pytest.raises(ValueError):
        jar.withdraw(1)

    # try withdraw negative cookies from empty jar
    with pytest.raises(ValueError):
        jar.withdraw(-1)

    # add 5 cookies
    jar.deposit(5)
    assert jar.size == 5

    # try withdraw negative cookies from non-empty jar
    with pytest.raises(ValueError):
        jar.withdraw(-1)

    # withdraw zero cookies
    jar.withdraw(0)
    assert jar.size == 5

    # withdraw all cookies
    jar.withdraw(5)
    assert jar.size == 0

    # try withdraw some cookies from empty jar
    with pytest.raises(ValueError):
        jar.withdraw(10)
