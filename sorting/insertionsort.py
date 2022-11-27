# insertion sort
# in-plcae and stable
# used in practise for small arrays
# best suited for sort array but worst case in reverse sorted array

def insertion(l):
    for i in range(1,len(l)):
        x=l[i]
        j=i-1
        while j>=0 and i[j] > x:
            l[j+1]=l[j]
            j=j-1
        l[j+1]=x
    
    