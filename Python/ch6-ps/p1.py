a=int(input("enter a num: "))
b=int(input("enter a num: "))
c=int(input("enter a num: "))
d=int(input("enter a num: "))

if b > a and b > c and b > d:
    print(b," is the greatest")
elif c > a and c > b and c > d:
    print(c," is the greatest")
elif d > a and d > b and d > c:
    print(d," is the greatest")
else:
    print(a, " is the greatest")
