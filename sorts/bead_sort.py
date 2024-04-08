"""
Bead sort only works for sequences of non-negative integers.
https://en.wikipedia.org/wiki/Bead_sort
"""

from itertools import pairwise


def bead_sort(sequence: list) -> list:
    """
    >>> bead_sort([6, 11, 12, 4, 1, 5])
    [1, 4, 5, 6, 11, 12]

    >>> bead_sort([9, 8, 7, 6, 5, 4 ,3, 2, 1])
    [1, 2, 3, 4, 5, 6, 7, 8, 9]

    >>> bead_sort([5, 0, 4, 3])
    [0, 3, 4, 5]

    >>> bead_sort([8, 2, 1])
    [1, 2, 8]

    >>> bead_sort([1, .9, 0.0, 0, -1, -.9])
    Traceback (most recent call last):
        ...
    TypeError: Sequence must be list of non-negative integers

    >>> bead_sort("Hello world")
    Traceback (most recent call last):
        ...
    TypeError: Sequence must be list of non-negative integers
    """
    if any(not isinstance(x, int) or x < 0 for x in sequence):
        raise TypeError("Sequence must be list of non-negative integers")
    for _ in range(len(sequence)):
        for i, (rod_upper, rod_lower) in enumerate(pairwise(sequence)):
            if rod_upper > rod_lower:
                sequence[i], sequence[i + 1] = rod_lower, rod_upper
    return sequence


if __name__ == "__main__":
    assert bead_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]
    assert bead_sort([7, 9, 4, 3, 5]) == [3, 4, 5, 7, 9]
