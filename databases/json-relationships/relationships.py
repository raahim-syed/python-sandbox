import json
import sqlite3


connection = sqlite3.connect("../db/roster.sqlite")
query = connection.cursor()

# Resetting DB
query.execute("DROP TABLE IF EXISTS User")
query.execute("DROP TABLE IF EXISTS Course")
query.execute("DROP TABLE IF EXISTS Member")


data_model = """
CREATE TABLE User (
    id     INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name   TEXT UNIQUE
);

CREATE TABLE Course (
    id     INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    title  TEXT UNIQUE
);

CREATE TABLE Member (
    user_id     INTEGER,
    course_id   INTEGER,
    role        INTEGER,
    PRIMARY KEY (user_id, course_id)
)
"""

# Creating Table Instances
query.executescript(data_model)


with open("../files/roster_data.json") as json_file:
    data = json.loads(json_file.read())
    
    for object in data:
        query.execute("INSERT OR IGNORE INTO User (name) Values (?)", (object[0],))
        query.execute("SELECT id FROM User WHERE name=?", (object[0],))
        user_id = query.fetchone()[0]
        
        query.execute("INSERT OR IGNORE INTO Course (title) Values (?)", (object[1],))
        query.execute("SELECT id FROM Course WHERE title=?", (object[1],))
        course_id = query.fetchone()[0]
        
        # print(user_id, course_id, object[2])
        
        query.execute("INSERT OR IGNORE INTO Member (user_id, course_id, role) Values (?, ?, ?)", (user_id, course_id, object[2], ))
    
    connection.commit()
    
for row in query.execute("""
                         SELECT User.name,Course.title, Member.role FROM 
                            User JOIN Member JOIN Course 
                            ON User.id = Member.user_id AND Member.course_id = Course.id
                            ORDER BY User.name DESC, Course.title DESC, Member.role DESC LIMIT 2;"""):
    print(row)
    pass

for row in query.execute("""
                         SELECT 'XYZZY' || hex(User.name || Course.title || Member.role ) AS X FROM 
                            User JOIN Member JOIN Course 
                            ON User.id = Member.user_id AND Member.course_id = Course.id
                            ORDER BY X LIMIT 1;
                         """):
    print(row[0])