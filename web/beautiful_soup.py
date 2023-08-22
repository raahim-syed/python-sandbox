import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup 
import ssl

# http://dr-chuck.com/page2.html
# http://py4e-data.dr-chuck.net/comments_42.html
# http://py4e-data.dr-chuck.net/comments_1762264.html

# SSL Certificate Stuff
context = ssl.create_default_context()
context.check_hostname = False
context.verify_mode = ssl.CERT_NONE

url = input("Enter URL: ")
response = urllib.request.urlopen(url).read()
# print(response)

soup = BeautifulSoup(response, "html.parser")

print(soup)

# Retrieve all of the anchor tags
tags = soup('span')

sum = 0
for tag in tags:
    # Look at the parts of a tag
    # print('TAG:', tag)
    # print('URL:', tag.get('href', None))
    # print('Contents:', tag.contents[0])
    # print('Attrs:', tag.attrs)
    
    sum = sum + int(tag.contents[0])

print(sum)
    
    

