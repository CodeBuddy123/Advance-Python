#Countdown from a number, using generator

def countdown(number):
	while number>0:
		yield number
		number=number-1


values=countdown(100)
for x in values:
	print(x)