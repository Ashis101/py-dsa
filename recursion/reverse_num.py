## print reverse of number

# def rev(num):
    # reversed_num=0
    # if num == 0:
    #     return reversed_num
    # reversed_num=reversed_num*10+num%10
    # rev(num=num//10)





def rev(num):
    rev=0
    nums=num
    while(nums > 0):
        rev = rev * 10 + nums%10
        nums = nums // 10
    return rev
print(rev(12345))
