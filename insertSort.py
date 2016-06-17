#!/usr/bin/env python

def insertSort(myList):
    for i in range(1, len(myList)):
        cur = myList[i]
        pre = i - 1
        while pre >= 0:
            if cur > myList[pre]:
                myList[pre+1] = myList[pre]
                myList[pre] = cur
                pre -= 1
            else:
                break

if __name__ == "__main__":
    myList = [10, 12, 8, 87, 45, 23, 21, 45]
    insertSort(myList)
    print myList
