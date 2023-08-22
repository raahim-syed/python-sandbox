import urllib.request

# Making Request and Getting Response (Same as file handling)
response = urllib.request.urlopen("http://data.pr4e.org/romeo.txt")

# # Printing response
# for line in response:
    
#     # Converts back to unicode
#     print(line.decode().strip())

word_count = dict()
for line in response:
    words = line.decode().split()
    
    for word in words:
        word_count[word] = word_count.get(word, 0) + 1
        
print(word_count)
        