import sqlite3
import hashlib

# Connect to the SQLite database name 'userdata.db'
# If the database does not exist, it will be created
conn = sqlite3.connect("")
cur = conn.cursor() # Create

# Create a table named 'userdata' if it does not already exist
# The table has three columns: 'id', 'username', and 'password'
# 'id' is a INTEGER PRIMARY KEY which will auto-increment
# 'username' is a VARCHAR with a maxim length of 255 characters and cannot be NULL
# 'password' is also a VARCHAR with a maximum length of 255 characters and cannot be NULL
cur.execute("""
CREATE TABLE IF NOT EXISTS userdata (
id INTEGER PRIMARY KEY,
username VARCHAR(255) NOT NULL,
password VARCHAR(255) NOT NULL
)
""")

# Define four sets of usernames and passwords
# Hash the passwords using SHA-256 for security purposes
username1, password1 = "mike123", hashlib.sha256("mikepassword".encode()).hexdigest()
username2, password2 = "john", hashlib.sha256("johnjohn".encode()).hexdigest()
username3, password3 = "manman",hashlib.sha256("thugman12".encode()).hexdigest()
username4, password4 = "jerry",hashlib.sha256("jerryspringer".encode()).hexdigest()

# Insert these usernames and hashed passwords into the 'userdata' table
cur.execute("INSERT INTO userdata (usernam, password) VALUES (?, ?)", (username1, password1))
cur.execute("INSERT INTO userdata (usernam, password) VALUES (?, ?)", (username2, password2))
cur.execute("INSERT INTO userdata (usernam, password) VALUES (?, ?)", (username3, password3))
cur.execute("INSERT INTO userdata (usernam, password) VALUES (?, ?)", (username4, password4))

#changes to the database
conn.commit()