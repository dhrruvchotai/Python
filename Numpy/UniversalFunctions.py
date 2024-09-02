import numpy as np 

arr1 = np.array([-4,-3,-2,-1,0,1,2,3,4,5,6,7,8,9])

#Universal functions(ufuncs) #explore more from docs..

print(np.sqrt(arr1)) #Square root of each elmt in the arr!!!!.

print(np.absolute(arr1)) #Prints absolute val of each elmt means negative to positive!!.

print(np.exp(arr1)) #Prints exponents means 2.718^1 2.718^2.... 2.716^anyNum like that!!

print(np.max(arr1)) #Prints largest elemt
print(np.min(arr1)) #Prints smallest elmt

print(np.sign(arr1)) #Prints the sign positive(1) or negative(-1) and for 0 it is 0.

#Trigonomatric functions
#sin cos tan log sinh cosh tanh......
print(np.sin(arr1))
print(np.tan(arr1))
print(np.log(arr1))

#.....Till l3!!