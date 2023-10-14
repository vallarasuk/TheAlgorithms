# Print all subset combinations of n element in given set of r element.


def combination_util(arr, n, r, index, data, i):
    """
    Current combination is ready to be printed, print it
    arr[]  ---> Input Array
    data[] ---> Temporary array to store current combination
    start & end ---> Staring and Ending indexes in arr[]
    index  ---> Current index in data[]
    r ---> Size of a combination to be printed

    >>> combination_util([1, 2, 3], 3, 2, 0, [0, 0], 0)
    1 2
    1 3
    2 3

    >>> combination_util([-1,-2,-3], 3, 2, 0, [0, 0], 0)
    -1 -2
    -1 -3
    -2 -3

    both of these should return nothing
    >>> combination_util([], 3, 2, 0, [0, 0], 0)

    >>> combination_util([1], 3, 2, 0, [0, 0], 0)


    """
    if index == r:
        for j in range(r):
            print(data[j], end=" ")
        print(" ")
        return
    #  When no more elements are there to put in data[]
    if i >= n:
        return
    # current is included, put next at next location
    data[index] = arr[i]
    combination_util(arr, n, r, index + 1, data, i + 1)
    # current is excluded, replace it with
    # next (Note that i+1 is passed, but
    # index is not changed)
    combination_util(arr, n, r, index, data, i + 1)
    # The main function that prints all combinations
    # of size r in arr[] of size n. This function
    # mainly uses combinationUtil()
    # edit


def print_combination(arr, n, r):
    """
    >>> print_combination([1, 2, 3], 3, 2, 0, [0, 0], 0)
    1 2
    1 3
    2 3

    >>> print_combination([-1,-2,-3], 3, 2, 0, [0, 0], 0)
    -1 -2
    -1 -3
    -2 -3

    both of these should return nothing
    >>> print_combination([], 3, 2, 0, [0, 0], 0)

    >>> print_combination([1], 3, 2, 0, [0, 0], 0)"""
    # A temporary array to store all combination one by one
    # returns nothing if n < r
    if n < r:
        return
    data = [0] * r
    # Print all combination using temporary array 'data[]'
    combination_util(arr, n, r, 0, data, 0)


if __name__ == "__main__":
    # Driver code to check the function above
    # arr = [10,20,30,40,50]
    arr = [10, 20, 30, 40, 50]
    print_combination(arr, len(arr), 3)
    # This code is contributed by Ambuj sahu
