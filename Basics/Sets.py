e = set() #This is an empty set.
s1 = {1,2,2,4,3} #This is filled set. 
s2 = {} #This is not a empty set this is a empty dictionary

print(type(s1),type(s2),type(e)) #set dict set

print("Len of s1 : ",len(s1)) #gives 4 cause 2 is counted only once and also enterd only once.
s1.remove(3)#if 3 is not present then gives error.
print("Popped elmt :",s1.pop())
s1.discard(3)#same as remove but if 3 is not there then no error
print("S1 : ",s1) #here repeated elements is not printed.
print("S2 : ",s2)

s3 = s1.union(s2)
print("S3 after union : ",s3)

s3 = s1.intersection(s2)
print("After intersection s3 :",s3)

s3 = s1.difference(s2) #gives elmt that is in s1 but not in s2 here o/p is 4
print("s1 diff s2 : ",s3)

s3 = s2.difference(s1) #gives elmt that is in s2 but not in s1 here o/p is 3
print("s2 diff s1 : ",s3)

s3 = s1.symmetric_difference(s2) #gives elmt that are diff in both o/p 3,4
print("s1 Symmdiff s2 : ",s3)