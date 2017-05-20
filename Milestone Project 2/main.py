#
# -*- coding: utf-8 -*-
# @Date:   14-05-2017
# @Email:  koldo.oteo1@gmail.com
# @Filename: main.py
# @Last modified time: 15-05-2017
from Cards import *
from Board import *
from ClassMoney import *
from Info import *

game = True

while game:

    name = raw_input('Please input the name of the player: ')
    game_on = True

    while game_on:
        a = Info(name)
        b = Cards()

        c1 = b.rand_card()
        b.mod_card(c1)
        point = int(Cards.cards_values[c1])
        a.addpoint(point)
        print "Your card is %s with %s points" % (c1, Cards.cards_values[c1])
        print "You have a Total of %s points"

        c2 = b.rand_card()
        b.mod_card(c2)
        point = int(Cards.cards_values[c2])
        a.addpoint(point)
        totpoints = a.pointsC()
        print "Your card is %s with %s points" % (c2, Cards.cards_values[c2])
        print "You have a Total points of: %i" % (totpoints)

        game_on = False
