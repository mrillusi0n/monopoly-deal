import json
import socket
import time
from queue import Queue
from threading import Thread

from cards import initializeDeck
from player import Player

HOST = ''
PORT = 43220
SOCK = socket.socket()

CARDS = []
PLAYER_CLIENTS = Queue(6)
NP = 0

playerCount = 0


class Handler(Thread):

    def __init__(self, sock):
        Thread.__init__(self)
        self.client = sock

    def run(self):

        resp = self.client.recv(1024)
        details = json.loads(resp)
        newPlayer = Player(details['name'], details['color'].upper())
        PLAYER_CLIENTS.put((self.client, newPlayer))
        print(f'{newPlayer} added successfully.')


def broadcastMsg(msg):

    print(msg)

    for sock, _ in PLAYER_CLIENTS.queue:
        sock.send(msg.encode())


def makeJSON(player):

    d = {'hand': None, 'ground': Player.table}
    d['hand'] = {key: value for key, value in enumerate(list(
        map(str, player.getCardsInHand())))}  # list(map(str, player.getCardsInHand()))
    return json.dumps(d, indent=4)


def distributeCards():

    for _, player in PLAYER_CLIENTS.queue:
        player.pickCards(CARDS, 5)


def beginGame():

    global NP

    print('Beginning game...')
    distributeCards()
    print('Distributed Cards.')

    while True:

        # print(f'Cards in the deck: {len(CARDS)}')
        currSock, currPlayer = PLAYER_CLIENTS.get()
        # print(f'{currPlayer}:', end=' ')
        currPlayer.pickCards(CARDS, 2)
        # JSON containing current player cards and other players' ground cards
        cards = makeJSON(currPlayer)
        currSock.send(cards.encode())
        resp = currSock.recv(1024).decode()
        cardPlayed = currPlayer.getCardsInHand()[int(resp)]
        currPlayer.play(cardPlayed)
        msg = f'{currPlayer} played {cardPlayed}.'
        broadcastMsg(msg)
        PLAYER_CLIENTS.put((currSock, currPlayer))


def initServer():

    global NP
    global CARDS

    SOCK.bind((HOST, PORT))
    SOCK.listen(6)
    CARDS = initializeDeck()
    NP = int(input('Number of Players: '))


def getClients():

    global NP
    global SOCK
    global PLAYER_CLIENTS

    threads = []
    pc = NP

    while pc:

        # print('Waiting for a player...')
        playerClient, addr = SOCK.accept()
        print(f'New Player from {addr}.')
        newThread = Handler(playerClient)
        threads.append(newThread)
        newThread.start()
        pc -= 1

    for t in threads:
        t.join()


if __name__ == "__main__":

    initServer()
    getClients()
    beginGame()
