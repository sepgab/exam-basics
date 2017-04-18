# Create a Card class, that has a color and a value
# Create a constructor for setting those values
# Card should be represented as string in this format:
# 9 Hearts
# Jack Diamonds
# Create a Deck class, that has a list of cards in it
# Create a constructor that takes a whole number as parameter
# The constructor should fill the list with the number of different cards using at least 4 different colors (except if the number given is smaller than four, than all cards should have different colors)
# We should be able to shuffle the deck, which randomly orders the cards
# We should be able to draw the top card which returns the drawn card and also removes it from the deck
# Deck should be represented as string in this format:
# 12 cards -  3 Clubs, 3 Diamonds, 3 Hearts, 3 Spades
# deck = Deck(12)
# print(deck)
# Should print out:
# 12 cards -  3 Clubs, 3 Diamonds, 3 Hearts, 3 Spades
# top_card = deck.draw()
# print(top_card)
# print(deck)
# Should print out:
# Queen Spades
# 11 cards - 3 Clubs, 3 Diamonds, 3 Hearts, 2 Spades

import random

list_of_colors = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
list_of_values = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']

class Card():

    def __init__(self):
        self.color = random.choice(list_of_colors)
        self.value = random.choice(list_of_values)
        self.card = str(self.value) + ' ' + str(self.color)
        return self.card

class Deck():

    def __init__(self, number_of_cards):
        self.number_of_cards = int(number_of_cards)
        self.card_to_add = None
        self.list_of_cards = []
        self.counter_cards = 0
        while self.counter_cards < self.number_of_cards:
            self.card_to_add = Card()
            if self.card_to_add not in self.list_of_cards:
                self.list_of_cards.append(card_to_add)
                self.counter_cards += 1

deck = Deck(12)

print(deck)
