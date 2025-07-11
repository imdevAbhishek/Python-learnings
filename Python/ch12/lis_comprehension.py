mylist =[1, 2, 9, 5, 3, 5]

squaredlist1 = []
squaredlist2 =[]
for item in mylist:
    squaredlist1.append(item*item)

# Easy way
squaredlist2 = [i*i for i in mylist]

print(squaredlist1)
print(squaredlist2)