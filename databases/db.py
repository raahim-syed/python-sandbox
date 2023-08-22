import sqlite3
import urllib.request, urllib.parse, urllib.error
import re

conn = sqlite3.connect("./db/assignment.sqlite")

query = conn.cursor()

# Reset Everytime
query.execute("DROP TABLE IF EXISTS Counts")
query.execute("CREATE TABLE Counts (org TEXT, count INTEGER)")

# url = "https://www.py4e.com/code3/mbox.txt?PHPSESSID=d0c30cbf30e017a08238e4998c398b6d"

# response = urllib.request.urlopen(url)

# print(response)

with open("./files/data.txt") as data:
    
    for line in data:
        if not line.startswith("From: "): continue
        # print(line)
        # Getting Email From File
        # email = line.rstrip().split(" ")[1]
        email = line.split()[1]
        
        org = re.search("@([a-zA-Z0-9.-]+)$", email).group(1)
        
        # Checking If Email Already In Database
        query.execute("SELECT count FROM Counts WHERE org=?", (org, ))
        result = query.fetchone()
        
        if result == None:
            # Insert new data
            query.execute("INSERT INTO Counts (org, count) VALUES (?, 1)", (org,))
        else:
            # Update Previous Data
            query.execute("UPDATE Counts SET count = count + 1 WHERE org=?", (org,))
        
    # The commit insists on completely writing all the data to disk every time it is called.
    conn.commit()


# Getting Data From Database
# data = query.execute("SELECT org, count FROM Counts ORDER BY count DESC LIMIT 10")

sum = 0
for row in query.execute("SELECT org, count FROM Counts ORDER BY count DESC LIMIT 3"):
    sum = sum + int(row[1])
    print(row)
        
print(sum)
query.close()

