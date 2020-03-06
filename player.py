import json

from collections import defaultdict
from cards import initializeDeck

class Player:
    """Represents a person playing the game."""

    table = defaultdict(list)

    def __init__(self, name, color):
        self.name = name
        self._cards = {'hand': set(), 'played': set()}
        self.color = color
        
    def play(self, card):
        self._cards['hand'].remove(card)
        self._cards['played'].add(card)
        self.table[str(self)].append(str(card))

    def pickCards(self, deck, n):
        for _ in range(n):
            self._cards['hand'].add(deck.pop())

    def getCardsInHand(self):
        return list(self._cards['hand'])

    def getCardsPlayed(self):
        return self._cards['played']

    def __str__(self):
        return self.name

if __name__ == "__main__":
    
    p1 = Player('Nick', 'RED')
    p2 = Player('Kevin', 'BLUE')

    cards = initializeDeck()

    p1.pickCards(cards, 5)
    p2.pickCards(cards, 5)

    p1.play(list(p1.getCardsInHand())[2])
    p1.play(list(p1.getCardsInHand())[0])
    p2.play(list(p2.getCardsInHand())[3])
    p2.play(list(p2.getCardsInHand())[1])

    print(p1.table)
    print(json.dumps(p1.table))