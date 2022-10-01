
def nextgret(arr):
    stack=[]
    for j in range(len(arr)):
        for i in range(j+1,len(arr)):
            if arr[j] < arr[i]:
                gret=arr[i]
                stack.append(gret)
            else:
                break
    stack.append(-1)        
    return stack
a=[6 ,8 ,0 ,1,3]
print(nextgret(a))