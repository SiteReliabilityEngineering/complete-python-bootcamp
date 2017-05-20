# -*- coding: utf-8 -*-
"""
Created on Mon May 08 20:33:12 2017

@author: koteo
"""


class Money(object):

    def __init__(self, name, balance=0.0):
        """We inicialize the class with the name and the balance"""
        self.name = name
        self.balance = balance

    def win_mon(self, amount):
        """We add the amount of money that the user won in this game"""
        self.balance += amount
        return self.balance

    def loose_mon(self, amount):
        """we rest the amount of money that the user had lost in this
        game"""
        self.balance -= amount
        return self.balance

    def show_mon(self):
        """Show the total amount of money that the user have """
        return self.balance
