num1 = float(input("Enter a number: "))
operator = input("Enter operation: ")
num2 = float(input("Input another number: "))
result = 0

def printEquation(num1, num2, operator, result):
    return str(num1) + " " + str(operator) + " " + str(num2) + " = " + str(result)

if operator == "+":
    result = (num1 + num2)
elif operator == "-":
    result = (num1 - num2)
elif operator == "*":
    result = (num1 * num2)
elif operator == "/":
    result = (num1 / num2)
else:
    print("Invalid Operation!")
    
print(printEquation(num1, num2, operator, result))