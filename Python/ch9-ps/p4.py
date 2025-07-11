word="donkey"
new_word="#####"

with open("p4.txt", "r") as f:
    content=f.read()
content=content.replace(word,new_word)

with open("p4.txt", "w") as f:
    f.write(content)
