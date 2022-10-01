p=[4,5,8,10]

def sorted():
    r=1
    while r < len(p):
        if p[r] < p[r-1]:
            return "no"
        r=r+1
    return "yes"

print(sorted())
