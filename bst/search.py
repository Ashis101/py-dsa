
import time

class Node:
    def __init__(self,k):
        self.left=None
        self.key=k
        self.right=None



def searh(root,k):

    if root == None:
        return False
    
    if root.key == k:
        return True
    if root.key > k:
        return searh(root.left,k)
    else:
        return searh(root.right,k)
    

root=Node(50)
root.left=Node(30)
root.left.left=Node(30)
root.left.right=Node(40)
root.right=Node(70)
root.right.right=Node(78)
root.right.left=Node(60)
root.right.left.left=Node(55)

print(time.time())
print(searh(root,400))
print(time.time())