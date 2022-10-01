class Node:
    def __init__(self,k):
        self.left=None
        self.key=k
        self.right=None


# Inorder Tree
def inorder(root):
    if root != None:
        inorder(root.left)
        print(root.key)
        inorder(root.right)

def preorder(root):
    if root != None:
        print(root.key)
        preorder(root.left)
        preorder(root.right)

def postorder(root):
    if root != None:
        preorder(root.left)
        preorder(root.right)
        print(root.key)
        


root=Node(10)
root.left=Node(20)
root.right=Node(30)
root.right.left=Node(40)
root.right.right=Node(50)
inorder(root)
preorder(root)