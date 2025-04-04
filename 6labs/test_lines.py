"""Unit test for lines"""

import pytest
from lines import get_lines


def test_get_lines():
    """Count lines of THIS file"""
    assert get_lines(__name__+".py") == 10


def test_get_lines_no_file():
    """Raise exception of not existing file"""
    with pytest.raises(FileNotFoundError):
        get_lines("NOT_EXISTING_FILE")
