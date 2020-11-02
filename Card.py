# -*- coding: utf-8 -*-
"""
Created on Tue May  5 12:45:02 2020

@author: santhilata

create deck of cards class

Create a deck of cards class. Internally, the deck of cards should use another class, a card class. Your requirements are:

    The Deck class should have a deal method to deal a single card from the deck
    After a card is dealt, it is removed from the deck.
    There should be a shuffle method which makes sure the deck of cards has all 52 cards and then rearranges them randomly.
    The Card class should have a suit (Hearts, Diamonds, Clubs, Spades) and a value (A,2,3,4,5,6,7,8,9,10,J,Q,K)

"""

class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value
        
    def __repr__(self):
        return ('{} of {}'.format(self.suit, self.value))
        

class Deck:
    
    def __init__(self):
        suits = ['hearts', 'clubs','spades','diamonds']
        values = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']
        self.cards = [Card(suit, value) for suit in suits for value in values]

    def __repr__(self):
		return ("Cards remaining in deck: {}".format(len(self.cards)))


    def shuffle(self):
        if (len(self.cards) <52):
            raise ValueError('Need 52 cards')
            
        shuffle(self.cards)
        return self
    
    def deal(self):
        if len(self.cards) == 0:
			raise ValueError("All cards have been dealt")
		return self.cards.pop()
    
    