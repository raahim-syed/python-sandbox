#Objects that belong together
#Parenthesis are optional in tuples
myTuple = "Max",17,False

print(myTuple)

#tuple constructor
tupleFuntion = tuple([1,2,"Raahim"])
print(myTuple[0])

#tuple to list
my_list = list(myTuple)
print(my_list)

#Unpacking
name, age, isGraduated = myTuple
print(isGraduated)

#Another Way

largeTuple = [1,2,3,4,5,6,7,8,9]

start, second, *middle, end = largeTuple
print(middle)

