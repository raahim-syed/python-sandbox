my_dict = {
    "name": "Raahim",
    "age": 21,
    "city": "Islamabad"
}

#Using Constructor
function_dict = dict(name="Mahad", age=20, city="Islamabad")

print(function_dict)

print(my_dict["name"])

my_dict["email"] = "sharaahim24@gmail.com"

del my_dict["name"]

print(my_dict)

if "age" in  my_dict:
    print(my_dict["age"])

for key, value in my_dict.items():
    print(key, ":", value)
    
print(function_dict.items())

print(len(function_dict))

#Copying
cpy_dict = dict(my_dict)
cpy_dict2 = function_dict.copy()


