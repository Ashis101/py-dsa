l=[10,10,20,20,4]

# --in for loop
# def finod():
#     val=None
#     for i in l:
#         if l.count(i) != 2:
#             val=i
#             break
#     return val
# print(finod())

# -- in xor
def finod():
    val=0
    for i in l:
       val=val^i
    return val
print(finod())
