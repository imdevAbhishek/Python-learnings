def pr(n):
    if(n==0):
        return
    print("*" * n)
    pr(n-1)

pr(3)