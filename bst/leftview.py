
class Node:
    def __init__(self,k):
        self.left=None
        self.key=k
        self.right=None




def view(root,currentHeight,counter):
    if root is None:
        return

    if (currentHeight[0] < counter):
        print(root.key)
        currentHeight[0]=counter

    view(root.left,currentHeight,counter+1)
    view(root.right,currentHeight,counter+1)

def leftView(root):
    height=[0]
    view(root,height,1)



root=Node(50)
root.left=Node(30)
root.left.left=Node(30)
root.left.right=Node(40)
root.right=Node(70)
root.right.right=Node(78)
root.right.left=Node(60)
root.right.left.left=Node(55)
print(leftView(root))