p=[4,5,8,10,7,5,41,22,11]

def getseclar():
    if len(p) <= 1:
        return None
    larg=p[0]
    seclarg=None
    for i in p[1:]:
        if i > larg:
            seclarg=larg
            larg=i
        elif i != larg:
            if seclarg == None or i > seclarg:
                seclarg=i
    return seclarg  
            

print(getseclar())