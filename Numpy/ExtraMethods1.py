import numpy as np

#Array Creation and Properties

#1 np.eye()

#used to create an identity matrix np.eye(N, M=None, k=0, dtype=float, order='C')
#n rows , m cols , k = shift diagonal,order = 'c' for (row major) & 'f' for (col major)

#n X m here n = m = 3 
np1 = np.eye(3) #rows = cols = 3 default
print(np1)

#4 X 4
print(print(np.eye(4)))

#3 X 4 
np1 = np.eye(3,4) #rows,cols
print(np1)

# 3x3 matrix diagonal shifted above the main diagonal (k=1)
np2 =  np.eye(3, k=1)
print(np2)


#2 np.linspace

#used to create arr of evenly spaced nums in given interval.
#np.linspace(start, stop, num=50, endpoint=True, retstep=False, dtype=None)
#nums means how many points to genrate in given range(default 50).
#endpoint: True (default), includes the stop value in the array; if False, excludes it.
#retstep:if fTrue then returns the step size(means gap between two.).

np3 = np.linspace(10,50,5,True,True)
print(np3)

np4 = np.linspace(1,10)
print(np4)


print('\n')

#3.random.rand and random.randint

print(np.random.rand(5))
print(np.random.randint(1,30,5)) #low high size


