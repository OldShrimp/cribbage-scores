import itertools

class Card:
    def __init__(self, name, number, value, suit):
        self.name = name
        self.number = number
        self.value = value
        self.suit = suit


class CribbageCounter:
    def __init__(self):
        pass
    
    def count_runs(self, hand: list[Card]) -> int:
        cards = [0] * 13
        for card in hand:
            cards[card.number] += 1
        points = 0
        first = last = 0
        while last < len(cards):
            if cards[first] == 0:
                first += 1
                last = first + 1 
            else:
                while cards[last] != 0 and last < len(cards):
                    last += 1
                if last - first > 2:
                    subtotal = last - first
                    for multiplier in cards[first:last]:
                        subtotal *= multiplier
                    points += subtotal
                first = last
        return points
    
    def count_fifteens(self, hand: list[Card]) -> int:
        values = [0] * 10
        for card in hand:
            values[card.value] += 1
    
    def count_flushes(self, hand: list[Card]) -> int:
        for card in hand[1:]:
            if card.suit != hand[0].suit:
                return 0
        return len(hand)
    
    def count_hand(self, hand: list[Card]) -> int:
        hand.sort()
        total = self.count_runs(hand=hand)
        total += self.count_fifteens(hand=hand)
        total += self.count_flushes(hand=hand)
        
        return total


if __name__ == "__main__":
    print('hi')