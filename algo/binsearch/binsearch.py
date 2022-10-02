a=[10,20,30,40,50,60,70]
def bin(l):
    low=0
    high=len(a) -1 
    while low <= high:
        mid=(low+high)//2

        if a[mid] == l:
            return mid
        elif l > a[mid] :
            low=mid+1
        else:
            high=mid-1
    return -1

print(bin(50))