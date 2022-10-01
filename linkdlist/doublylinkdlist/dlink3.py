## Delete First Node

class Node:
    def __init__(self,k):
        self.key=k
        self.prev=None
        self.next=None

def deleteHead(head):
    if head == None:
        return None
    if head.next == None:
        return None
    else:
        head=head.next
        head.prev=None
        return head
    
    



    
