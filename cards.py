import random
from pprint import pprint

class Card:
    """Super Class"""

    def __init__(self, value):
        self.value = value
        self._isPlayed = False

    def __repr__(self):
        return f'<{self.__class__.__name__}> Value = {self.value} M'


class CashCard(Card):
    """This is Money. One and only one CashCard must be visible to other players."""

    def __init__(self, value):
        super().__init__(value)
        self.onTop = True
        
    def flip(self):
        self.onTop = not self.onTop
        

class ActionCard(Card):
    """Played against one or more players."""

    def __init__(self, value):
        super().__init__(value)


class DealBreaker(ActionCard):
    """Can be played against a player who played an action card against you."""

    def __init__(self, value):
        super().__init__(value)


class DoubleTheRent(ActionCard):
    """Played over the RentCard to ask for double the rent."""

    def __init__(self, value):
        super().__init__(value)


class DebtCollector(ActionCard):
    """..."""

    def __init__(self, value):
        super().__init__(value)


class Hotel(ActionCard):
    """..."""

    def __init__(self, value):
        super().__init__(value)


class House(ActionCard):
    """..."""

    def __init__(self, value):
        super().__init__(value)


class Birthday(ActionCard):
    """Ask every other player to pay you 2 M."""

    def __init__(self, value):
        super().__init__(value)


class JustSayNo(ActionCard):
    """Deny an ActionCard played against you."""

    def __init__(self, value):
        super().__init__(value)


class SlyDeal(ActionCard):
    """Swap PropertyCard with a player."""

    def __init__(self, value):
        super().__init__(value)


class ForcedDeal(ActionCard):
    """Ask a player to give you a PropertyCard."""

    def __init__(self, value):
        super().__init__(value)


class PassGo(ActionCard):
    """Skip to play a card."""

    def __init__(self, value):
        super().__init__(value)


class RentCard(ActionCard):
    """Ask a player to pay you the rent of the Property listed in the colors of this card."""

    def __init__(self, value, colors):
        Card.__init__(self, value)
        self.colors = colors

    def __repr__(self):
        return super().__repr__() + f' Colors = {self.colors}'


class WildRentCard(RentCard):
    """Ask for a particular person the rent of any property you own."""

    def __init__(self, value, colors):
        super().__init__(value, colors)

    def setColor(self, color):
        self.currentColor = color


class PropertyCard(Card):
    """The player who gets 3 full sets of different colored properties will be the winner."""

    def __init__(self, value, color, collection):
        super().__init__(value)
        self.color = color
        self.collection = collection

    def __repr__(self):
        return super().__repr__() + f' Color = {self.color} Collection = {self.collection}'


class BiPropertyWildCard(PropertyCard):
    """This WildCard can act as any of the two colors."""

    def __init__(self, value, color, collection):
        super().__init__(value, color, collection)
        self.assignedColor = None

    def assignProperty(self, color):
        self.assignedColor = color

    def __repr__(self):
        return super().__repr__() + f' Assigned = {self.assignedColor}'



class MultiPropertyWildCard(PropertyCard):
    """This WildCard can act as any color."""

    def __init__(self, value, color, collection):
        super().__init__(value, color, collection)
        self.assignedColor = None

    def assignProperty(self, color):
        self.assignedColor = color

    def __repr__(self):
        return super().__repr__() + f' Assigned = {self.assignedColor}'



def initializeDeck():

    CARDS = []

    # initialize all cards...
    for _ in range(2):
        CARDS.append(DealBreaker(5))
        CARDS.append(DoubleTheRent(1))
        CARDS.append(PropertyCard(1, 'BROWN', (1, 2)))
        CARDS.append(PropertyCard(1, 'PGREEN', (1, 2)))
        CARDS.append(PropertyCard(4, 'BLUE', (3, 8)))
        CARDS.append(BiPropertyWildCard(2, ('MAGENTA', 'ORANGE'), None))
        CARDS.append(BiPropertyWildCard(3, ('RED', 'YELLOW'), None))
        CARDS.append(MultiPropertyWildCard(0, 'All', None))
        CARDS.append(RentCard(1, ('BLUE', 'GREEN')))
        CARDS.append(RentCard(1, ('LBLUE', 'BROWN')))
        CARDS.append(RentCard(1, ('MAGENTA', 'ORANGE')))
        CARDS.append(RentCard(1, ('BLACK', 'PGREEN')))
        CARDS.append(RentCard(1, ('RED', 'YELLOW')))
        CARDS.append(CashCard(5))

    for _ in range(3):
        CARDS.append(DebtCollector(3))
        CARDS.append(Hotel(4))
        CARDS.append(House(3))
        CARDS.append(Birthday(2))
        CARDS.append(JustSayNo(4))
        CARDS.append(SlyDeal(4))
        CARDS.append(PropertyCard(4, 'GREEN', (2, 4, 7)))
        CARDS.append(PropertyCard(1, 'LBLUE', (1, 2, 3)))
        CARDS.append(PropertyCard(2, 'ORANGE', (1, 3, 5)))
        CARDS.append(PropertyCard(2, 'MAGENTA', (1, 2, 4)))
        CARDS.append(PropertyCard(3, 'RED', (2, 3, 6)))
        CARDS.append(PropertyCard(3, 'YELLOW', (2, 4, 6)))
        CARDS.append(WildRentCard(3, 'All'))
        CARDS.append(CashCard(4))
        CARDS.append(CashCard(3))

    for _ in range(4):
        CARDS.append(ForcedDeal(3))
        CARDS.append(PropertyCard(2, 'BLACK', (1, 2, 3, 4)))

    for _ in range(5):
        CARDS.append(CashCard(2))
        
    for _ in range(6):
        CARDS.append(CashCard(1))

    for _ in range(10):
        CARDS.append(PassGo(1))
        
    CARDS.append(BiPropertyWildCard(4, ('BLUE', 'GREEN'), None))
    CARDS.append(BiPropertyWildCard(1, ('LBLUE', 'BROWN'), None))
    CARDS.append(BiPropertyWildCard(4, ('BLACK', 'GREEN'), None))
    CARDS.append(BiPropertyWildCard(4, ('BLACK', 'LBLUE'), None))
    CARDS.append(BiPropertyWildCard(2, ('BLACK', 'PGREEN'), None))
    CARDS.append(CashCard(10)) 

    random.shuffle(CARDS)
    return CARDS

if __name__ == "__main__":

    deck = initializeDeck()
    pprint(deck)

