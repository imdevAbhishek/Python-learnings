n = int(input("ENter a number to print table: "))

multipyList = [f"{n} x {i} = {n*i}" for i in range(1,11)]

print(multipyList)

with open("table.txt","w") as f:
    for line in multipyList:
       f.write(line + "\n")
