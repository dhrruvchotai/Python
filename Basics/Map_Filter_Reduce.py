from functools import reduce
my_list =[1,2,3,4,5]

#map
square = lambda n: n * n
sqlist = map(square, my_list)
print(list(sqlist))

#filter
def even(n):
    if(n % 2 == 0):
        return True
    else:
        return False

evenNums = filter(even,my_list)
print(list(evenNums))

#reduce (Uh need to import this from functools module before using it.  )
sum = lambda a,b : a+b
sumOfNums = reduce(sum,my_list)
print(sumOfNums)