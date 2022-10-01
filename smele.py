inpu=int(input("taking input:\n"))
def  smallerele(p):
    small=[]
    for i in p:
        if i < inpu:
            small.append(i)
    return small    

p=[4,5,8,10,7,5,41,22,11]
print(smallerele(p))