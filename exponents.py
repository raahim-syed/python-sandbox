
print(3**3)

def raiseToPower(baseNum, powNum):
    result = 1
    for index in range(powNum):
        result = result * baseNum
    return result

print(raiseToPower(3, 9))