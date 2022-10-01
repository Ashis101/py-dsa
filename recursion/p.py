

from itertools import count


def merge(details,array,n):
    length=n-1

    if length < 1:
        return array
    array.append(details[length])
    print('n:',n,array)
    merge(details,array,n-1)

def mergeDetails(details):
    new_array=[]
    length=len(details)

    merge(details,new_array,length)
    
details = [
["John","johnsmith@mail.com","john_newyork@mail.com"],
["John","johnsmith@mail.com","john00@mail.com"],
["Mary","mary@mail.com"],
["John","johnnybravo@mail.com"]

]

print(mergeDetails(details))