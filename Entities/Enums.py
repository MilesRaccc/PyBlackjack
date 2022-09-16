import enum


class Value(enum.IntEnum):
    Ace = 1,
    Two = 2,
    Three = 3,
    Four = 4,
    Five = 5,
    Six = 6,
    Seven = 7,
    Eight = 8,
    Nine = 9,
    Ten = 10,
    Jack = 11,
    Queen = 12,
    King = 13


class Suit(enum.IntEnum):
    Hearts = 0,
    Diamonds = 20,
    Spades = 40,
    Clubs = 80
