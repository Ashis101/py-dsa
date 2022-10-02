# count occurences in sorted array
l=[10,20,20,20,30,40,50,50,60]

def soArr(x):
    # count=0
    # for i in range(0,len(l)-1):
    #     if x == l[i]:
    #         count = count + 1
    # return count

    # firstoccer and lastoccer() functions are made in binsearch1&2
    # here simple idea is geting first occurence and last occurenece index,and then do (last - first + 1)  

    first=firstoccer(l,x)
    if first == -1:
        return 0
    return lastoccer(l,x) - first +1

print(soArr(50))
