# merge two sorted array

def merarray(a,b):
    re=[]
    m=len(a)
    n=len(b)
    i=0
    j=0
    while i<m and j<n:
        if a[i] < b[j]:
            re.append(a[i])
            i=i+1
        else:
            re.append(b[i])
            j=j+1
    while i<m:
        re.append(a[i])
        i=i+1
    while j<n:
        re.append(b[j])
        j=j+1
    return re


