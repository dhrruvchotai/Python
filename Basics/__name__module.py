def printHello():
    print("Helllo brooo...")

printHello()

print(__name__)  #This will print that the this code is run from which file means
#If you will run this code from this file it will print __name__ == __main__
#i have imported this printHello function in file named __name__Demo so if i will run that file then 
#it will print __name__module as a output of __name__


#example

if(__name__ == '__main__'):
    print("We are directly running this code.")
else:
    print("We are running this code by importing it from another file.")