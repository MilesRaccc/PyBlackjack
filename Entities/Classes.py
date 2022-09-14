from Entities.Enums import *
import random


class Card:

    def __init__(self, card_value, card_suit):
        self.__cardValue = card_value
        self.__cardSuit = card_suit

    @property
    def value(self):
        return self.__cardValue

    @property
    def suit(self):
        return self.__cardSuit

    def __str__(self):
        return f"{self.__cardValue.name} of {self.__cardSuit.name}"

    def getGameValue(self):
        tens = [Value.Ten, Value.Jack, Value.Queen, Value.King]

        if self.__cardValue == Value.Ace:
            return 11
        elif self.__cardValue in tens:
            return 10
        else:
            return self.__cardValue


class Deck:
    content = list()

    def __init__(self):
        # self.content.clear()
        for suit in Suit:
            for value in Value:
                self.content.append(Card(value, suit))


class Hand:
    handContent = list()

    def __init__(self, deck=None):
        if deck is not None:
            counter = 0
            while counter < 2:
                counter += 1
                self.hit(deck)

    def hit(self, deck):
        print(len(deck))
        # rndCard = deck.pop(random.randint(0, len(deck)))
        # self.handContent.append(rndCard)

