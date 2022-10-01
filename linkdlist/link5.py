## Delete first node

class Node:
    def __init__(self,key):
        self.data=key
        self.next=None

class deleteFirstnode():
    if head == None:
        return None
    else:
        return head.next

head=Node(10)
head.next=Node(20)
head.next=Node(30)
head.next=Node(40)
print(head)