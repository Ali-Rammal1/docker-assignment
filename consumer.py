import socket

HOST = "producer"  # Docker will resolve this to the producer container
PORT = 5000
DATA_FILE = "/data/logs.txt"  # store in the docker volume


client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


print("Connecting to producer...")
client_socket.connect((HOST, PORT))
print("Connected to producer.")

while True:
    data = client_socket.recv(1024).decode()  # Receive data
    if not data:
        break  # break if connection is closed /lost
    
    file = open(DATA_FILE, "a") # a for append
    file.write(data) 
    file.close()  
    print("Received and saved:", data.strip())

