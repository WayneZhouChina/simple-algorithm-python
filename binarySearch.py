#!/usr/bin/env python

def binarySearch(myList, val):
    first = 0
    last  = len(myList) - 1
    found = False
    while first <= last and not found:
        mid = (last+first)  // 2
        if myList[mid] == val:
            found = True
        else:
            if myList[mid] > val:
                last = mid - 1
            else:
                first = mid + 1

    return found

if __name__ == "__main__":
    myList = [1,2,3,4,5,6]
    # True
    print binarySearch(myList, 4)
    # False
    print binarySearch(myList, 7)
