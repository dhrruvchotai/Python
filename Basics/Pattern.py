n= 5

print("P1 : \n")
for i in range (1,n+1):
    print(" "* (n-i),end="")
    print("*"* (2*i -1),end="\n")
print("\n")

print("P2 : \n")

for i in range (1,n+1):
    print("*"*i)
print("\n")

print("P3 : \n")

for i in range(n+1,0,-1):
    print("*"*i)
print("\n")

print("P4 : \n")

for i in range(1,n+1):
    print(" "*(n-i),end="")
    print("*"*i,end="\n")
print("\n")

print("P5 : \n")

for i in range(n,0,-1):
    print(" "*(n-i),end="")
    print("*"*i,end="\n")
print("\n")

print("P6 : \n")

for i in range (1,n+1):
    if (i == 1 or i == n):
        print("*"*n,end="")
        print("\n")
    else:
        print("*",end="")
        print(" "*(n-2),end="")
        print("*",end="")
        print("\n")