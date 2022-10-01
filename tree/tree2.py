# Size of a binary tree

class Node:
    def __init__(self,k):
        self.right=None
        self.key=k        
        self.left=None


def sizeoftree(root):
    if root == None:
        return 0
    else:
        left=sizeoftree(root.left)
        right=sizeoftree(root.right)
        return left+right+1

root=Node(10)
root.left=Node(20)
root.right=Node(30)
root.right.left=Node(40)
root.right.right=Node(50)
print(sizeoftree(root))