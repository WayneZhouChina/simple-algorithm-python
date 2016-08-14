#!/usr/bin/env python
# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        start = 1
        end = n
        while start <= end:
            mid =  (start + end) // 2
            judge = guess(mid)
            if judge == 1:
                start = mid + 1
            elif judge == -1:
                end = mid - 1
            else:
                return mid


