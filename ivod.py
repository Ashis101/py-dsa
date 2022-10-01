a=[10,80,30,15,41]

even=[]
odd=[]

def getval():
    for i in a:
        if i%2 == 0:
            even.append(i)
        else:
            odd.append(i)
    return even,odd

even,odd=getval()
print("even:",even,"odd:",odd)