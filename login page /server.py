import sqlite3
import hashlib
import socket
import threading
def handle_connection(c):
try:
print("Client connected")

# Send a prompt to the client asking for the username
c.send("Username: ".encode())
# Receive the username from the client
username = c.recv(1024).decode().strip()
print(f"Received username: {username}")

# Send a prompt to the client asking for the password
c.send("Password: ".encode())
# Receive the password from the client
password = c.recv(1024).decode().srtip()
print(f"Received password (pre-hash): {password}")
# Hash the password using SHA-256 for security
password = hashlib.sha256(password.encode()).hexdigest()
print(f"Hashed password: {password}")

# Connect to the SQLite database
conn = sqlite3.connect("userdata.db")
cur = conn.cursor()
# Check if the username and hashed password match any entry in the database
cur.execute("SELECT * FROM userdata WHERE username = ? AND password = ?", (username, password))

# If a match is found, send a success message to the client
if cur.fetchall():
c.send("Login Succesfully!".encode())
print("Login successful")
# If no match is found, send a failure massage to the client
else:
c.send("Login Failed! WOMB WOMB".encode())
print("Login failed")

# Close the database connection
conn.close()
except Exception as e:
# If an error occurs, print the error and send an error message to the client
print(f"Error: {str(e)}")
c.send(f"Error: {str(e)}".encode)
finally:
# Close the client connection
c.close()
# Create a socket object for the server
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Bind the srver to localhost on port 3333
server.bind(("localhost", 3333))
# Start listening for incoming connections
server.listen()

print("Server started on port 3333...")

while True:
# Accept an incoming client connections
Client, addr = server.accept()
# Handle the client connection in new thread
threading.Thread(target=handle_connection, args=(Client)).start()
