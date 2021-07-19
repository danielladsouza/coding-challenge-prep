"""
    We're going to store numbers in a tree. Each node in this tree will store a single digit (from 0 to 9), and each path from root to leaf encodes a non-negative integer.

    Given a binary tree t, find the sum of all the numbers encoded in it.

    Example

    For
    t = {
        "value": 1,
        "left": {
            "value": 0,
            "left": {
                "value": 3,
                "left": null,
                "right": null
            },
            "right": {
                "value": 1,
                "left": null,
                "right": null
            }
        },
        "right": {
            "value": 4,
            "left": null,
            "right": null
        }
    }
    the output should be
    digitTreeSum(t) = 218.
    There are 3 numbers encoded in this tree:

    Path 1->0->3 encodes 103
    Path 1->0->1 encodes 101
    Path 1->4 encodes 14
    and their sum is 103 + 101 + 14 = 218.
    t = {
        "value": 0,
        "left": {
            "value": 9,
            "left": null,
            "right": null
        },
        "right": {
            "value": 9,
            "left": {
                "value": 1,
                "left": null,
                "right": null
            },
            "right": {
                "value": 3,
                "left": null,
                "right": null
            }
        }
    }
    the output should be
    digitTreeSum(t) = 193.
    Because 09 + 091 + 093 = 193

    Input/Output

    [execution time limit] 4 seconds (py3)

    [input] tree.integer t

    A tree of integers. It's guaranteed that the sum of encoded integers won't exceed 252.

    Guaranteed constraints:
    1 ≤ tree size ≤ 2000,
    1 ≤ tree depth ≤ 9,
    0 ≤ node value ≤ 9.

    [output] integer64

    The sum of the integers encoded in t, as described above.
"""
#
# Binary trees are already defined with this interface:
# class Tree(object):
#   def __init__(self, x):
#     self.value = x
#     self.left = None
#     self.right = None
def digitTreeSum(t):
    """
              1
             /  \
           0     4
         /  \
        3    1
    """
    if not t:
        return 0

    sum = 0

    def helper(n, partial_sum):
        nonlocal sum

        if not n:
            return

        partial_sum = partial_sum * 10 + n.value
        if not n.left and not n.right:  # Update the sum when we are at the leaf node
            sum += partial_sum

        helper(n.left, partial_sum)
        helper(n.right, partial_sum)

    helper(t, 0)
    return sum