
import math
from operator import le, lt


class Heap:

    arr=[]
    def __init__(self,value):
        self.arr=value
    
    def parent(self,i):
        return (i-1)//2
    
    def leftChild(self,i):
        return (2*i+1)

    def rightChild(self,i):
        return (2*i+1)


    def insert(self,x):
        arr=self.arr
        arr.append(x)
        insertElementIndex=len(arr)-1
        
        while insertElementIndex > 0 and arr[self.parent(insertElementIndex)] > arr[insertElementIndex]:
            parentElementIndex=self.parent(insertElementIndex)
            
            arr[insertElementIndex],arr[parentElementIndex]=arr[parentElementIndex],arr[insertElementIndex]

            insertElementIndex=parentElementIndex
            

        print(arr)


    def extractMin(self):
        arr=self.arr
        n=len(arr)

        if(n==0):
            return math.inf
        
        min=arr[0]
        arr[0]=arr[n-1]
        arr.pop()
        self.minHeapify(0)
        return min

    def minHeapify(self,index):
        arr=self.arr
        smallest=index
        print(smallest)
        print(index)
        lc=self.leftChild(index)
        rc=self.rightChild(index)
         
        n=len(arr)-1

        if lc < n and arr[lc] < arr[smallest]:
            smallest=lc
        if rc < n and arr[rc] < arr[smallest]:
            smallest=rc
        if smallest != index: 
            arr[smallest],arr[index]=arr[index],arr[smallest]
            print(arr)
            self.minHeapify(smallest)

        
        


    def test(self):
        print("test")
        

