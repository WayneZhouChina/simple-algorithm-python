#!/usr/bin/env python

class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        ver1 = version1.split('.')
        ver2 = version2.split('.')

        ver1Len = len(ver1)
        ver2Len = len(ver2)
        maxLen = max(ver1Len, ver2Len)
        for m in range(0, maxLen):
            val1 = 0
            if m < ver1Len:
                val1 = int(ver1[m])
            val2 = 0
            if m < ver2Len:
                val2 = int(ver2[m])

            if val1 < val2:
                return -1
            if val1 > val2:
                return 1
        return 0
