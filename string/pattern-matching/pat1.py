txt="THIS IS A TEST TEXT"
pat="XT"


def search(txt,pat):
    lpet=len(pat)
    ltxt=len(txt)   

    for i in range(ltxt - lpet +1 ):
        j=0

        while j < lpet:
            if(txt[i+j] != pat[j]):
                break

            j+=1
        
        if(j == lpet):
            return "Pattern Found At: "+str(i)

print(search(txt,pat))