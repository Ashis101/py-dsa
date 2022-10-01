a="abbaa"

def chekpal():
    f=0
    l=len(a)-1
    while f < l:
        if a[f] != a[l]:
            print("no")
            break
        f=f+1
        l=l-1
    else:
        print("yes")
    # another solution: reverse the string and do match with current string  
chekpal()