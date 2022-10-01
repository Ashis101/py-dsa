
class Node:
    def __init__(self,k):
        self.left=None
        self.key=k
        self.right=None
# maximum in binary tree

# def maxInTree(root):

#     if(root == None):
#         return 
#     ls=maxInTree(root.left)
#     rs=maxInTree(root.right)
#     return max(root.key,ls,rs)

def searchIn(root,s):
    if root == None:
        return  False
    if root.key == s:
        return True
    elif searchIn(root.left,s) == True:
        return True
    else:    
        searchIn(root.right,s)

def heightOFTree(root):

    if root == None:
        return 0
    
    ls=heightOFTree(root.left)
    rs=heightOFTree(root.right)

    return max(ls,rs) + 1



node=Node(10)
node.left=Node(20)
node.right=Node(30)
node.left.left=Node(40)
node.left.right=Node(50)

# print(maxInTree(node))
# print(searchIn(node,40))
print(heightOFTree(node))