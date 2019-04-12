st = "gayatri"
def reverse(index,st):
    if index >= len(st) or st == None:
        return st
    reverse(index+1,st)
    print(st[index])
reverse(0,st)
