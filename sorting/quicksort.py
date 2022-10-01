# divide and conquer algortithem

# worst case time:0(n2)

# despite 0(n2) worst case,it is consider faster,because of the following
# reason
#     .in-place
#     .cache friendly
#     .average case in 0(nlogn)
#     .tail recursive

# partition is key sunction(naive,lomuto,hoare)

# partition in giver array(naive)

# def Naivepartition(arr,p):
#     # p is index of a value
#     n=len(arr)
#     arr[p],arr[n-1]=arr[n-1],arr[p]
#     temp=[]
#     for x in arr:
#         if x <= arr[n-1]:
#             temp.append(x)
#     for x in arr:
#         if x > arr[n-1]:
#             temp.append(x)
#     for i in range(len(arr)):
#         arr[i]=temp[i]    

# arr=[6,3,7,12,8,10]
# print(Naivepartition(arr,4))

# def Lumotopartition(arr,low,high):
#        pivot=arr[high]
#        i=low-1
#        for j in range(low,high):
#            if arr[j] <= pivot:
#                i=i+1
#                arr[i],arr[j]=arr[j],arr[i]
#         arr[i+1],pivot=pivot,arr[i+1]
#         return i+1

# arr=[6,3,7,12,8,10]
# print(partition(arr,4))

def hoarePartition(arr,low,high):
       pivot=arr[i]
       i=low-1
       j=high+1
       while True:
           i=i+1
            while arr[i] < pivot:
                i=i+1
            j=j-1
            while arr[j] > pivot:
                j=j-1
            if i >= j:
                return j
            arr[i],arr[j]=arr[j],arr[i]
             
arr=[6,3,7,12,8,10]
print(partition(arr,4))
