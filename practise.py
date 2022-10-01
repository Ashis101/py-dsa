

def bisearch(arr,n):
    low=0
    high=len(arr)-1
    count=0
    while low <= high:
        mid=(low+high) / 2

        if(arr[mid] <= n):
            count+=(mid-low+1)
            low=mid+1
        else:
            high=mid-1
    return count

def issame(a,b):
    arr=[]
    count=0
    b.sort()
    n=0
    for i in range(1,len(a)):
        count=bisearch(b,i)
        a[n]=count
        n=i
        
    return a
    
x=[1,2,3,4,7,9]
y=[0,1,2,1,1,4]
print(issame(x,y))

