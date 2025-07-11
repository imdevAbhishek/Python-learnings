with open("log.txt", "r") as f:
    lines=f.readlines()

word="python"
lineno=1
for line in lines:
    if word in line:
        print(f"python is present in line {lineno}")
        break
    lineno+=1
else:
    print("not present")