# is zero sum

# def isZeroSum(l):
#     pr_sum=0
#     d=set()

#     for i in range(len(l)):
#         pr_sum += l[i]
#         if pr_sum == 0 or pr_sum in d:
#             return True
#         d.add(pr_sum)
#         print(d)
#     return False


# print(isZeroSum([-3,4,-3,-1,1]))

# hashing for pair 1
def sumExists(arr,N,sum):
    
    #using set to store the elements.
    mySet=set()
    
    #inserting all elements in the set.
    for i in arr:
        mySet.add(i) 
    
    #iterating over the array.
    for i in arr:
        #taking care of cases like 4-2=2 as two 2's cannot exist in distinct
        #array so we continue iteration over next element.
        if(sum-i==i):
            continue
        else:
            #if (sum-arr[i]) exists in set, we return 1.
            if sum-i in mySet: 
                return 1
                
                
    #if no such pair is present, we return 0.
    return 0 
print(hasing1([61,14,75, 71, 36, 34, 12],68))

