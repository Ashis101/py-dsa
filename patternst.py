a="geeks for geeks"
p="geeks"

def paterrn():
    # res keeps first matching occurence value 0
    res=a.find(p)
    # whenever res get -1 means there is no matching occurence,then loops end
    while res>=0:
        print(res)
        res=a.find(p,res+1)


print(paterrn())