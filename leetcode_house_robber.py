#!/usr/bin/env python

def Solution(object):
    def rob(self, nums):
        if len(nums) <= 1:
            return 0 if len(nums) == 0 else nums[0]

        #last max num
        lastMax = nums[0]
        #cur max
        curMax = max(nums[0],  nums[1])
        for i in range(2, len(nums)):
            tmp = curMax
            curMax = max(lastMax + nums[i], curMax)
            lastMax = tmp

        return curMax




