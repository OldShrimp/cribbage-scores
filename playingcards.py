
class Card:
    def __init__(self, name: str, number: int, value: int, suit: str):
        self.name = name
        self.number = number
        self.value = value
        self.suit = suit
        
    def __str__(self):
        return f"{self.name} of {self.suit}"
        
class Deck:
    def __init__(self):
        self.cards = []
        self.cards.append(Card('Ace', 1, 1, 'Hearts'))
        self.cards.append(Card('Two', 2, 2, 'Hearts'))
        self.cards.append(Card('Three', 3, 3, 'Hearts'))
        self.cards.append(Card('Four', 4, 4, 'Hearts'))
        self.cards.append(Card('Five', 5, 5, 'Hearts'))
        self.cards.append(Card('Six', 6, 6, 'Hearts'))
        self.cards.append(Card('Seven', 7, 7, 'Hearts'))
        self.cards.append(Card('Eight', 8, 8, 'Hearts'))
        self.cards.append(Card('Nine', 9, 9, 'Hearts'))
        self.cards.append(Card('Ten', 10, 10, 'Hearts'))
        self.cards.append(Card('Jack', 11, 10, 'Hearts'))
        self.cards.append(Card('Queen', 12, 10, 'Hearts'))
        self.cards.append(Card('King', 13, 10, 'Hearts'))
        self.cards.append(Card('Ace', 1, 1, 'Clubs'))
        self.cards.append(Card('Two', 2, 2, 'Clubs'))
        self.cards.append(Card('Three', 3, 3, 'Clubs'))
        self.cards.append(Card('Four', 4, 4, 'Clubs'))
        self.cards.append(Card('Five', 5, 5, 'Clubs'))
        self.cards.append(Card('Six', 6, 6, 'Clubs'))
        self.cards.append(Card('Seven', 7, 7, 'Clubs'))
        self.cards.append(Card('Eight', 8, 8, 'Clubs'))
        self.cards.append(Card('Nine', 9, 9, 'Clubs'))
        self.cards.append(Card('Ten', 10, 10, 'Clubs'))
        self.cards.append(Card('Jack', 11, 10, 'Clubs'))
        self.cards.append(Card('Queen', 12, 10, 'Clubs'))
        self.cards.append(Card('King', 13, 10, 'Clubs'))
        self.cards.append(Card('Ace', 1, 1, 'Diamonds'))
        self.cards.append(Card('Two', 2, 2, 'Diamonds'))
        self.cards.append(Card('Three', 3, 3, 'Diamonds'))
        self.cards.append(Card('Four', 4, 4, 'Diamonds'))
        self.cards.append(Card('Five', 5, 5, 'Diamonds'))
        self.cards.append(Card('Six', 6, 6, 'Diamonds'))
        self.cards.append(Card('Seven', 7, 7, 'Diamonds'))
        self.cards.append(Card('Eight', 8, 8, 'Diamonds'))
        self.cards.append(Card('Nine', 9, 9, 'Diamonds'))
        self.cards.append(Card('Ten', 10, 10, 'Diamonds'))
        self.cards.append(Card('Jack', 11, 10, 'Diamonds'))
        self.cards.append(Card('Queen', 12, 10, 'Diamonds'))
        self.cards.append(Card('King', 13, 10, 'Diamonds'))
        self.cards.append(Card('Ace', 1, 1, 'Spades'))
        self.cards.append(Card('Two', 2, 2, 'Spades'))
        self.cards.append(Card('Three', 3, 3, 'Spades'))
        self.cards.append(Card('Four', 4, 4, 'Spades'))
        self.cards.append(Card('Five', 5, 5, 'Spades'))
        self.cards.append(Card('Six', 6, 6, 'Spades'))
        self.cards.append(Card('Seven', 7, 7, 'Spades'))
        self.cards.append(Card('Eight', 8, 8, 'Spades'))
        self.cards.append(Card('Nine', 9, 9, 'Spades'))
        self.cards.append(Card('Ten', 10, 10, 'Spades'))
        self.cards.append(Card('Jack', 11, 10, 'Spades'))
        self.cards.append(Card('Queen', 12, 10, 'Spades'))
        self.cards.append(Card('King', 13, 10, 'Spades'))