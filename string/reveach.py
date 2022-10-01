'''Reverse each word in a given string'''

def sp(s):
    stack=[]
    st=s.split(".")
    
    for i in range(len(st)):
        x=st[i]
        y=''
        for j in range(len(x)):
            y=x[j]+y

        stack.append(y)
    ns='.'.join(stack)
    return ns
S = "i.like.this.program.very.much"

print(sp(S))