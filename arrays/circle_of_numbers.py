"""
    Consider integer numbers from 0 to n - 1 written down along the circle in such a way that the distance between any two neighboring numbers is equal (note that 0 and n - 1 are neighboring, too).

    Given n and firstNumber, find the number which is written in the radially opposite position to firstNumber.

    Example

    For n = 10 and firstNumber = 2, the output should be
    circleOfNumbers(n, firstNumber) = 7.



    Input/Output

    [execution time limit] 4 seconds (py3)

    [input] integer n

    A positive even integer.

    Guaranteed constraints:
    4 ≤ n ≤ 20.

    [input] integer firstNumber

    Guaranteed constraints:
    0 ≤ firstNumber ≤ n - 1.

    [output] integer
"""


def circleOfNumbers(n, firstNumber):
    """"
    n = 10

    Radially opposite - a line that passes through the center of the circle.
    Along the radius - This is the diameter line.
    It divides the circle into half.
    How do we calculate the other end of this diameter.

    T.C - O(1)
    S.C. - O(1)

    n  firstNumber     mid.       result

    10   2              5.        7
    4    1              2         3
    """
    mid_distance = (n + 1) // 2
    return (firstNumber + mid_distance) % n

