class Node:
    def __init__(self,k):
        self.key=k
        self.next=None
class Mystack:
    def __init__(self):
        self.head=None
        self.n=0

    def push(self,k):
        newnode=Node(k)
        newnode.next=self.head
        self.head=newnode
        self.n+=1
    def size(self):
        return self.n
    def peek(self):
        curr=self.head
        while curr.next != None:
            curr=curr.next
        return curr.key
    def pop(self):
        if self.head == None:
            return math.inf
        
        curr=self.head.next
        self.head=self.head.next
        self.n-=1
        return curr
 

