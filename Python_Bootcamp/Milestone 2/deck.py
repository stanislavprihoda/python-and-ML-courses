import card
import random


class Deck:
    values = ['Ace', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
    colors = ['Clubs', 'Diamonds', 'Hearts', 'Spades']

    def __init__(self):
        full_deck = [card.Card(value, color) for value in Deck.values for color in Deck.colors]
        self.full_deck = full_deck

    def get_full_deck(self):
        return self.full_deck

    def get_random_card(self):
        rnd_number = random.randint(0, len(self.full_deck)-1)
        card_for_removal = self.full_deck[rnd_number]
        return self.full_deck.pop(self.full_deck.index(card_for_removal))
