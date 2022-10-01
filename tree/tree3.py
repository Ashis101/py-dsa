# max number of a binary tree

import math

class Node:
    def __init__(self,k):
        self.right=None
        self.key=k        
        self.left=None


def maxoftree(root):
    if root == None:
        return -math.inf
    else:
        left=maxoftree(root.left)
        right=maxoftree(root.right)
        return max(root.key,left,right)

root=Node(10)
root.left=Node(20)
root.right=Node(30)
root.right.left=Node(40)
root.right.right=Node(50)
print(maxoftree(root))