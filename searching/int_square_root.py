"""
    Given a nonnegative integer return the largest integer whose square is less than or equal to the given integer
    Given k, return the largest value of x such that x**2 < k

"""


def square_root(k):
    """
        Brute force approach
        Iterate over the range(k), stop when you encounter an integer whose
        square is > k
        -- if k were a 32bit integer, the unit sized increments would result
        in iterations that were about 2 ** 30 (1 GB) - 1 billion iterations
        TC O(k)

        Looking for x such that x**2 <= k
        if x**2 <= k , we can be certain that all values < x can be eliminated
        if x**2 > k, we can be certain that all values > x can be eliminated.

        Interval [0,k], We can use binary search to eliminate large ranges of
        possibilities
        T.C. - O(logk)
        S.C. - O(1)
    """
    left, right = 0, k
    while left <= right:
        mid = (left + right) // 2
        squared = mid * mid
        if squared <= k:
            left = mid + 1
        else:
            right = mid - 1
    return left - 1


assert(square_root(400) == 20)
assert(square_root(5) == 2)
assert(square_root(21) == 4)
assert(square_root(25) == 5)
