# Sum of natural numbers

def sum(n):
    if n == 0:
        return 0
    return n+sum(n-1)

print(sum(5))

# Sum of natural numbers, using math

# def sum(n):
#     # 10*(10+1)//2 = 55
#     sum=n*(n+1)//2
#     print("Sum is",sum)
# print(sum(10))

