import os

with open("Temp.txt") as f:
    content = f.read()

with open("NewTemp.txt","w") as f:
    f.write(content)

os.remove("Temp.txt")

print("Old file deleted and New created.")