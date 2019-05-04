n = 6
def printNumOdd(n):
    if n>=0:
        printNumOdd(n-2)
        print(n)

printNumOdd(n)
