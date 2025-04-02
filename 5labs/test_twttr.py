"""Unittest for twttr"""

import pytest
from twttr import shorten


def test_shorten():
    """Test shorten() func"""
    assert shorten("Twitter") == "Twttr"
    assert shorten("What is the question") == "Wht s th qstn"
    assert shorten("Accomodation") == "ccmdtn"


def test_shorten_empty():
    """Test shorten() func with empty str"""
    assert shorten("") == ""


def test_shorten_punct():
    """Test shorten() func with punctuation"""
    assert shorten(".") == "."
    assert shorten(",") == ","
    assert shorten("?") == "?"
    assert shorten("!") == "!"


def test_shorten_arg_type():
    """Test shorten() func with not str argument"""
    with pytest.raises(TypeError):
        assert shorten(5)
    with pytest.raises(TypeError):
        assert shorten(0.3)
