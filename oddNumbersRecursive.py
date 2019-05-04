n=6
def printOdd(n):
    
    if n>=1:
        printOdd(n-2)
        print(n)
printOdd(n-1)