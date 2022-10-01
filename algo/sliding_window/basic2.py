''' Problem 2: Count negative elements present in every K-length subarray  '''

def negative(arr,k):
    i = 0
    j = 0
     
    # Store the count of negative numbers
    count = 0
    n = len(arr)
     
    while(j < n):
         
        # Increase the count
        # if element is less then 0
         
        if (arr[j] < 0):
            count = count + 1
             
        # If size of the window equal to k  
        if (j - i + 1 == k):
            print(count)
             
            # If the first element of
            # the window is less than 0,
            # decrement count by 1
             
            if(arr[i] < 0):
                count = count - 1
             
            i = i+1
        j = j+1
a=[-1, 2, -2, 3, 5, -7, -5]
negative(a,3)