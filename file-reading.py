# fileData = open("employee.txt", "r")

# print(fileData.readable())

# print(fileData.readline())
# print(fileData.readlines())

infile = open("employee.txt", "a")
infile.write("Usman - Sweeper \n")

outFile = open("employee.txt", "r")


for line in outFile.readlines():
    print(line)



infile.close()
outFile.close()







