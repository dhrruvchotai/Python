#Dictionary

data = {}  #This is an empty dictionary.
data = {
    #Write key names inside ""
    "name" : "DHRUV",
    "id" : 101,
    "marks" : 2.5,
    "nums" : [1,2,3,4,5]
}


print(type(data))
#Also remember access value with keynames in ""
print(data["id"])
print(data["marks"])
print(data["nums"])
print(data)

#Methods
print("Length of dict : ",len(data))
print(data.items())
print(data.keys())
print(data.values())

data.update({"Year" : 2006,"marks":95}) #Here key marks already present there so it will update it!
print(data)


#For adding some data to the dict.
name = input("Enter name : ")
lang = input("Enter language : ")

data.update({name:lang}) 

print(data)

#NEW feature in py
#Merge two dicts

dict1 = {'val1':100,'val2':99}
dict2 = {"val3":212,'val4':107}

dict3 = dict1 | dict2
print(f"Merged dicts : {dict3}")