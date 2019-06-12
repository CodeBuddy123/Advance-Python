#a function can return a function

def outer():
	print('Outer function execution')

	def inner():
		print('Inner function execution')

	return inner #outer function returning inner function
f1=outer()       #catching the return value in f1
f1()             #using f1,calling the returned function inner