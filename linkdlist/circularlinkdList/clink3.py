class Node:
    def __init__(self,k):
        self.key=k
        self.next=None


def insertEnd1(head,k):
    newnode=Node(k)
    if head == None:
        return newnode.next=newnode
    else:
        curr=head
        while curr.next != head:
            curr=curr.next
        curr.next=newnode
        newnode.next=head
        return head
def insertEnd2(head,x):
    newnode=Node(x)
    if head == None:
        newnode.next=newnode
        return newnode
    else:
        newnode.next=head.next
        head.next=newnode.next
        # swapping the values head to newnode,and newnode became head and head became last node
        head.data,newnode.data=newnode.data,head.data
        return head
