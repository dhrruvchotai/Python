import numpy as np

#Copy
#Copy does not change itself or does not affect base array.
np1 = np.array([1,2,3,4,5])
np2 = np1.copy()

print(f"Original np1 from copy is :{np1}")
print(f"Orginal np2 from copy is :{np2}")

np1[0] = 14

print(f"Changed np1 from copy is : {np1}")
print(f"Original np2 from copy is : {np2}")

np2[0] = 68
print(f"Orginal np1 from copy is : {np1}")
print(f"Changed np2 from copy is : {np2}")

#View
#While view is different from copy if you change base table it will affect base table
#or if you change base table it will change view.

print('\n')

np1 = np.array([1,2,3,4,5])
np2 = np1.view()

print(f"Original np1 from view is :{np1}")
print(f"Orginal np2 from view is :{np2}")

np1[0] = 14

print(f"Changed np1 from view is : {np1}")
print(f"Original np2 from view is : {np2}")

np2[0] = 68
print(f"Orginal np1 from view is : {np1}")
print(f"Changed np2 from view is : {np2}")


#.....Till l4!!