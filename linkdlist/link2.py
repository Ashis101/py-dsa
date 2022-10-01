## add a value begiing of the linked list

class Node:
    def __init__(self,k):
        self.key=k
        self.end=None


def inserBegin(head,key):
    value=Node(key)
    value.next=head
    return value
head=None
head=inserBegin(head,10)
head=inserBegin(head,20)
print(head)



