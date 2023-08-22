friends = ["Rafay", "Shahzaib", "Natsu", "Shahmeer"]
luckyNumber = [666, 777, 7, 989]

#friends.extend(luckyNumber)
friends.append("luckyNumber")
friends.insert(2, "Sallar")
friends.remove("Sallar")
#friends.clear()

#Tuples (Immutable)
coordinates = (4,5)

# print(coordinates)

numberGrid = [
    [1, 2, 3],
    [4, 5, 6],
    [0, 3, 2],
    [5,6,7]
]  
for row in range(len(numberGrid)):
    print("||")
    for column in range(len(numberGrid[row])):
        print(str(numberGrid[row][column]) + ", ")

