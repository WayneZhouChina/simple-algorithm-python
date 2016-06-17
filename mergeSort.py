#!/usr/bin/env python

def mergeSort(myList):
    if len(myList) > 1:
        mid = len(myList) // 2
        leftHalf  = myList[:mid]
        rightHalf = myList[mid:]

        mergeSort(leftHalf)
        mergeSort(rightHalf)

        i = j = k = 0
        while i < len(leftHalf) and j < len(rightHalf):
            if leftHalf[i] < rightHalf[j]:
                myList[k] = leftHalf[i]
                i += 1
            else:
                myList[k] = rightHalf[j]
                j += 1
            k += 1

        while i < len(leftHalf):
            myList[k] = leftHalf[i]
            i += 1
            k += 1

        while j < len(rightHalf):
            myList[k] = rightHalf[j]
            j += 1
            k += 1
        print("Merging", myList)


if __name__ == "__main__":
    myList = [10, 12, 8, 87, 45, 23, 21, 45]
    mergeSort(myList)
    print myList
