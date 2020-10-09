"""
Problem 13: https://projecteuler.net/problem=13

Problem Statement:
Work out the first ten digits of the sum of the following one-hundred 50-digit
numbers.
"""
import os


def solution():
    """
    Returns the first ten digits of the sum of the array elements
    from the file num.txt

    >>> solution()
    '5537376230'
    """
    array = []

    file_path = os.path.join(os.path.dirname(__file__), "num.txt")
    with open(file_path, "r") as file_hand:
        for line in file_hand:
            array.append(int(line))

    return str(sum(array))[:10]


if __name__ == "__main__":
    print(solution())
