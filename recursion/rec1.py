
# def fun(n):
#     if n == 0:
#         return
#     print(f'it is {n}')
#     fun(n-1)
#     print(n)

# fun(3)

# def fun(n):
#     if n >= 1:
#         return 0
#     else:
#         return 1+fun(n//2)

# print(fun(16))

# print 5 to 1
def fun(n):
    if n == 0:
        return 0
    
    fun(n-1)
    print(n)

print(fun(5))

# print 1 to 5 

# def fun(n):

