import more_itertools
from math import comb
from playingcards import Card, Deck
import random

class CribbageCounter:
    def __init__(self):
        pass
    
    def count_runs(self, hand: list[Card]) -> int:
        cards = [0] * 13
        for card in hand:
            cards[card.number - 1] += 1
        points = 0
        first = last = 0
        while last < len(cards):
            if cards[first] == 0:
                first += 1
                last = first + 1 
            else:
                while last < len(cards) and cards[last] != 0:
                    last += 1
                if last - first > 2:
                    subtotal = last - first
                    for multiplier in cards[first:last]:
                        subtotal *= multiplier
                    points += subtotal
                first = last
        print(f"{points}pts from runs: {cards}")
        return points
    
    def count_fifteens(self, hand: list[Card]) -> int:
        card_values = [card.value for card in hand]
        fifteens = [x for x in more_itertools.powerset(card_values) if sum(x) == 15]
        points = 2 * len(fifteens)
        print(f"{points}pts from fifteens: {fifteens}")
        return points
    
    def count_flushes(self, hand: list[Card]) -> int:
        if len(hand) < 2:
            return len(hand)
        for card in hand[2:]:
            if card.suit != hand[1].suit:
                print("no flush")
                return 0
        flush_size = len(hand)
        if hand[0].suit == hand[1].suit:
            flush_size += 1
        print(f"flush of {flush_size}")
        return flush_size
    
    def count_pairs(self, hand: list[Card]) -> int:
        cards = [0] * 13
        for card in hand:
            cards[card.number - 1] += 1
        cards = [2*comb(card, 2) for card in cards]
        points = sum(cards)
        print(f"{points}pts from pairs: {cards}")
        return points
    
    def count_hand(self, hand: list[Card]) -> int:
        hand.sort(key=lambda card : card.number)
        print(', '.join(map(str, hand)))
        total = self.count_runs(hand=hand)
        total += self.count_fifteens(hand=hand)
        total += self.count_flushes(hand=hand)
        total += self.count_pairs(hand=hand)
        if len(hand) > 1 and len([card for card in hand[1:] if card.number == 11 and card.suit == hand[0].suit]) > 0:
            total += 1
            print("and one for the jack")
        
        return total


if __name__ == "__main__":
    num_hands = 100
    hand_range = 10
    random.seed()
    deck = Deck()
    average_hands = [0] * hand_range
    for i in range(hand_range):
        for j in range(num_hands):
            random.shuffle(deck.cards)
            hand = deck.cards[0:i]
            average_hands[i] += CribbageCounter().count_hand(hand=hand) / num_hands
    print(average_hands)
