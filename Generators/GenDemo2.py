#Generating first n natural numbers using Generator

def firstn(number):
	n=1
	while n<=number:
		yield n
		n=n+1


g=firstn(6)
for x in g:
	print(x)