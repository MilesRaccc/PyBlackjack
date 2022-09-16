from Entities.Enums import *
import random
import time
import os


clear = lambda: os.system('cls')


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
        suit = ""
        value = str(self.__cardValue.value)

        match self.__cardValue:
            case Value.Ace:
                value = "A"
            case Value.Jack:
                value = "J"
            case Value.Queen:
                value = "Q"
            case Value.King:
                value = "K"
            case _:
                pass

        match self.__cardSuit:
            case Suit.Hearts:
                suit = "♥"
            case Suit.Diamonds:
                suit = "♦"
            case Suit.Clubs:
                suit = "♣"
            case Suit.Spades:
                suit = "♠"
            case _:
                pass

        return value + " of " + suit

    def get_game_value(self):
        tens = [Value.Ten, Value.Jack, Value.Queen, Value.King]

        if self.__cardValue == Value.Ace:
            return 11
        elif self.__cardValue in tens:
            return 10
        else:
            return int(self.__cardValue)


class Deck:

    def __init__(self):
        self.content = list()
        for suit in Suit:
            for value in Value:
                self.content.append(Card(value, suit))


class Hand:
    def __init__(self, deck=None):
        self.handContent = list()
        if deck is not None:
            counter = 0
            while counter < 2:
                counter += 1
                self.hit(deck)

    def hit(self, deck):
        rnd_card = deck.content.pop(random.randint(0, len(deck.content) - 1))
        self.handContent.append(rnd_card)

    def get_total_value(self):
        total_value = 0
        for card in self.handContent:
            total_value += card.get_game_value()
            if card.value == Value.Ace and total_value > 21:
                total_value -= 10
        return total_value


class PlayerHand(Hand):
    __handLost = False

    @property
    def hand_lost(self):
        return self.__handLost

    @hand_lost.setter
    def hand_lost(self, hand_lost):
        self.__handLost = hand_lost

    def __init__(self, deck=None, splitted_hand=None):
        super().__init__(deck)
        if splitted_hand is not None:
            split_card = splitted_hand.handContent.pop()
            self.handContent.append(split_card)

    def player_turn(self, deck, player_set, ai_hand):
        q = False
        stand = False

        while True:
            # clear()
            print("Dealer's Hand:\n", str(ai_hand) + "\n")
            print("Your Hand:")

            for player_hand in player_set:
                print(str(player_hand) + "\n")

            if self.get_total_value() > 21:
                self.__handLost = True
                print("Overdraw! Good luck next time. :З")
                break
            elif self.get_total_value() == 21:
                print("BLACKJACK!")
                input("Press any key to continue.\n")
                break

            resp = input("Input Action: (H - Hit, D - Stand, S - split, Q - quit)\n")

            match resp.split():
                case ["Q"]:
                    q = True
                case ["H"]:
                    self.hit(deck)
                case ["D"]:
                    stand = True
                case ["S"]:
                    if not self.able_to_split():
                        print("You can only split if both cards in hand have same value on the first turn!")
                        time.sleep(3)
                    elif len(self.handContent) > 2:
                        print("You can't split on the second turn!")
                        time.sleep(3)
                    elif len(player_set) > 1:
                        print("You already used split this game!")
                        time.sleep(3)
                    else:
                        second_hand = self.split(deck)
                        player_set.append(second_hand)
                case _:
                    print("Correct command not found.")

            if q or stand:
                break

        return q

    def able_to_split(self):
        return self.handContent[0].value == self.handContent[1].value

    def split(self, deck):
        split_hand = PlayerHand(splitted_hand=self)
        self.hit(deck)
        split_hand.hit(deck)
        return split_hand

    def __str__(self):
        words = list()

        for card in self.handContent:
            words.append(str(card))

        words.append("Total Cards Value of " + str(self.get_total_value()))
        result = "\n".join(words)
        return result


class AiHand(Hand):
    __ai_first_hand = True

    def __init__(self, deck=None):
        super().__init__(deck)

    def ai_console_output(self, player_set):
        # clear()
        print(
            "Dealer's Hand:\n"
            f"{str(self)}\n\n"
            "Your Hand:")

        for player_hand in player_set:
            print(str(player_hand) + "\n")
            if self.get_total_value() == player_hand.get_total_value():
                print("Draw! Better than losing though. :)")
                player_hand.hand_lost = True
            elif self.get_total_value() > 21:
                print("Dealer overdrawn! You won! :D")
            elif self.get_total_value() == 21:
                print("Dealer got Blackjack. Tough luck, bro. :C")
            elif self.get_total_value() > player_hand.get_total_value():
                print("Dealer is closer to 21 than you. You lost. :<")
            elif player_hand.get_total_value() > 21:
                print("Overdraw! Good luck next time. :З")
        time.sleep(3)

    def ai_open_hand(self):
        self.__ai_first_hand = False

    def ai_win_conditions(self, player_set):
        biggest_card_value = 0

        for player_hand in player_set:
            hand_value = player_hand.get_total_value()
            if 22 > hand_value > biggest_card_value:
                biggest_card_value = hand_value

        return biggest_card_value == 0 or (biggest_card_value <= self.get_total_value() < 22)

    def __str__(self):
        words = list()

        for card in self.handContent:
            if self.__ai_first_hand and len(words) > 0:
                words.append("--------")
            else:
                words.append(str(card))

        if not self.__ai_first_hand:
            words.append("Total Cards Value of " + str(self.get_total_value()))

        result = "\n".join(words)
        return result
