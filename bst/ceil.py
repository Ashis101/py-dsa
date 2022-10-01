class Node:
    def __init__(self,key):
        self.left=None
        self.key=key
        self.right=None

def ceil(root,key):
    presentValue=None
    while root != None:
        if root.key == key:
            return root
        elif key > root.key:
            presentValue=root.right
        else:
            presentValue=root.left
    return presentValue



root=Node(50)
root.left=Node(30)
root.left.left=Node(30)
root.left.right=Node(40)
root.right=Node(70)
root.right.right=Node(78)
root.right.left=Node(60)
root.right.left.left=Node(55)
print(ceil(root,50))