import urllib.request, urllib.parse, urllib.error
import json

# address = "http://py4e-data.dr-chuck.net/json?"
address = "http://py4e-data.dr-chuck.net/json?" + urllib.parse.urlencode({"key": 42, "address": "Universitat Politecnica de Valencia"})

response = urllib.request.urlopen(address)
data = response.read().decode()


data = json.loads(data)

# data = """
#     {
#         "name": "Raahim",
#         "age": "23"
#     }
# """

for object in data["results"]:
    # for key in object.keys():
    #     if key == "place_id":
    print(object["place_id"])
    
# print(data)
# sum = 0
# for object in data:
#     # for name, count in object:
#     sum = sum + int(object["count"])
#     #     print(count)
#     print(object)
    
    
# print(sum)