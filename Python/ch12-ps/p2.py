a = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for index, item in enumerate(a):
    if index in (3,5,7):
        print(f"The item number at index {index} is {item}")