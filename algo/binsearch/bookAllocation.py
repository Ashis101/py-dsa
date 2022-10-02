def isPossible(A,N,M,MID):
    page_sum=0
    stunt_count=1

    for i in range(0,N-1):
        if((A[i] + page_sum) <= MID ):
            page_sum=page_sum+A[i]
        else:
            stunt_count+=1
            if(stunt_count > M or A[i] > MID):
                return False
            page_sum=A[i]


    return True

def bookAllocation(A, N, M):
    low=0
    sum=0
    for i in A:
        sum+=i
    
    high=sum
    ans=-1

    while(low<=high):
        mid=(low+high)//2

        if(isPossible(A,N,M,mid)):
            ans=mid
            high=mid-1
        else:
            low=+1
    return ans

a=[12,34,67,90]
print(bookAllocation(a,4,2))
    




