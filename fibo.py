def fibo(num):
    if(num==1):
        return 1
    else:
        return pow(num*num) + fibo(num-1)
print(fibo(5))
