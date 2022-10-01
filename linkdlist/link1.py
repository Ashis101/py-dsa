## list node
class Node:
    def __init__(self,k):
        self.key=k
        self.next=None
## simple linkdlist
#     
# def link(head):
#     curr=head
#     while curr != None:
#         print(curr.key,end = '')
#         curr=curr.next  

## element search in linkdlist
def link(head,x):
    curr=head
    position=1
    while curr != None:
        if curr.key == x:
            return  position
        position=position+1
        curr=curr.next 
    return -1

head=Node(10)
head.next=Node(20)
head.next.next=Node(30)
head.next.next.next=Node(40)
print(link(head,2000))
    


