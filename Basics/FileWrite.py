str = "DHRUV is a handsome boy."

#Open file in write mode.
f = open("Temp.txt","w")
f.write(str+"\n")
f.close()

#Open file in append mode.
f = open("Temp.txt","a")
f.write("Yes, "+str)
f.close()
