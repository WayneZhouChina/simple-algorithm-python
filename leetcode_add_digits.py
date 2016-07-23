#!/usr/bin/env python
'''
https://leetcode.com/problems/add-digits/
Given num = 38, the process is like: 3 + 8 = 11, 1 + 1 = 2. Since 2 has only one digit, return it.
'''

def addDigits(num):
    if num == 0:
        return num
    return (num - 1) % 9 + 1

if __name__ == "__main__":
    print(addDigits(38))
