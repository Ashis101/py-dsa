## Insert at last

class Node:
    def __init__(self,k):
        self.key=k
        self.prev=None
        self.next=None

def insertLast(head,k):
    newnode=Node(k)
    if head == None:
        return newnode
        
    else:
        curr=head
        while curr.next != None:
            curr=curr.next
        curr.next=newnode
        newnode.prev=curr
        return head
    