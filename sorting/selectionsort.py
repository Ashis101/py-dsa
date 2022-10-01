# selection sort
# idea behind this sortind algo is find minimum element is array and replace position to 0
# next find 2nd minimum element and replace position to 1


def selsort(x):
    n=len(x)
    for i in range(n-1):
        min_ind=i
        for j in range(i+1,n):
            if x[min_ind] > x[j]:
                min_ind=j
        x[min_ind],x[i]=x[i],x[min_ind]
    return x
    
l=[10,8,20,5]
print(selsort(l))
