import os
import time
import magic

def SpeedRead(Text):
	PText = Text.split(" ")
	clear = lambda: os.system('clear')
	for word in PText:
		clear()
		print word
		time.sleep(.2)

Texto = raw_input("Please enter the text you wish to use: ")


rtexto = open(Texto)
Tipo = magic.from_file(Texto)
print Tipo
rtipo = Tipo.split(",")

if rtipo[0] == "ASCII text":
	for line in rtexto:
		SpeedRead(line)
else:
	print "That's not a text file!"





