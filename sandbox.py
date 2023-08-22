# arr = [1,2,3,4]
# subset = []
# subsets = []


# def genSubsets(arr, i, subset, subsets):
#     if i == len(arr): 
#         subsets.append(subset.copy())
#     else:
#         genSubsets(arr, i+1, subset + [arr[i]], subsets)
#         genSubsets(arr, i+1, subset, subsets)

# genSubsets(arr, 0, subset, subsets)

# print(subsets)



# # def getPos(binaryArray):
# #     positions = []
# #     i = 0
# #     for i in range((len(binaryArray) - 1)):
# #         if binaryArray[i] == 1 or binaryArray[i] == "1":
# #             positions.append(i)
            
# #     return positions

# # # converted = bin(12)[2:]
# # # print(converted)
# # # print(getPos(bin(12)[2:]))


# # def genSubsets2(arr): 
# #     subsets = []
# #     for i in range(2**(len(arr))):
# #         #Getting positions of ones
# #         positions = getPos(bin(i)[2:])
# #         # print(positions)
# #         subset = []
        
# #         #Iterating through positions array
# #         for j in range(len(positions)): 
            
# #             if len(positions) == 0:
# #                 subset = []
# #             else:
# #                 #Subtract array length from positions in order to reverse
# #                 subset.append(arr[(len(arr) - 1) - positions[j]])
        
# #         subsets.append(subset)
# #         subset = []
# #     return subsets

# # print(genSubsets2([1,2,3,4]))

        


data = {"a", "B"}

data.add("C")
print(data)

if "a" in data:
    print(data)