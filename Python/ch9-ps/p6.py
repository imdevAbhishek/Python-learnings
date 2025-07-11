with open("log.txt", "r") as f:
    content=f.read()
word="python"
count= content.count(word)
if word in content.lower():
    print(f"python is present in log file. python present {count} times")
else:
    print("not present")