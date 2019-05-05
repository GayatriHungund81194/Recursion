arr=[1,2,3,4]
def mult(arr,i):
    if (i==len(arr)-1):
        return arr[i]
    else:
        return arr[i]*mult(arr,i+1)
        
s = mult(arr,0)
print(s)
