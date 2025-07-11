a = int(input("Enter a 1st number: "))
b = int(input("Enter a 2nd number: "))

if(b==0):
    raise ZeroDivisionError("Infinity")
else:
    print(f"The division of a/b is {a/b}")