# one time left rotate a list

def isSorted(arr,n):
    
    inc=1
    d=1
    
    for i,e in enumerate(arr[:n-1]):
        if arr[i+1]>=arr[i]:
            continue
        else:
            inc=0
            break
    for i,e in enumerate(arr[:n-1]):
        if arr[i+1]<=arr[i]:
            continue
        else:
            d=0
            break
    
    if inc or d:
        return 1
    else:
        return 0
arr=[98,76,19,3,5]
# arr=[1,5,4,8,5,]
print(leftro(arr)) 


int isSorted(int arr[],int n)
{
  
    bool flagI=true;
    bool flagD=true;
    
    for(int i=0;i<n-1;i++)
    {
        if(arr[i+1]>=arr[i])
        {
            continue;
        }
        else
        {
            flagI=false;
            break;
        }
    }
    for(int i=0;i<n-1;i++)
    {
        if(arr[i+1]<=arr[i])
        {
            continue;
        }
        else
        {
            flagD=false;
            break;
        }
    }
    
    return flagD||flagI;
    
   
}

