# def sqr(num):
#     return num%2 == 1

# numli=[1,2,3,4,5,6,7,45]

# for i in filter(sqr,numli):
#     print(i)

# def va(A):
#     n = len(A)
#     total = int((n + 1)*(n + 2)/2)
#     sum_of_A = sum(A)
#     return total - sum_of_A
list1=[1,2,5,6,8]
list2=[]
# AP=1
# for i in range(20):
#     if AP in list1:
#         AP=AP+1
#     else:
#         list2.append(AP)
#         AP=AP+1

# print(list2)

for i in range(0,len(list1)):
    for y in list1:
        if list1[i] != y:
            print(y)

# A = [1, 2, 4, 5, 6]
# miss = va(A)
# print(miss)