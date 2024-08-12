import random

def game():
    score = random.randint(1,100)
    
    with open("High_Score.txt") as f:
        highScore = f.read()

        if(highScore != ""):
            highScore = int(highScore)
        else:
            highScore = 0


    if(score > highScore):
        with open('High_Score.txt','w') as f:
            f.write(str(score))
            score = highScore

    print(f"Cureent score is : {score} and HighScore is : {highScore}")

game()  