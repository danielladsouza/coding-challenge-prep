"""
    L.C. 1578 - Minimum deletion cost to avoid repeating letters

Two step process

1. Identify the start and the end of the repeating character sequence
2. Sum the costs coresponding to that sequence excluding the max cost.

The first step can be done using a two pointer technique
one iterates over the string one character at a time
the other keeps track of the current character that differs from the previous one,
current non repeating character

Now when we get multiple characters side by side, all we have to do is exclude the max value
in that sequence.
0 1 2 3 4 5
a a b a a a

1 1 3 4 1 2

current_nonrepeating_char

a       [1, 1] .. When I encounter a different character, I process the list
min_cost = max(1, 1)
"""

class Solution:
    """
        Algorithm
        This is using a two iterator approach
        1. Iterator that enumerates over the string
        2. Iterator keeping track of the start of a non repeat character sequence
        aabaa#
        |
          |. |
        index 0 2 3 5. are positions of non repeat sequence characters

        T.C. O(N)
        S.C. O(1)
    """

    def minCost(self, s: str, cost: List[int]) -> int:
        # Delete the chosen characters at the same time
        current_non_repeat = ""
        current_non_repeat_idx = 0
        min_cost = 0
        s += '#'  # Adding a sentinel character to the end of the string to trigger the calculation of min cost

        for idx, c in enumerate(s):
            if c != current_non_repeat:
                diff = idx - current_non_repeat_idx
                if (diff > 1): # Since there could be multiple conscutive repeating characters, we want to evaluate the cost
                    # only when we encounter a character that is different
                    # also we add a condition to check that there was at least one other character prior to this one
                    #  ab  vs. aab   , we want to trigger calculation in the second case only
                    cost_repeat = cost[current_non_repeat_idx: idx]
                    max_cost = max(cost_repeat)
                    cost_repeat.remove(max_cost)
                    min_cost += sum(cost_repeat)

                current_non_repeat = c
                current_non_repeat_idx = idx

        return min_cost