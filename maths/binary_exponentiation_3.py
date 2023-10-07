"""
* Binary Exponentiation for Powers
* This is a method to find a^b in a time complexity of O(log b)
* This is one of the most commonly used methods of finding powers.
* Also useful in cases where solution to (a^b)%c is required,
* where a,b,c can be numbers over the computers calculation limits.
* Done using iteration, can also be done using recursion

* @author chinmoy159
* @version 1.0 dated 10/08/2017
"""


def b_expo(a: int, b: int) -> int:
    """

    >>> b_expo(1, 1)
    1

    >>> b_expo(2, 1)
    2

    >>> b_expo(3, 1)
    3

    >>> b_expo(4, 1)
    4

    >>> b_expo(1, 2)
    1

    >>> b_expo(2, 2)
    4

    >>> b_expo(3, 2)
    9

    >>> b_expo(4, 2)
    16

    >>> b_expo(1, 3)
    1

    >>> b_expo(2, 3)
    8

    >>> b_expo(3, 3)
    27

    >>> b_expo(4, 3)
    64

    """
    res = 1
    while b > 0:
        if b & 1:
            res *= a

        a *= a
        b >>= 1

    return res


def b_expo_mod(a: int, b: int, c: int) -> int:
    """

    >>> b_expo_mod(1, 1, 7)
    1

    >>> b_expo_mod(2, 1, 7)
    2

    >>> b_expo_mod(3, 1, 7)
    3

    >>> b_expo_mod(4, 1, 7)
    4

    >>> b_expo_mod(1, 2, 7)
    1

    >>> b_expo_mod(2, 2, 7)
    4

    >>> b_expo_mod(3, 2, 7)
    2

    >>> b_expo_mod(4, 2, 7)
    2

    >>> b_expo_mod(1, 3, 7)
    1

    >>> b_expo_mod(2, 3, 7)
    1

    >>> b_expo_mod(3, 3, 7)
    6

    >>> b_expo_mod(4, 3, 7)
    1

    >>> b_expo_mod(1, 1, 5)
    1

    >>> b_expo_mod(2, 1, 5)
    2

    >>> b_expo_mod(3, 1, 5)
    3

    >>> b_expo_mod(4, 1, 5)
    4

    >>> b_expo_mod(1, 2, 5)
    1

    >>> b_expo_mod(2, 2, 5)
    4

    >>> b_expo_mod(3, 2, 5)
    4

    >>> b_expo_mod(4, 2, 5)
    1

    >>> b_expo_mod(1, 3, 5)
    1

    >>> b_expo_mod(2, 3, 5)
    3

    >>> b_expo_mod(3, 3, 5)
    2

    >>> b_expo_mod(4, 3, 5)
    4

    """
    res = 1
    while b > 0:
        if b & 1:
            res = ((res % c) * (a % c)) % c

        a *= a
        b >>= 1

    return res


"""
* Wondering how this method works !
* It's pretty simple.
* Let's say you need to calculate a ^ b
* RULE 1 : a ^ b = (a*a) ^ (b/2) ---- example : 4 ^ 4 = (4*4) ^ (4/2) = 16 ^ 2
* RULE 2 : IF b is ODD, then ---- a ^ b = a * (a ^ (b - 1)) :: where (b - 1) is even.
* Once b is even, repeat the process to get a ^ b
* Repeat the process till b = 1 OR b = 0, because a^1 = a AND a^0 = 1
*
* As far as the modulo is concerned,
* the fact : (a*b) % c = ((a%c) * (b%c)) % c
* Now apply RULE 1 OR 2 whichever is required.
"""


if __name__ == "__main__":
    import doctest

    doctest.testmod()
