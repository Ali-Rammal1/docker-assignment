import socket
import random
import time

HOST = "0.0.0.0"  # Listen on all network interfaces
PORT = 5000      

# tcp socket on port 5000
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen(1)  #1 connection only

print(f"Producer is listening on port {PORT}...")

conn, addr = server_socket.accept()
print(f"Connected by {addr}")

while True:
    number = random.randint(1, 100)  # generates a random number
    message = str(number)+"\n"
    
    try:
        conn.sendall(message.encode())  # Send the number
        print("Sent:", number)
    except BrokenPipeError:
        print("Connection lost. Waiting for a new connection...")
        conn, addr = server_socket.accept()
        print(f"Connected by {addr}")
    
    time.sleep(5)  # wait 5 seconds before sending the next number

