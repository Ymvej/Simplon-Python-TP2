# Init

import os




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


