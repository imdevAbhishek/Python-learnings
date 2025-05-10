# name=input("enter your name: ")
# date=int(input("enter todays date: "))

# print(f"letter=\n\tDear {name},\n\tyou are selected!\n\t{date}")

letter='''Dear <|name|>,
          you are selected!
          <|date|>
          '''

print(letter.replace("<|name|>","abhi").replace("<|date|>","20 sep 2020"))