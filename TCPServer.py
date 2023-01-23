from socket import *
from threading import *

# constant serverport
serverPort = 55772

# Method for receiving incoming string
def handleClient(clientSocket, addr):
    sentence = clientSocket.recv(2048).decode()
    upperSentence = sentence.upper()
    clientSocket.send(upperSentence.encode())
    clientSocket.close()


# main program
# creates server object
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(1)
print('the server is running on port:', serverSocket)

# loop for server
while True:
    connectionSocket, addr = serverSocket.accept()
    print('connected to client from adddress:', addr)
    Thread(target=handleClient, args=(connectionSocket, addr)).start()

