a=['dog','cat','act','god','fan']

def isAnagram(a,b):
        #code here
        x=len(a)
        y=len(b)
        
        if x != y or x <=2 or y <= 2:
            return "No"
        
        if sorted(a) != sorted(b):
            return "NO"
        else:
            return "Yes"
        

print(isAnagram('b','d'))