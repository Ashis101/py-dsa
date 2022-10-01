''' Inorder Sucesser and Predesseor '''


class Node:

    def __init__(self,key):
        self.key=key
        self.left=None
        self.right=None



def suc(root):
    s=root.right
    while(s != None):
        s=s.left
    return s

def pre(root):
    p=root.left
    while(p != None):
        p=root.right
    return p

def findSuccandPred(root,fkey,pre,succ):
    if(root == None):
        return
    if(root.key == fkey):
        if(root.right):
            s=succ(root)
        if(root.left):
            p=pre(root)
        return("SUCCCER AND PREDECESSOR OF KEY:{}:: {}:{}".format(fkey,s,p))
            
    if(root.key > fkey):
        s=root
        findSuccandPred(root.right,fkey,root,s)
    elif(root.key < fkey):
        p=root
        findSuccandPred(root.left,fkey,p,root)



 