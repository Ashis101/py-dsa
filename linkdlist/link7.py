## Sorted insert for Linkdlist
class Node:
    def __init__(self,k):
        self.key=k
        self.next=None

def sortedInsert(head,x):
    temp=Node(k)
    if head == None:
        return temp
    elif x < head.data:
        temp.next=head
        return temp
    else:
        curr=head
        while curr.next != None and curr.next.data < x:
            curr=curr.next
        temp.next=curr.next
        curr.next=temp
        return head

