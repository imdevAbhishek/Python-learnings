def gretest():
    a=int(input("enter a number: "))
    b=int(input("enter a number: "))
    c=int(input("enter a number: "))

    if(a>b and a>c):
        print(f"{a} is gretest")
    elif(b>a and b>c):
        print(f"{b} is gretest")
    else:
        print(f"{c} is gretest")

gretest()