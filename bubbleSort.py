#!/usr/bin/env python

def bubbleSort(myList):
    for i in range(0, len(myList) - 1):
        for j in range(0, len(myList) - i - 1):
            if myList[j] > myList[j+1]:
                myList[j], myList[j+1] = myList[j+1], myList[j]


if __name__ == "__main__":
    myList = [10, 12, 8, 87, 45, 23, 21, 45]
    bubbleSort(myList)
    print myList
