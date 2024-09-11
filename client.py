import socket
import threading

nickname = input("Enter you nickname for the chat room >>> ")
client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(('server_IP_address',4444))

def recv_msg():
    while True:
        try:
            message = client.recv(1024).decode('utf-8')
            if message=='Enter your nickname for the chat room >>> ':
                client.send(nickname.encode('utf-8'))
            else:
                print(message)
        except:
            print("Error!!")
            client.close()
            break
 
def send_msg():
    while True:
        message = f'{nickname}: {input("")}'
        client.send(message.encode('utf-8'))

recv_thread = threading.Thread(target=recv_msg)
recv_thread.start()
send_thread = threading.Thread(target=send_msg)
send_thread.start()
