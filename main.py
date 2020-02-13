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
def draw_card(deck, hand):
	'''
	Draws a card from a deck and returns a hand appended with it
	'''
	hand.append(deck.pop())

	return hand


# Core ----------------------------------------------------------------




# Takes a list of tuples as argument and loops over the first index of 
# each tuple, then sums each number at every loop.
def value_hand(hand):
	''' 
	Calculates the score of a hand and returns it
	'''

	card = 0
	result = 0
	for i in range(len(hand)):
		card = hand[i][0]
		if  card == 11 or card == 12 or card == 13:
			result += 10
		elif card == 1 :
			if result >= 11: 
				result += 1
			else :
				result += 11
		else:
			result += card

	return result


# 
def display(dealer_hand, player_hand):
	'''

	'''

	total1 = []
	total2 = []
	output1 = ''
	output2 = ''

	clear()
	for i in range(len(player_hand)):
		total1.append(str(player_hand[i][0]) + player_hand[i][1])
		print(total1)
	




	return None



d = create_deck()
h0 = []
h1 = []
h0 = draw_card(d, h0)
h1 = draw_card(d, h1)
h0 = draw_card(d, h0)
h1 = draw_card(d, h1)
h0 = draw_card(d, h0)


display(h0,h1)