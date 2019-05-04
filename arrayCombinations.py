arr = [1,2,3]
def arrayCombo(arr,i,j):

    if(j==len(arr)-1):
        print(arr[i],arr[j])
        return 0
    else:
        arrayCombo(arr,i,j+1)
        print(arr[i],arr[j])
        arrayCombo(arr,i+1,j+1)
        print(arr[i],arr[j])
arrayCombo(arr,0,1)
