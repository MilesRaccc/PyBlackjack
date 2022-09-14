import enum


class Value(enum.Enum):
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


class Suit(enum.Enum):
    Hearts = 0,
    Diamonds = 1,
    Spades = 2,
    Clubs = 3