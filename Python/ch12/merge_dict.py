# dict1 = {"a":1,"b":2}
# dict2 = {"b":3,"c":4}
# merge = dict1 | dict2

# print(merge)


with (
    open('file1.txt') as f1,
    open('file2.txt') as f2
):
    content=(f1.read(),f2.read())
    print(content)