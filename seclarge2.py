p=[4,5,8,10,7,5,41,22,11]

def getlarge():
    l=p[0]
    for i in range(1,len(p)):
        if p[i] > l:
            l=max(l,p[i])
    return l    

# print(getlarge())

def seclarg():
    if len(p) <= 1:
        return None
    large=getlarge()
    seclarg=None
    for i in p:
        if i != large:
            if seclarg == None:
                seclarg = i
            else:
                seclarg=max(seclarg,i)
    return seclarg
print(seclarg())