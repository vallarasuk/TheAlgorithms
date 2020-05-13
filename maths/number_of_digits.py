def num_digits(n):
    """
        Find the number of digits in a number.
        >>> num_digits(12345)
        5
        >>> num_digits(123)
        3
    """
    digits = 0
    while(n > 0):
        n = n // 10
        digits = digits + 1
    return digits


if __name__ == "__main__":
    num = 12345
    print(num_digits(num))   # ===> 5
