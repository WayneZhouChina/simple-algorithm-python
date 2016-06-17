#!/usr/bin/env python

ROW = 4
COL = 4

def matrixSearch(myMatrix, searchKey):
    i = 0
    j = COL - 1
    val = myMatrix[i][j]

    while True:
        if val == searchKey:
            return True
        elif searchKey < val and j > 0:
            j -= 1
            val = myMatrix[i][j]
        elif searchKey > val and i < (ROW-1):
            i += 1
            val = myMatrix[i][j]
        else:
            return False


if __name__ == "__main__":
    myMatrix = [[1,2,8,9], [2,4,9,12], [4,7,10,13], [6,8,11,15]]
    # answer is True
    print matrixSearch(myMatrix, 8)
    # answer is False
    print matrixSearch(myMatrix, 88)


