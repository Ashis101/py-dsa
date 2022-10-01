# ## Balanced Paranthesis

# def isMatching(a,b):
#     if (a=='(' and b==')')or(a=='{' and b=='}')or(a=='[' and b==']'):
#         return True
#     else:
#         return False

# def isBalance(exp):
#     stack=[]
#     for x in exp:
#         if x in ('(','{','['):
#             stack.append(x)
#         else:
#             if not stack:
#                 return False
#             elif isMatching(stack[-1],x) == False:
#                 return False
#             else:
#                 stack.pop()
#     if stack:
#         return False
#     else:
#         return True
    

def isBalance(exp):
    stack=[]
    for x in exp:
        if x in ('(','{','['):
            stack.append(x)
    return stack

print(isBalance("[{()}]"))