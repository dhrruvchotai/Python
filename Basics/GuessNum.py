import random

myNum = random.randint(1,100)

userNum = (int)(input("Enter your initial guess : "))

attempts = 0

while(True):
    attempts += 1
    if(userNum == myNum):
        print(f"You Guessed it right in {attempts} attempts.")
        break

    elif(userNum < myNum):
        userNum = int(input("Guess bigger than this : "))  

    elif(userNum > myNum):
        userNum = int(input("Guess smaller than this : "))     

    
