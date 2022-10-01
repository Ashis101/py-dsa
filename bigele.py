p=[4,5,8,10,7,5,41,22,11]

def bigele():
    # for i in p:
    #     for y in p:
    #         if y > i:
    #             break
    
    #     else:
    #         return i
    # return none
    if not p:
        return none
    else:
        res=p[0]
        for i in range(1,len(p)):
            if p[i] > res:
                res=p[i]
    return res


print(bigele())
    

