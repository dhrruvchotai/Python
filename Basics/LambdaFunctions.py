def square(n):
    return n*n

print(square(4))

#square of num using lambda function
squareUsingLambda = lambda n : n*n #here n is argument that functions takes and after : write your logic squareUsingLambda and this is function name.
print(squareUsingLambda(5))

#sum of 2 nums using lambda function
sum = lambda a,b : a+b
print(sum(4,4))

#table using lamba function
num = 11
print(f"Table of {num} using Lambda function")
table = lambda num,i : f"{num} * {i} = {num*i}"

for i in range(1,11):
    print(table(num,i))
