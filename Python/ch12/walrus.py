# Example without walrus:
data = input("Enter something: ")
if len(data) > 5:
    print(f"'{data}' is long enough.")


# With walrus:
if (n := len(data := input("Enter something: "))) > 5:
    print(f"'{data}' is long enough with length {n}.")



