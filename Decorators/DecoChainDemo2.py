def decor1(func):
	def inner1(name):
		print('First decor execution')
		func(name)
	return inner1

def decor2(func):
	def inner2(name):
		print('Second decor execution')
		func(name)
	return inner2

@decor2
@decor1
def wish(name):
	print('Hello',name,'Good morning')

wish('Ramu')