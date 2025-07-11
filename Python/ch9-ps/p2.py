import random

def game():
    score=random.randint(1,100)
    with open("highscore.txt","r") as f:
        hiscore=f.read()
        if hiscore=="":
            hiscore=0
        else:
            hiscore=int(hiscore)
    print(f"your score is {score}")
    print(f"hifhscore is {hiscore}")
    if(score>hiscore):
        with open("highscore.txt","w") as f:
            f.write(str(score))

game()
    