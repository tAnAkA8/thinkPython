class Card:
    """Represents a standard playing card"""
    def __init__(self, suit=0, rank=2):
        self.suit = suit
        self.rank = rank

queen_of_diamonds = Card(1, 12)
print(queen_of_diamonds.suit)
print(queen_of_diamonds.rank)