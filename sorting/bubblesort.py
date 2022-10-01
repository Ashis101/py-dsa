# bubble sort 
# idea behind this sort mechanism is comparing two occurence 1st occer > next occer then replace theire positions
# doing sorting array's last index to first index
 
def bsort(l):
    last=len(l)
    for i in range(last-1):
        for j in range(last-i-1):
            if l[j] > l[j+1]:
                tmp = l[j];  #Temporary variable to hold the current number
                l[j] = l[j+1]; #Replace current number with adjacent number
                l[j+1] = tmp; #Replace adjacent number with current number

    return l

l=[10,8,20,5]
print(bsort(l))

