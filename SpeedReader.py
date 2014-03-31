import os
import time

Text = raw_input("Please enter the text you wish to use: ")


PText = Text.split(" ")
clear = lambda: os.system('clear')
for word in PText:
	time.sleep(.2)
	clear()
	print word
