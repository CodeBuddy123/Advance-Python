#Generator is a function used to generate seq of values without allocation of memory

def mygen():
	yield 'A'
	yield 'B'
	yield 'C'
	yield 'D'

g=mygen()
'''print(next(g))
print(next(g))
print(next(g))
print(next(g))   #getting generated val individually
'''

for x in g:
	print(x)
