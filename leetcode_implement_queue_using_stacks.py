#!/usr/bin/env python

class Queue(object):
    def __init__(self):
        self.inStack  = []
        self.outStack = []

    def push(self, x):
        self.inStack.append(x)

    def pop(self):
        self.peek()
        self.outStack.pop()

    def peek(self):
        if not self.outStack:
            while self.inStack:
                inStackVal = self.inStack.pop()
                self.outStack.append(inStackVal)
        return self.outStack[-1]

    def empty(self):
        if self.inStack == 0 and self.outStack == 0:
            return True
        else:
            return False
