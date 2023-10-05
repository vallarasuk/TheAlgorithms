"""
Program to find the shortest palindrome in the given string
"""


def shortestpalindrome(s: str) -> str:
    """
    >>> shortestpalindrome("aacecaaa")
    'aaacecaaa'
    >>> shortestpalindrome("abcd")
    'dcbabcd'
    """

    # Reverse the input string 's' and store it in 'r'
    r = s[::-1]

    # Check if the original string 's' is already a palindrome
    if s == s[::-1]:
        return s

    # Iterate through the characters of 's'.
    for i in range(len(s) + 1):
        # If substring of 's' starting from index 'i' matches with reversed string 'r'
        if s.startswith(r[i:]):
            # construct shortest palindrome by concatenating reversed prefix & string
            return r[:i] + s


if __name__ == "__main__":
    from doctest import testmod

    testmod()
