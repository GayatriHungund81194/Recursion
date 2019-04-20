n = 6
def printnum(n):
        if n >=0:
                printnum(n-1)
                print(n)
printnum(n)
