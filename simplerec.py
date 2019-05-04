arr  = [1,2,3,4]
def rec(arr,index):
    if (index ==len(arr)):
        print(arr[index-1])
        return arr[index-1]
    
    rec(arr,index+1)
    print(st)
    
a=rec(arr,0)
