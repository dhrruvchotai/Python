import numpy as np

#np.sort numerical
np1 = np.array([9,3,6,2,0,1,4,14])
print(f"Sorted numerical array is : {np.sort(np1)}")

#np.sort alphabetical
np2 = np.array(["Meet","Het","DHRUV","Mann","jhon"]) #here first letter of j is small so it will appear last.
print(f"Sorted alphabetical array is : {np.sort(np2)}")

#np.sort boolean T/F
np3 = np.array([True,False,False,True,True]) #you can consider F as 0 and T as 1.
print(f"Sorted boolean array is : {np.sort(np3)}")

#sort returns a copy does not change the original array
np4 = np.array([14,4,21,10,20,6])
sortednp4 = np.sort(np4)
print(f"Sorted np4 is : {sortednp4}")
print(f"Original np4 is : {np4}")


#2-D Array
#here individually the rows are sorted not the whole array.
np5 = np.array([[1,9,4,7],[14,21,10,2]])
print(f"Sorted 2-D array np5 is : {np.sort(np5)}")

#.....Till l7!!