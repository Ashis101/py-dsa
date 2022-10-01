class Node:
    def __init__(self,key):
        self.data=key
        self.next=None
class Likdlist:
    def __init__(self):
        self.start=None
    
    def insertEnd(self,k):
        newnod=Node(k)
        if self.start == None:
            self.start=newnod
        else:
            temp=self.start
            while temp.next != None:
                temp=temp.next
            temp.next=newnod
    
    def deleteFirst(self):
        if self.start == None:
            print("List is empty")
        
        self.start=self.start.next
        while self.start.next != None:
            print(self.start.data,end="")
            self.start=self.start.next
            

    def viewAll(self):
        if self.start == None:
            print("Nothing to view")
        temp=self.start
        while temp.next != None:
            print(temp.data,end=" ")
            temp=temp.next

    def howMany(self):
        if self.start == None:
            return 0
        else:
            temp=self.start
            count=0
            while temp.next != None:
                count+=1
                temp=temp.next
            print(count)

    def givenPosition(self,nodenumber,value):
        newNode=Node(value)
        if nodenumber == 1:
            self.start=newNode
        else:
            temp=self.start
            count=1
            while temp.next != None:
                count+=1

                if count == nodenumber:
                    newNode.next=temp.next
                    temp.next=newNode
                    break
                temp=temp.next
                if temp.next == None:
                    print("beond the size")
                    break
    def delLastnode(self):
        if self.start == None:
            return None
        if self.start.next == None:
            return None
        else:
            temp=self.start
            while temp.next.next != None:
                temp=temp.next
            temp.next=None

    def sortedList(self,val):
        newnode=Node(val)
        if self.start == None:
            self.start=newnode
        elif val < self.start.data :
            newnode.next=self.data
        else:
            curr=self.start
            while curr.next != None and curr.next.data < val:
                curr=curr.next

            newnode.next=curr.next
            curr.next=newnode
    
    def reverseList(self):
        curr=self.start
        prev=None
        while curr != None:
            next=curr.next
            curr.next=prev
            prev=curr
            curr=next
        return prev
        
mylist=Likdlist()
mylist.insertEnd(10)
mylist.insertEnd(20)
mylist.insertEnd(30)
mylist.insertEnd(40)
mylist.insertEnd(50)
print("\n---Now---")
# mylist.howMany()
mylist.viewAll()
# print("\n---delete first and now---")
# mylist.howMany()

# mylist.deleteFirst()
print("\n changing desire node value ")
mylist.givenPosition(2,5)
print("--before delete--\n")
mylist.viewAll()

mylist.delLastnode()
print("\n--after delete--")
mylist.viewAll()

