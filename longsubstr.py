''' logest substring '''


# def lsub(a):
#     l=0
#     r=0
#     count=0
#     s={}

#     while r < len(a)-1:
#         if a[r] != a[r-1]:
#             count+=1
#             s[a[r]]=r
#         elif a[r] in s:
#             l=s[a[r]]+1
#             s[a[r]]=r



#         r+=1
#     return count

# print(lsub())

def lsub(a):
    charset=set()
    l=0
    res=0

    for r in range(len(a)):
        if a[r] in charset:
            charset.remove(a[r])
            l+=1

        charset.add(a[r])
    res=max(res,r-l+1)

x='abcdhgabcmnbabcdef'
print(lsub(x))