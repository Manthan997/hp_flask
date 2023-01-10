#this file will be used only once to create a .db file and
#  then you make a direct connection to it while later using it

import sqlite3
# creates a connection to database.db. if not present .db file will be created recursively
connection = sqlite3.connect('database.db')

#to set the table structure we import thw schema from a .sql script file
with open('schema.sql') as f:
    connection.executescript(f.read())
    #this function takes .sql and imprints that on .db

cur = connection.cursor() #variable to set the cursor
# you can use cur.execute to actually make tables instead of .sql files but in bigger 
# structures it's better to have seperate files 
# cur.execute is a function for passing sql commands in .py file/syntax/command interpretor

#below two DMLs[data manipulation language] insert values in the table.
cur.execute("INSERT INTO posts (title, content) VALUES (?, ?)",
            ('First Post', 'Content for the first post')
            )
            # use '?' instead of direct python variable insertion to protect from sql injections

cur.execute("INSERT INTO posts (title, content) VALUES (?, ?)",
            ('Second Post', 'Content for the second post')
            )

#uploads the changes to .db file. this created a database transaction.
connection.commit()
#close the connection with database for security reasons 
connection.close()