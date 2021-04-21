"""
    L.C. 121. Best Time to Buy and Sell Stock

    You are given an array prices where prices[i] is the price of a given stock on the ith day.

    You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

    Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
"""


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # maximum profit can be computed per day, by calculating the difference
        # between the price on that day and the min price encountered so far
        # T.C - O(N)
        # S.C. - O(1)

        min_price_so_far, max_profit = float('inf'), 0

        for price in prices:
            min_price_so_far = min(min_price_so_far, price)
            max_profit = max(max_profit, price - min_price_so_far)
        return max_profit
