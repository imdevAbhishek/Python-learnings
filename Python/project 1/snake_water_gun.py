import random

you=int(input("1 for Snake.\n2 for Water.\n3 for Gun.\nEnter your choice: "))


if you not in[1,2,3]:
    print("invali1d input.")
else:
    computer=random.choice([1, 2, 3])

    dict={1:"snake",2:"water",3:"gun"}
    print(f"You chose: {dict[you]}")
    print(f"Computer chose: {dict[computer]}")

    if(computer==you):
        print("Match is draw.")
    elif(you==1 and computer==2):
        print("you win")
    elif(you==2 and computer==3):
        print("you win")
    elif(you==3 and computer==1):
        print("you win")
    else:
        print("you lose")