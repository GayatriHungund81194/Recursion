def rec(n):
    if n==1:
        return 1
    else:
        m = rec(n-1)
        #print(m)
        return m 
n1 =3
s = rec(n1)
print(s)