#!/usr/bin/env python

def quickSort(myList):
    quickSortHelper(myList, 0, len(myList) - 1)

def quickSortHelper(myList, first, last):
    if first < last:
        pivot = partition(myList, first, last)
        quickSortHelper(myList, first, pivot-1)
        quickSortHelper(myList, pivot+1, last)

def partition(myList, first, last):
    pivot = myList[first]
    left  = first + 1
    right = last

    found = False
    while not found:
        while left <= right and pivot <= myList[left]:
            left += 1

        while left <= right and pivot >+ myList[right]:
            right -= 1

        if left > right:
            found = True
        else:
            tmp = myList[left]
            myList[left] = myList[right]
            myList[right] = tmp

    tmp = myList[right]
    myList[right] = myList[first]
    myList[first] = tmp

    return right

if __name__ == "__main__":
    myList = [10, 20, 24, 89, 24, 56, 12, 9, 79]
    quickSort(myList)
    print myList


