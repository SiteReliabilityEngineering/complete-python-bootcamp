# -*- coding: utf-8 -*-
# @Date:   14-05-2017
# @Email:  koldo.oteo1@gmail.com
# @Filename: Info.py
# @Last modified time: 20-05-2017


class Player(object):

    def __init__(self, name):
        self.name = name
        self.counter = []
        self.points = 0

    def turn(self):
        return self.name

    def pointsC(self):
        """Here we display the points"""
        return self.points

    def addpoint(self, quantity):
        """We save the points into self.counter"""
        self.quantity = quantity
        self.counter += str(self.quantity)
        self.points += self.quantity
