class Node:
    def __init__(self,k):
        self.left=None
        self.key=k
        self.right=None

# dfs approch

# def insert(root, Key):
#     if root == None:
#         return Node(Key)
#     elif root.key == Key:
#         return root    
#     elif root.key > Key:
#         root.left=insert(root.left,Key)
#     else:
#         root.right=insert(root.right,Key)
#     return root
    
# bfs approch

def insert(root,key):
    parent=None
    curr=root
    while curr != None:
        parent=curr

        if curr.key > key:
            curr=curr.left
        else:
            curr=curr.right 

    if parent == None:
        return Node(root)
    elif parent.key > key:
        parent.left=Node(key)    
    else:
        parent.right=Node(key)
    return parent





root=Node(50)
root.left=Node(30)
root.left.left=Node(30)
root.left.right=Node(40)
root.right=Node(70)
root.right.right=Node(78)
root.right.left=Node(60)
root.right.left.left=Node(55)
print(insert(root,100))