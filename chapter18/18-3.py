class Card:
    """Represents a standard playing card"""
    def __init__(self, suit=0, rank=2):
        self.suit = suit
        self.rank = rank

    def __lt__(self, other):
        t1 = self.suit, self.rank
        t2 = other.suit, other.rank
        return t1 < t2

    def __str__(self):
        return '%s of %s' % (Card.rank_names[self.rank], \
            Card.suit_name[self.suit])

    suit_name = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
    rank_names = [None, 'Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
