try:
    a=int(input("Enter a number: "))
    print(a) 

except ValueError as v:
    print("V")

except Exception as e:
    print("e")

print("thank you")