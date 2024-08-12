import random

print(f"Using random() num is : {random.random()}") #between 0 to 1 floating

print(f"Using random() num is : {random.randint(0,10)}") #between given range int

print(f"Using uniform() num is : {random.uniform(1.3,3.3)}") #between given range float

list = ["banana","apple","DHRUV",4,14]

print(f"Using choice() elmt or num is : {random.choice(list)}") #genrare random from list

print(f"Using sample() sublist is : {random.sample(list,2)}") #k-sized sublist from given list

print(f"Using suffle() new suffled list is : {random.shuffle(list)}") #suffles the given list

random.seed(14) #here to remember next time which sequence to generate
print(f"num1 using after seed : {random.randint(11,20)} ")
print(f"num1 using after seed : {random.randint(11,20)} ")

random.seed(14) #dont remember to set seed.
print(f"num3 using after seed : {random.randint(11,20)} ")
print(f"num4 using after seed : {random.randint(11,20)} ")
