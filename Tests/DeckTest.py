import unittest
from Entities.Classes import *


class SimpleDeckTestCase(unittest.TestCase):
    def setUp(self):
        self.test_deck = Deck()  # add assertion here


class DefaultDeckUniqueTestCase(SimpleDeckTestCase):
    def runTest(self):
        card_list = list(int(card.value + card.suit) for card in self.test_deck.content)
        card_set_list = set(card_list)
        list_len = len(card_set_list)
        assert list_len == 52, 'values not unique'


if __name__ == '__main__':
    unittest.main()
