class Node:
    def __init__(self,k):
        self.key=k
        self.next=None
def delLastnode(head):
    if head == None:
        return None
    if head.next == None:
        return None
    else:
        curr=head
        while head.next.next != None:
            curr=head.next
        curr.next=None
        return head
head=Node(10)
head.next=Node(20)
head.next=Node(30)
head.next=Node(40)
print(head)
