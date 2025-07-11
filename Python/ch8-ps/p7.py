l= ["harry","rohan","shubham","an"]
n=[]
def rem(l, word):
    for i in l:
        if (i!=word):
            n.append(i.strip(word))
    return n
    
print(rem(l, "an"))