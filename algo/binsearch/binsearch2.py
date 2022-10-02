# Find first occurence of a number 

l=[5,10]

def bins(x):
    low=0
    high=len(l)-1
    while low <= high:
        mid=(low+high)//2
        if x == l[mid]:
            return mid
        elif x > l[mid]:
            low=mid+1
        else:
            if mid == len(l)-1 or l[mid+1] != l[mid]:
                return mid
            else:
                low=mid+1 
    return -1
print(bins(10))
