import socket
import json

from sys import argv


server = socket.socket()


def getServerInfo():

    try:
        host = argv[1]
        port = int(argv[2])
    except:
        host = 'localhost'
        port = 43220

    return host, port


def connectToServer(host, port):
    
    server.connect((host, port))


def sendCreds(name, color):

    data =  {"name": name , "color": color}
    data = json.dumps(data)
    server.send(data.encode())


def beginGame():

    while True:

        # print('Waiting for the server to send data...')
        serverResp = server.recv(16384)
        print(serverResp.decode())
        try:
            serverResp = json.loads(serverResp)
            act = input('Action: ')
            server.send(act.encode())
        except json.JSONDecodeError:
            continue


if __name__ == "__main__":
    
    host, port = getServerInfo()
    connectToServer(host, port)
    name, color = input().split()
    sendCreds(name.upper(), color.upper())
    beginGame()