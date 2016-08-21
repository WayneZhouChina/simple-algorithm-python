#!/usr/bin/env python

def isPowerOfTwo(n):
    """
        :type n: int
        :rtype: bool
        """
    if n > 0 and (n & (n - 1)) == 0:
        return True
    else:
        return False

if __name__ == "__main__":
    print(isPowerOfTwo(3))
