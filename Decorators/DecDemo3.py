
def smart_division(func):
	def inner(a,b):
		print('We are dividing',a,'with',b)
		if b==0:
			print('Sorry division not possible')
			return
		else:
			return func(a,b)
	return inner


@smart_division
def divison(a,b):
	return a/b

print(divison(10,2))
print(divison(20,0))