def vowel(ch):
    ch=ch.upper()
    return (ch=='A' or ch=='E' or ch=='I' or ch=='O' or ch=='U')
def vowlcount(N):
    #Your code here
    count=0
    for i in range(len(N)):
        if vowel(N[i]):
            count+=1
    return count