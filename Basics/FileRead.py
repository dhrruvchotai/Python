f = open("Temp.txt")

#Gives simple data.
data = f.read()
print(data)
f.close() #MOST IMP
 
#Gives list of the lines.
f = open("Temp.txt")
listoflines = f.readlines()
print(listoflines,type(listoflines))
f.close()
