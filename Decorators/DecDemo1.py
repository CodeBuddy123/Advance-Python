#Decorator is a function which takes function as input and provides enhanced or modified func as output

def decor(func):
	def inner(name):
		if name=='sachin':         #if arg is sachin, functionality is extended with below statements
			print('You are a Great Batsman')
			print('I am your fan',name)
			print('Good Morning Sachin')
		else:
			func(name)         #if other arguments are provided,just execute normal func
	return inner

@decor                         #declaring the decorator to the wish function
def wish(name):
	print('Good Morning',name)


wish('Ravi')
wish('sachin') #when this argument is provided, the output is enhanced