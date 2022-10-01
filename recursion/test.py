

def isSorted(a=[],size=0):
    if(size == 0 or size == 1):
        return True
    if(a[0] > a[1]):
        return False
    
    return isSorted(a[0+1],size-1)

        
        
a=[1,2,3,4,5]
isSorted(a,5)