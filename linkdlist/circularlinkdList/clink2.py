
class Node:
    def __init__(self,k):
        self.key=k
        self.next=None

def inserBeg1(head,x):
    temp=Node(x)
    if head == None:
        temp.next=temp
        return temp
    curr=head
    while curr.next != head:
        curr=curr.next  
    curr.next=temp
    temp.next=head
    return temp

def inserBeg2(head,x):
    temp=Node(x)
    if head == None:
        temp.next=temp
        return temp
    else:
        temp.next=head.next 
        head.next=temp
        head.key,temp.key=temp.key,head.key
        return head