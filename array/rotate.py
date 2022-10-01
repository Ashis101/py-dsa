
def makro(leng,rota,*arg):
    list1=[]
    for i in arg:
        i.replace(" ",",")
        list1.append(i)
    rotate(rota,leng,list1)
    print(list1)
def rotate(ro,leng,list1):
    rotate=ro
    while rotate:
        temp=list1[0]
        for i in range(0,leng-1):
            list1[i]=list1[i+1]
        list1[leng-1]=temp
        rotate=rotate-1

def find(key):

    ar=[5,6,7,8,9,10,1,2,3]
    leng=len(ar)
    for i in range(0,leng):
        if key == ar[i]:
            return "key found in index {}".format(i)
        else:
            return "key is not found"

            


# makro(5,2,1 2 3 4 5)

print(find(6))