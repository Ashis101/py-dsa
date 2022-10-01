ar=[10,15,20,40,8,11,55]

def submerge(low,mid,high,ar):
    left=ar[low:mid+1]
    right=ar[low:high+1]
    i=0
    j=0
    k=low
    while i<len(left) and j<len(right):
        if left[i] <= right[j]:
            ar[k]=left[i]
            k=k+1
            i=i+1
        else:
            ar[k]=right[j]
            k=k+1
            j=j+1
    
    while i<len(left):
        a[k]=left[i]
        i=i+1
        k=k+1
    while j<len(right):
        a[k]=right[j]
        j=j+1
        k=k+1



