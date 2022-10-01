## inserting node at the given position of a linkdlist
class Node:
    def __init__(self,key):
        self.data=key
        self.next=None

def insertPas(head,data,par):
    newNode=Node(data)
    if par == 1:
        temp.next=head
        return temp 
    current=head
    for i in range(par-2):
        current=current.next
        if current == None:
            return head
    newNode.next=current.next
    current.next=newNode
    return head
