

try: 
    number = int(input("Enter a number: "))
    value = 10/0   
except ZeroDivisionError as err: 
    print("Don't divide by zero")
except ValueError:
    print("INvalid Input")
    