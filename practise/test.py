from itertools import count


# def rev(arr,length,breakPoint):
#     print(arr)
#     i=0
#     group=-1
#     while i < length:
#         if(i >= breakPoint):
           
#             if(group == 0):
#                 arr[i],arr[i-1]=arr[i-1],arr[i]
#                 # print(arr)
#                 group=-1
#             else:
#                 group=group+1
#         i+=1
#     return arr

# a=[1,2,3,4,5,6,7,8,9]
# N = 9 ;K = 3
# rev(a,N,K)

def ch(A,B):
    if (len(A) != len(B)):
            return 0
        
    A.sort()
    B.sort()
    i=0 
    l=len(A)
    ok=0
    while i < l:
        if(A[i] == B[i] ):
            ok=1
        else:
            return 0
        i+=1
    return ok 
            
a=[1, 2, 3, 4, 5]
b=[5, 4, 3, 2, 1]
print(ch(a,b))

