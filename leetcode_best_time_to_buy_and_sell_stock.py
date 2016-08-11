#!/usr/bin/env python

class Solution(object):
    def maxProfit(prices):
        if len(prices) <= 1:
            return 0

        minV = prices[0]
        profit = prices[1] - prices[0]

        for i in range(2, len(prices) ):
            minV = min(prices[i-1], minV)
            profit = max(prices[i] - minV, profit)

        if profit < 0:
            return 0
        return profit

