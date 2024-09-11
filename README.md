# Client-Server-Communication-System

# Setting Up and Using the Client-Server Communication System

# Configure the Server:
Open the server.py file.
Replace the placeholder 'server_IP_address' with the actual IP address of the server machine (the computer that will act as the server).

# Configure the Clients:
Open the client.py file.
Replace the placeholder 'server_IP_address' with the IP address of the server machine (the same IP used in the server.py file).

# Start the Server:
Execute the server.py script on the server machine to start the server.
The server will listen for incoming connections from clients and handle message routing between them.

# Connect the Clients:
Run the client.py script on each client machine.
Each client will connect to the server using the IP address provided in the client.py file.

# Start Chatting:
Once the clients are connected, they can begin exchanging messages.
All communication between clients will pass through the server, which facilitates the message exchange.

# Important Notes:
Server Dependency: Clients cannot communicate directly with each other. All messages must go through the server, which acts as an intermediary to ensure that each client receives the messages sent by others.
Communication Flow: Every message sent by a client is received by the server and then broadcast to all other connected clients.

By following these steps, you will successfully set up a system where clients can communicate through a centralized server.
