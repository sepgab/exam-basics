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



class Card():

    def __init__(self):
        self.list_of_colors = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
        self.list_of_values = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
        self.color = random.choice(self.list_of_colors)
        self.value = random.choice(self.list_of_values)
        self.card = str(self.value) + ' ' + str(self.color)

class Deck():

    def __init__(self, number_of_cards):
        self.number_of_cards = int(number_of_cards)
        self.number_of_clubs = 0
        self.number_of_diamonds = 0
        self.number_of_hearts = 0
        self.number_of_spades = 0
        self.to_add = None
        self.list_of_cards = []
        self.counter_cards = 0
        self.upload()

    def upload(self):
        if self.number_of_cards < 4:
            self.upload_first_4_cards(self.number_of_cards)
        else:
            self.upload_first_4_cards(4)
            while self.counter_cards < self.number_of_cards:
                self.to_add = Card()
                if self.to_add.card not in self.list_of_cards:
                    self.list_of_cards.append(self.to_add.card)
                    self.counter_cards += 1
                    if self.to_add.color == 'Clubs':
                        self.number_of_clubs += 1
                    elif self.to_add.color == 'Diamonds':
                        self.number_of_diamonds += 1
                    elif self.to_add.color == 'Hearts':
                        self.number_of_hearts += 1
                    else:
                        self.number_of_spades += 1

    def upload_first_4_cards(self, number):
        self.number = number
        while self.counter_cards < self.number:
            self.to_add = Card()
            self.add_condition = True
            for card in self.list_of_cards:
                if card.split()[1] == self.to_add.color:
                    self.add_condition = False
            if self.to_add.card not in self.list_of_cards and self.add_condition == True:
                self.list_of_cards.append(self.to_add.card)
                self.counter_cards += 1
                if self.to_add.color == 'Clubs':
                    self.number_of_clubs += 1
                elif self.to_add.color == 'Diamonds':
                    self.number_of_diamonds += 1
                elif self.to_add.color == 'Hearts':
                    self.number_of_hearts += 1
                else:
                    self.number_of_spades += 1

    def shuffle(self):
        self.temp_deck = []
        while self.list_of_cards != []:
            self.random_card = random.choice(self.list_of_cards)
            self.temp_deck.append(self.random_card)
            self.list_of_cards.remove(self.random_card)
        self.list_of_cards = self.temp_deck

    def draw(self):
        self.top_card = self.list_of_cards[0]
        self.list_of_cards = self.list_of_cards[1:]
        self.counter_cards -= 1
        if self.top_card.split()[1] == 'Clubs':
            self.number_of_clubs -= 1
        elif self.top_card.split()[1] == 'Diamonds':
            self.number_of_diamonds -= 1
        elif self.top_card.split()[1] == 'Hearts':
            self.number_of_hearts -= 1
        else:
            self.number_of_spades -= 1
        return self.top_card

    def __str__(self):
        result = ""
        result = str(self.counter_cards) + ' cards -  ' + str(self.number_of_clubs) + ' Clubs, ' + str(self.number_of_diamonds) + ' Diamonds, ' + str(self.number_of_hearts) + ' Hearts, ' + str(self.number_of_spades) + ' Spades'
        return result

deck = Deck(12)

print(deck)

deck.shuffle()

top_card = deck.draw()
print(top_card)
print(deck)
