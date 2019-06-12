#we can call function either by using decorator or without by following way

def decor(func):

	def inner(name):
		if name=='sunny':
			print('Hello sunny Bad morning')
		else:
			func(name)

	return inner

def wish(name):
	print('Hello',name,'Good morning')

wish('ramesh') #decorator will not be executed
wish('sunny')  #decorator will not be executed


dec_func=decor(wish)
dec_func('ramesh')             #decorator will be executed
dec_func('sunny')              #decorator will be executed
