#Declaring method inside a method is called Nested Method
#Purpose:-To define method specific repeatedly required functionality

class Test:

	def m1(self):

		def calc(a,b): #taking calc method inside m1 method
			print('Sum of {} and {} is {}'.format(a,b,a+b))
			print('Difference of {} and {} is {}'.format(a,b,a-b))
			print('Product of {} and {} is {}'.format(a,b,a*b))
			print('Division of {} and {} is {}'.format(a,b,a/b))
			print()

		calc(10,30) #repeatedly in m1, we need the calc functionality
		calc(40,50)
		calc(123,56)

t=Test()
t.m1()
