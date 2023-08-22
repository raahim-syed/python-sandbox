import sqlite3
import xml.etree.ElementTree as ET

conn = sqlite3.connect("./db/songs.sqlite")

query = conn.cursor()

# Reset Everytime
query.execute("DROP TABLE IF EXISTS Artist")
query.execute("DROP TABLE IF EXISTS Genre")
query.execute("DROP TABLE IF EXISTS Album")
query.execute("DROP TABLE IF EXISTS Track")

# Creating Tables in Database
data_model = """
CREATE TABLE Artist (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name    TEXT UNIQUE
);

CREATE TABLE Genre (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name    TEXT UNIQUE
);

CREATE TABLE Album (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    artist_id  INTEGER,
    title   TEXT UNIQUE
);

CREATE TABLE Track (
    id  INTEGER NOT NULL PRIMARY KEY 
        AUTOINCREMENT UNIQUE,
    title TEXT  UNIQUE,
    album_id  INTEGER,
    genre_id  INTEGER,
    len INTEGER, rating INTEGER, count INTEGER
);

"""
query.executescript(data_model)

# For Finding and Return Values Form XML
def find(elem, match):
    matched = False
    
    for key in elem:
        # To return the value of the key (sibling of key)
        if matched: return key.text 
        
        if key.tag == "key" and key.text == match:
            matched = True
            
    return None
         

# Getting Data From File and Storing in database
file_data = open("./files/Library.xml")

# Parsing XML
xml_tree = ET.fromstring(file_data.read())
track_data = xml_tree.findall("./dict/dict/dict")

data = dict()

for track in track_data:

    if ( find(track, 'Track ID') is None ) : continue

    data["Name"] = find(track, "Name")
    data["Album"] = find(track, "Album")
    data["Genre"] = find(track, "Genre")
    data["Artist"] = find(track, "Artist")
    data["Play Count"] = find(track, "Play Count")
    data["Rating"] = find(track, "Rating")
    data["Total Time"] = find(track, "Total Time")
    
    # print(f"{data['Name']}, {data['Genre']}, {data['Artist']}, {data['Album']}, {data['Play Count']}")
    
    if data["Name"] is None or data["Artist"] is None or data["Album"] is None or data["Genre"] is None: continue
    
    # Inserting Data into Database
    query.execute("INSERT OR IGNORE INTO Artist(name) Values (?)", (data["Artist"], ))
    query.execute("SELECT * FROM Artist WHERE name=?", (data["Artist"], ))
    artist_id = query.fetchone()[0]
    
    
    query.execute("INSERT OR IGNORE INTO Genre(name) Values (?)", (data["Genre"], ))
    query.execute("SELECT * FROM Genre WHERE name=?", (data["Genre"], ))
    genre_id = query.fetchone()[0]
    
    query.execute("INSERT OR IGNORE INTO Album(artist_id, title) Values (?, ?)", (artist_id, data["Album"], ))
    query.execute("SELECT * FROM Album WHERE title=?", (data["Album"], ))
    album_id = query.fetchone()[0]
    
    # print(artist_id, genre_id, album_id)
    
    query.execute("INSERT OR IGNORE INTO Track(title, album_id, genre_id, len, rating, count) VALUES (?, ?, ?, ?, ?, ?)", 
                  (data["Name"], album_id, genre_id, data["Total Time"], data["Rating"], data["Play Count"], ))

    
conn.commit()
    

result = query.execute("""SELECT Track.title, Artist.name, Album.title, Genre.name 
    FROM Track JOIN Genre JOIN Album JOIN Artist 
    ON Track.genre_id = Genre.ID and Track.album_id = Album.id 
        AND Album.artist_id = Artist.id
    ORDER BY Artist.name LIMIT 3""")

for data in result:
    for col in data:
        print(col)
    

# query.close()
file_data.close()