st = "onedf"
def reverse(index,st):
    if index >= len(st) or st == None:
        print(st)
        return st
    reverse(index+1,st)
    print(st[index])

reverse(0,st)

# 