with open("this.txt", "r") as f:
    content=f.read()

with open("this1.txt", "r") as f:
    content1=f.read()

if content ==content1:
    print("Both the files are identical.")
else:
    print("Not identical")