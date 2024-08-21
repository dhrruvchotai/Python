#Must import all the require things like list tuple dict from typing module
#Without this it will give an error.

from typing import List,Tuple,Dict,Union

a : List[int] = [1,2,3,4.5]
b : Tuple[str,int] = ("DHRUV",1)
c : Dict[str,int] = {"Dhruv":100,"Het":99}
d : Union[str,int,float] = 1
d = "DHRUV"
d = 21.2

print(a)
print(b)
print(c)

#By this type you can define datatype of any like variable tuple dict etc...