def decor1(func):
	def inner1():
		x=func()          #input function is number()
		return x*x
	return inner1

def decor2(func):
	def inner2():
		x=func()          #input function is inner1,i.e output of decor1
		return x*2
	return inner2

@decor2
@decor1         #declaring more than one decorator
def number():
	return 10

print(number())