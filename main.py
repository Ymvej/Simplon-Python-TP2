# Init

import os
import itertools
import random




# Basic functions -----------------------------------------------------




# Uses os to check shell and input the right command.
def clear():
	'''
	Clears the screen
	'''

	if os.name == 'nt':
		os.system('CLS')
	if os.name == 'posix':
		os.system('clear')


# Uses itertool to create a deck from a list of values
def create_deck():
	'''
	Creates a deck and returns it
	'''

	deck = list(itertools.product(
		[1,2,3,4,5,6,7,8,9,10,11,12,13],
		['Spades','Hearts','Diamonds','Clubs']))
	random.shuffle(deck)

	return deck


# Pops a card out of a deck given as argument
def draw_card(deck):
	'''
	Draws a card from a deck and returns it
	'''

	card = deck.pop()
	return card

