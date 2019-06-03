#It can be declared inside constructor and instance methods using self
#It can be declared outside class using object reference

class Test:
	def __init__(self):
		self.a=20 #declaring using constructor

	def m1(self):
		self.b=30 #declaring using instance method

t=Test()
t.c=50            #declaring outside class
print(t.__dict__) #gives a dictionary with properties and their values as key-value pair
t.m1()            #when this method is invoked, b variable is declared   
print(t.__dict__)