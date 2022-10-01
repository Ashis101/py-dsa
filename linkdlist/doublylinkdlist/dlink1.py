## Insert at begining

class Node:
    def __init__(self,k):
        self.key=k
        self.prev=None
        self.next=None

def insertBegin(head,k):
    newnode=Node(k)
    curr=head
    while curr.next != None:
        print(curr.key,end="")
        curr=curr.next 
def insertAtBegin(head,k):
    temp=Node(k)
    if head != None:
        head.prev=temp
    temp.next=head
    return temp

head=None
head=insertBegin(head,10)
head=insertBegin(head,20)
head=insertBegin(head,30)
print(head)

