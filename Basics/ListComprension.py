list = [1,2,3,4,5]

sqauredList = [elmt*elmt for elmt in list]#(MAIN -> note this i have done square brackets here) it will assign i*i at each index.
halvedList = [elmt/2 for elmt in list]

print(f"squaredList is : {sqauredList}")
print(f"halvedList is : {halvedList}")