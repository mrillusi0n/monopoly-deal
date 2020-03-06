from cards import initializeDeck
from player import Player
from collections import defaultdict
from pprint import pprint


def initializePlayers(numberOfPlayers):
    for i in range(numberOfPlayers):
        name = input(f'Player {i+1}: ')
        color = colors[i] # input('Color: ')
        cards = set()
        for _ in range(CARDS_PER_PLAYER):
            cards.add((CARDS.pop()))
        PLAYERS.append(Player(name, color.upper()))


CARDS_PER_PLAYER = 5
CARDS = initializeDeck()

# names = ['Phoenix', 'Nick', 'Snow', 'BayMAX']
colors = ('BLUE', 'RED', 'CYAN', 'WHITE')
PLAYERS = []
np = int(input('Players: '))
ground = defaultdict(set) # maintain each player's cards on ground: key - player, value - set of cards
turn = 0
# I guess I should define action dict

# begin the game
print('BEGINNING GAME...', end='\n'*2)
initializePlayers(np)

while True:
    currentPlayer = PLAYERS[turn]
    currentPlayer.pickTwoCards(CARDS)
    print(repr(currentPlayer) + '\'s Turn')
    currPlayerPlayableCards = currentPlayer.getCardsInHand()
    pprint(currPlayerPlayableCards)
    action = input('Action: ')
    if action == 'play':
        cardNum = int(input('Card: '))
        cardChosen = currPlayerPlayableCards[cardNum]
        currentPlayer.play(cardChosen)
        text = f'{currentPlayer} played {cardChosen}.'
        print(text)
        ground[currentPlayer].add(cardChosen)
    if action == 'skip':
        continue
    if action == 'quit':
        break
    turn = (turn + 1) % np
    print()