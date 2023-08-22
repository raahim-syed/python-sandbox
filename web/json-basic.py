import urllib.request, urllib.parse, urllib.error
import json

res = urllib.request.urlopen("http://py4e-data.dr-chuck.net/comments_1770478.json").read().decode()

json_data = json.loads(res)

# print(json_data)

sum = 0
for data in json_data["comments"]:
    sum+= int(data["count"])
    
print(sum)