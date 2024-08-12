comments = ["Make a lot of money","click this","subscribe","buy now"]
comment = input("Enter your comment : ")

#(PENDING TO UNDERSTAND!!!)
if any(spam in comment for spam in comments):
    print("Stop spamming in the comment section.")
else:
    print("It is a valid comment!!")

temp = "Dhruv"

txt = input("Enter some text : ")
if(temp in txt):
    print("This is talking about Dhruv.")
else:
    print("Nothing about Dhruv.")
