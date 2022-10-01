## Reverse doubly linkdlist

class Node:
    def __init__(self,k):
        self.key=k
        self.prev=None
        self.next=None

def reverse(head):
    if head == None:
        return None
    if head.next == None:
        return head
    else:
        curr=head
        prev=None
        while curr.next != None:
            # at last prev is going hold head 
            prev=curr
            curr.next,curr.prev=curr.prev,curr.next
            curr=curr.next

        return prev

