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
        "aabaaa"
        1. Enumerates over the string
        2. Keeping track of the start of a non repeat character sequence
        3. Calculate the cost for removal of duplicates when we encounter a different character
        4. Use a sentinel for the end
        aabaa#

        T.C. O(N)
        S.C. O(1)
    """

    def minCost(self, s: str, cost: List[int]) -> int:
        last_non_repeat_char_idx = 0
        last_non_repeat_char = ""

        min_cost = 0
        s += '#'  # Adding a sentinel character to the end of the string to trigger the calculation of min cost

        for idx, c in enumerate(s):
            if c != last_non_repeat_char:
                if (idx - last_non_repeat_char_idx > 1):
                    # Since there could be multiple conscutive repeating characters, we want to evaluate the cost
                    # only when we encounter a character that is different
                    # and there was at least one other character prior to this one
                    #  ab  vs. aab   , we want to trigger calculation in the second case only
                    repeat_char_costs = cost[last_non_repeat_char_idx: idx]
                    most_expensive_char_cost = max(repeat_char_costs)
                    # We are going to be removing the least expensive characters
                    # calculat the cost of those.
                    repeat_char_costs.remove(most_expensive_char_cost)
                    min_cost += sum(repeat_char_costs)

                last_non_repeat_char = c
                last_non_repeat_char_idx = idx

        return min_cost


    def minCost_2(self, s: str, cost: List[int]) -> int:
        last_non_repeat_char_idx = 0
        last_non_repeat_char = ""

        min_cost = 0
        s += '#'  # Adding a sentinel character to the end of the string to trigger the calculation of min cost
        cost.append(0) # Likewise for cost

        local_sum = 0
        local_max = 0

        for idx, c in enumerate(s):
            if c != last_non_repeat_char:
                if (idx - last_non_repeat_char_idx > 1):
                    # Since there could be multiple conscutive repeating characters, we want to evaluate the cost
                    # only when we encounter a character that is different
                    # and there was at least one other character prior to this one
                    #  ab  vs. aab   , we want to trigger calculation in the second case only
                    # cost_repeat = cost[last_non_repeat_char_idx: idx]
                    # max_cost = max(cost_repeat)
                    # cost_repeat.remove(max_cost)
                    # min_cost += sum(cost_repeat)
                    min_cost += (local_sum - local_max)

                local_sum = 0
                local_max = 0

                last_non_repeat_char = c
                last_non_repeat_char_idx = idx

            local_sum += cost[idx]
            if cost[idx] > local_max:
                local_max = cost[idx]

        return min_cost