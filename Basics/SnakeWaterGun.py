import random 

def game():

    #Main logic

    compChoice = random.randint(0,2)

    valueDict = {"s" : 2, "w" : 0, "g" : 1}
    revValueDict = {2:"Snake", 0:"Water", 1:"Gun"}

    userInpt = input("Enter Your Choice S for Snake W for Water and G for Gun : ")
    userInpt = userInpt.lower()

    while(userInpt not in valueDict):
       userInpt =  input("Enter Valid Choice : ")

    print("\n")

    userChoice = valueDict.get(userInpt)

    if(userChoice == compChoice):
        print("----- It's a DRAW!!\n")

    elif (userChoice == 2 and compChoice == 1) or (userChoice == 0 and compChoice == 2) or (userChoice == 1 and compChoice == 0):
        print(f"----- You Win! {revValueDict.get(userChoice)} beats {revValueDict.get(compChoice)}")

    else:
        print(f"----- You Lose! {revValueDict.get(compChoice)} beats {revValueDict.get(userChoice)}")
        

    print(f"----- You choose : {revValueDict.get(userChoice)} and Computer choose : {revValueDict.get(compChoice)}")
    print("----- Game Over!!")

    #Logic to restart 

    print("\n")
    restartOrNot = input("For NewGame Enter N and to Exit Enter E : ")
    restartOrNot.lower()


    if(restartOrNot == 'n'):
        game()
    else:
        print("Thanks for playing the game!!")


#Main call
game()


