f=open("poems.txt","r")
content=f.read()
f.close()

word="twinkle"
count=content.count(word)
print(count)
if word.lower() in content.lower():
    print(f"{word} is present in the poem")
else:
    print("not present")