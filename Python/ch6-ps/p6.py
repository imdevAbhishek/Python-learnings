marks=int(input("enter you marks to check grade:"))

if(marks<=100 and marks>=90):
    print("Ex")
elif(marks<=90 and marks>=80):
    print("A")
elif(marks<=80 and marks>=70):
    print("B")
elif(marks<=70 and marks>=60):
    print("C")
elif(marks<=60 and marks>=50):
    print("D")
else:
    print("fail")