#!/usr/bin/env python

# Thanks for http://bookshadow.com/weblog/2016/04/18/leetcode-power-of-four/

def Soultion(object):
    def isPowerOfFour(self, num):
        if num > 0 and num & (num - 1) == 0:
            if num & 0x55555555 > 0:
                return True

        return False
