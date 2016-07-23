#!/usr/bin/env python

# 0 represent red
# 1 represent white
# 2 represent blue
def holland(myList):
    curr  = 0
    begin = 0
    end   = len(myList) - 1

    while curr <= end:
        if myList[curr] == 0:
            myList[begin], myList[curr] = myList[curr], myList[begin]
            begin += 1
            curr  += 1
        elif myList[curr] == 1:
            curr += 1
        elif myList[curr] == 2:
            myList[curr], myList[end] = myList[end], myList[curr]
            end -= 1


if __name__ == "__main__":
    myList = [0,1,1,0,2,0,2,1,2]
    holland(myList)
    print(myList)
