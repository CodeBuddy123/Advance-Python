#Generating six letter random name
from random import choice
def namegen():
	alphabets='abcdefghijklmnopqrstuvwxyz'
	name=''
	for i in range(6):
		name=name+choice(alphabets)
	yield name

for x in range(5):  #gen five six letter random words
	for i in namegen():
		print(i)