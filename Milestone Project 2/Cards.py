# -*- coding: utf-8 -*-
"""
Created on Thu May 11 18:50:40 2017

@author: koteo
"""
# We import choice to do a random choice
from random import choice
#


class Cards(object):

    """Don´t modify this dictionary"""
    cards_values = {
            '♠': [1, 11], '♦': [1, 11], '♣': [1, 11], '♥': [1, 11],
            '♠2': 2, '♦2': 2, '♣2': 2, '♥2': 2,
            '♠3': 3, '♦3': 3, '♣3': 3, '♥3': 3,
            '♠4': 4, '♦4': 4, '♣4': 4, '♥4': 4,
            '♠5': 5, '♦5': 5, '♣5': 5, '♥5': 5,
            '♠6': 6, '♦6': 6, '♣6': 6, '♥6': 6,
            '♠7': 7, '♦7': 7, '♣7': 7, '♥7': 7,
            '♠8': 8, '♦8': 8, '♣8': 8, '♥8': 8,
            '♠9': 9, '♦9': 9, '♣9': 9, '♥9': 9,
            '♠10': 10, '♦10': 10, '♣10': 10, '♥10': 10,
            '♠J': 10, '♦J': 10, '♣J': 10, '♥J': 10,
            '♠Q': 10, '♦Q': 10, '♣Q': 10, '♥Q': 10,
            '♠K': 10, '♦K': 10, '♣K': 10, '♥K': 10
            }

    def __init__(self):
        """We initialize a dict called cards_game. This dict is a copy of the
        original dict.By this way, we only modify the copy of the dict"""

        self.cards_game = dict(Cards.cards_values)

    def rand_card(self):
        """We return a card from cards_game list"""

        return choice(self.cards_game.keys())

    def mod_card(self, card):
        """Pop card from cards_game dictionary.By this way I make sure,
        I don´t try to repeat with the same card"""

        self.card = card
        self.cards_game.pop(card)

    def player_cards(self, player):
        """With this method I try to update two dicts: one for the player and one
            for the crupier, where we include the cards of the game"""

        self.player = player
        self.play1c = {}
        self.crupc = {}

        if player == 'PLAYER1':
            self.play1c[self.card] = 0

        elif player == 'CRUPIER':
            self.crupc[self.card] = 0

        else:
            raise "Invalid player %s !!!" % (player)
