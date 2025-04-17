"""Lab 8.2 - Cookie Jar"""

class Jar:
    """Cookie jar to store cookies"""
    def __init__(self, capacity=12) -> None:
        if capacity <= 0:
            raise ValueError
        self._capacity = capacity
        self._size = 0

    def __str__(self) -> str:
        return "🍪" * self._size

    def deposit(self, n) -> object:
        """add n cookies to the cookie jar"""
        if n < 0 or self._size + n > self._capacity:
            raise ValueError
        self._size += n
        return self

    def withdraw(self, n) -> object:
        """remove n cookies from the cookie jar."""
        if n < 0 or self._size - n < 0:
            raise ValueError
        self._size -= n
        return self

    @property
    def capacity(self) -> int:
        """Returns a capacity of the jar"""
        return self._capacity

    @property
    def size(self) -> int:
        """Returns a capacity of the jar"""
        return self._size
