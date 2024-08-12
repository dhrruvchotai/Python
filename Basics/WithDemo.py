#Using with uh can do like this and here dont need to close the file explicitly!!
with open('Temp.txt') as f:
    print(f.read())
 
with open("Temp.txt","a") as f:
    f.write("\nDHRUV is a very calm boy.")

count = 0

with open('Temp.txt') as f:
    str = f.readline()
    while(str != ""):
        if("DHRUV" in str):
            count += 1
        str = f.readline()
print(f"The count of word DHRUV in the file is : {count}")