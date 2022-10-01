
class Node:
    def __init__(self,k):
        self.left=None
        self.key=k
        self.right=None


# def isBst(root):
#     if root == None:
#         return 

#     left=isBst(root.left)
#     right=isBst(root.right)
    
#     if root.key < right and root.key > left:
#         return True

#     else:
#         return False

def minValue(root):
    curr=root
    if curr.left == None:
        return curr.key
    if curr != None:
        curr=minValue(curr.left)
    
    return curr

root=Node(50)
root.left=Node(30)
root.left.left=Node(30)
root.left.right=Node(40)
root.right=Node(70)
root.right.right=Node(78)
root.right.left=Node(60)
root.right.left.left=Node(55)
print(minValue(root))