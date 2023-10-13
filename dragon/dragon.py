"""
* Class Dragon

Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>>
    >>>
"""


class Dragon:
    def __init__(self, name):
        self.name = name


if __name__ == "__main__":
    dragon = Dragon('Wawelski')
    result = dragon.name