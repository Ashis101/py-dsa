# using sliding window to make sum of subarray 

def slidingWindow_getMaxElement(arr,window):
    window_sum=0
    
    for i in range(window):
        window_sum+=arr[i]
    res=0
    for i in range(window,len(arr)):
        window_sum=window_sum+arr[i]-arr[i-window]
        res=max(window_sum,res)
    
    return res

a=[1,2,13,4,5,6,7]
print(slidingWindow_getMaxElement(a,2))

# using sliding window to make sum with given subarray 
# def slidingWindow_givenSum(arr,value):
#     w0=0
#     w1=1
#     window_sum=arr[w0]+arr[w1]

#     while w0 < len(arr)-1 and w1<len(arr)-1:
#         if(window_sum < value):
#             w1+=1
#             print("W1::{}".format(w1))
#             window_sum+=arr[w1]
#             print("W1 sum::{}".format(window_sum))
            
#         elif(window_sum > value):
#             w0+=1
#             print("w0::{}".format(w0))
#             window_sum-=arr[w0]
#             print("w0 sum::{}".format(window_sum))
#         else:
#             return "Found.."

#     return "Not Found.."

def slidingWindow_givenSum(arr,sum):
    s,curr=0,0

    for e in range(len(arr)):
        curr+=arr[e]
        while(sum>curr):
            sum-=arr[s]
            s+=1
        if(curr == sum):
            return True
    return False
print(slidingWindow_givenSum(a,19))
