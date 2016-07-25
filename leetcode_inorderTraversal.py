#!/usr/bin/env python

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def inorder(root):
    p = root
    ans = []
    stack = []

    while p or stack:
        while p:
            print("stack appand value: {0}".format(p.val))
            stack.append(p)
            p = p.left
        p = stack.pop()
        print("stack pop value: {0}".format(p.val))
        ans.append(p.val)
        print("ans: ", ans)
        p = p.right
    return ans

if __name__ == "__main__":
    nodeA = TreeNode('a')
    nodeB = TreeNode('b')
    nodeC = TreeNode('c')
    nodeD = TreeNode('d')
    nodeE = TreeNode('e')
    nodeF = TreeNode('f')
    nodeG = TreeNode('g')

    nodeA.left  = nodeB
    nodeA.right = nodeC
    nodeB.left  = nodeD
    nodeB.right = nodeE
    nodeC.left  = nodeF
    nodeC.right = nodeG

    nodeA1 = TreeNode('a')
    nodeB1 = TreeNode('b')
    nodeC1 = TreeNode('c')
    nodeD1 = TreeNode('d')
    nodeE1 = TreeNode('e')
    nodeF1 = TreeNode('f')
    nodeG1 = TreeNode('g')

    nodeA1.left  = nodeB1
    nodeA1.right = nodeC1
    nodeB1.left  = nodeD1
    nodeB1.right = nodeE1
    nodeC1.left  = nodeF1
    nodeC1.right = nodeG1

    print(inorder(nodeA))
