"""Lecture 9.11 - Etc: *args, **kwargs"""


def f(*args, **kwargs):  # positions args and key words args
    """Test *args and **kwarg behaviour"""
    print("Positional:", args)  # a sequence
    print("Named:", kwargs)  # a dict of params


def new_print(*objects, sep=" ", end="\n"):
    """Example of instance of print func"""

    # can iterate over each variable number of parameters
    for obj in objects:
        print(obj)


f(100, 50, 25)
# Positional: (100, 50, 25)
# Named: {}

f(galleons=100, sickles=50, knuts=25)
# Positional: ()
# Named: {'galleons': 100, 'sickles': 50, 'knuts': 25}

f([1, 2, 3], {4: 5, 6: 7}, xxx=8)
# Positional: ([1, 2, 3], {4: 5, 6: 7})
# Named: {'xxx': 8}
