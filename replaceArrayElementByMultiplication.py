arr=[1,2,3,4,5,6]
def rightSubarrayMult(arr,i,j):
    if (i==j):
        return 1
    else:
        lmult=arr[i+1]*rightSubarrayMult(arr,i+1,j)
        return lmult
        
def leftSubarrayMult(arr,i,j):
    if(i==j-1):
        return arr[i]
    else:
        rmult=arr[i]*leftSubarrayMult(arr,i+1,j)
        return rmult

def mult(arr):
    s=leftSubarrayMult(arr,0,2)
    print(s)
    s2=rightSubarrayMult(arr,2,5)
    print(s2)
    arr[2]=s*s2
    print(arr)
mult(arr)


