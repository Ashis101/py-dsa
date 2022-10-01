l=[10,20,30,40]

def left():
    le=len(l)
    f=l[0]
    for i in range(0,le):
        l[i]=l[i-1]
    l[le-1]=f
    return l

print(left())
