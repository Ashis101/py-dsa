a="abaac"
b="aacba"


def ana():
    # if len(a) != len(b):
    #     return False
    # sa=sorted(a)
    # sb=sorted(b)
    # return (sa == sb)
    if len(a) != len(b):
        return False
    count=[0]*256
    for i in range(len(a)):
        count[ord(a[i])] += 1
        count[ord(b[i])] -= 1
    for x in count:
        if x != 0:
            return False
    return True

print(ana())