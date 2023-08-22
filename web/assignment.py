# http://py4e-data.dr-chuck.net/known_by_Maximilian.html
# http://py4e-data.dr-chuck.net/known_by_Maximilian.html

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup 
import ssl

def request(url):
    response =  urllib.request.urlopen(url).read()
    return response

def get_name(tag, count):
    
    link = tag.get("href", None)
    response = request(link)
    soup = BeautifulSoup(response, "html.parser")
    
    # Retrieve all of the anchor tags
    tags = soup('a') 
    
    # Base Condition
    if count == 6:
        return tag.contents[0]

    # Recusion Call
    num = 0
    for tag in tags:
        num += 1
        if num == 18:
            return get_name(tag, count + 1)

# GET Request (The First Page)
url = input("Enter URL: ")
response = request(url)

soup = BeautifulSoup(response, "html.parser")

# Retrieve all of the anchor tags
tags = soup('a')

count = 0
content = str()
for tag in tags:
    count += 1
    if count == 18:
        content = get_name(tag, 0)
        break
print(content)

        
    
    
    
