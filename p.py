



def ps(arr:list,n:int,student:int,mid:int):
    pages_sum=0
    student_no=1
    for i in range(n-1):
        if(pages_sum+arr[i] < mid):
            pages_sum+=arr[i]
        else:
            student+=1
            if(student_no > student or arr[i] > mid ):
                return False
            
            pages_sum=0
            pages_sum+=arr[i]
    return True

def allocatebook(arr:list,n:int,student:int):
    sum_of_array=0
    for i in range(n-1):
        sum_of_array+=arr[i]
    low=0
    high=sum_of_array
    ans=0
    while(low<=high):
        mid=(low+high)//2
        if(ps(arr,n,student,mid)):
            ans=mid
            high=mid-1
        else:
            low=mid+1

    return ans


a=[12, 34, 67, 90]

print(allocatebook(a,4,2))


