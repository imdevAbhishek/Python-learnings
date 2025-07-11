import random

computer=random.randint(1,101)
i=1
you=0

while you != computer:
    you=int(input("Enter your guess between 1 to 100: "))
    if(you==computer):
        break
    else:
        if you>computer:
           print("Lower number please")
        elif you<computer:
           print("Higher number please")
    i+=1


print(f"Your guess is right! You guessed it in {i} tries.")
