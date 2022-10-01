## Delete last Node

class Node:
    def __init__(self,k):
        self.key=k
        self.prev=None
        self.next=None


def delLast(head):
    if head == None:
        return None
    if head.next == None:
        return None
    curr=head
    while curr.next.next != None:
        curr=curr.next
    curr.next=None
    return head
