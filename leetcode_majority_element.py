#!/usr/bin/env python

class Solution(object):
    def majorityElement(self, nums):
        if nums is None:
            return nums

        candidate, count = None, 0
        for num in nums:
            if count == 0:
                candidate = num
                count += 1
            elif num == candidate:
                count += 1
            else:
                count -= 1

        return candidate
