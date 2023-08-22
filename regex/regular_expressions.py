import re


data = "From stephen@uct.ze.au Sat Jan 5 09:14:21"

with open("data.txt") as file:
    print(sum(int(item) for item in re.findall("[0-9]+", file.read())))

# sliced = re.findall("^From (\S+@\S+)", data)
# print(sliced)
