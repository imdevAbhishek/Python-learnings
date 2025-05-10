s1=int(input("enter a s1 marks"))
s2=int(input("enter a s2 marks"))
s3=int(input("enter a s3 marks"))

t=(s1+s2+s3)/3
print(t)
if (t>40 and s1>33 and s2>33 and s3>33):
    print("pass")
else:
    print("fail")