filenames=["1.txt", "2.txt", "3.txt"]

for name in filenames:  
    try:
        with open(name, "r") as f:
           content=f.read()
           print(f"\n Content of {name}:\n{content}")

    except Exception as e:
        print(f"File {name} not found: {e}")

print("Thank you!")
