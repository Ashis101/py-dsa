''' Problem 1: Max,Min sub-array of k '''

# def sliding(arr,k):
#     l=len(arr)
#     window_sum=0
#     max_sum=None
#     ''' sum of first subarray and keeping value in window_sum variable '''
#     for i in range(k):
#         window_sum+=arr[i]

#     max_sum=window_sum
#     ''' sliding window '''
#     for i in range(l-k):
#         window_sum=window_sum-arr[i]+arr[k+i]
#         ''' Comparison between current subarry(window_sum) vs previous sub-array(max_sum) '''
#         max_sum=max(window_sum,max_sum)
    
#     return max_sum

def sliding(arr,k):
    i=0
    j=0
    maxsum=0
    windowsum=0
    n=len(a)
    while j < n:
        windowsum+=arr[j]
        
        if(j-i+1 == k):
            maxsum=max(windowsum,maxsum)
            i=i+1
        j=j+1
    return maxsum
a=[1,2,3,4,5,6,7]

print(sliding(a,3))

