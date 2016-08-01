#!/usr/bin/env python
# change user again
class Solution(object):
    def containsDuplicate(self, nums):

        nums = sorted(nums)
        for i in range(0, len(nums)-1):
            if nums[i] == nums[i+1]:
                return True
        return False
