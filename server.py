import socket
import threading

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind(('server_IP_address',4444))
server.listen()
clients = []
nicknames = []
def broadcast(message):
    for client in clients:
        client.send(message)

def client_handling(client):
    while True:
        try:
            message = client.recv(1024)
            broadcast(message)
        except:
            index = clients.index(client)
            clients.remove(client)
            client.close()
            broadcast((f"{nickname } has been disconnected from the chat room !").encode
                      ())
            nickname = nicknames[index]
            nicknames.remove(nickname)
            break
    
def receive():
    while True:
        print(f"server started listening...")
        client, address = server.accept()
        print(f"{str(address)} has been connected!")
        # deff
        client.send(("Enter your nickname for the chat room >>> ").encode())
         # deff
        nickname = client.recv(1024).decode()
        nicknames.append(nickname)
        clients.append(client)
        print((f"{nickname} has been joind in the chat room!").encode())
        broadcast((f"{nickname} has been joind in the chat room!").encode())
        thread = threading.Thread(target=client_handling,args=(client,))
        thread.start()

receive()




