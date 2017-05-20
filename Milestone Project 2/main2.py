#
# -*- coding: utf-8 -*-
# @Date:   20-05-2017
# @Email:  koldo.oteo1@gmail.com
# @Filename: main2.py
# @Last modified time: 20-05-2017
#
from Cards import *
from Board import *
from ClassMoney import *
from Player import *

game = True

while game:

    ask_name = raw_input("Please input your name: ")
    play1 = Player(ask_name)
    play1card = Cards()

    '''First turn of player 1, we get two random cards'''
    card1 = play1card.rand_card()
    play1card.mod_card(card1)
    card2 = pla1card.rand_card()
    play1card.mod_card(card2)

    if play1.points == 21:
        print "BLACKJACK - PLAYER1 WINS!!!!"
        break

    else:
        print "It´s turn for the crupier!!"
        crup = Player('crupier')
        crupcard = Cards()

        '''Now it´s turn to get two cards for the crupier'''
        card3 = crupcard.rand_card()
        crupcard.mod_card(card3)
        card4 = crupcard.rand_card()
        crupcard.mod_card(card4)

        if crup.points == 21:
            print "BLACK JACK - CRUPIER WINS"
            break

        else:
            turn == "PLAYER1"
            answer = None
            while answer:
                choice = raw_input("Would you want to hit (H) or stand (S) ")
                if choice in ["H", "h"]:
                    print 'It´s turn for %s' % (turn)
                    if turn == "PLAYER1":
                        play1card.mod_card(rand_card())
                        if play1.points < 21:
                            print "You have %d points" % (points)
