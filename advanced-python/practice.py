mylist = ["banana", "cherry", 5,6,7,True]


list2 = list()
print(list2)

if "banana" in mylist:
    print(len(mylist))

mylist.append("Raahim")
mylist.insert(1, "blueberry")

print(mylist)

popped = mylist.pop()
removed = mylist.remove("banana")
mylist.reverse()

print(mylist)

numList = [-1,5,7,2,4,5]
sorted = sorted(numList)
print(sorted)

newList = [4] * 5

print(newList)


#Slicing
a = mylist[1:3]

b = mylist[::2]
print(b)

#Copying
list_cpy = mylist.copy()
slicing_cpy = mylist[:]

print(slicing_cpy)

#List Comprehension
d = [1,2,34,5]

b = [i*i for i in d] #looping
print(b)