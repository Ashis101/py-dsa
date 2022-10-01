a=[10,52,41,74,52,51]

def revers():
    s=0
    l=len(a)-1
    while s<l:
        a[s],a[l]=a[l],a[s]
        s=s+1
        l=l-1
    return a
print(revers())