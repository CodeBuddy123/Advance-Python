#by default all variables are public, can be accessed within the class, outside the class
#or from the other modules

class Test:
	a=20
	def __init__(self):
		self.x=30
	def m1(self):
		print(Test.a) #Accessing within the class
		print(self.a)

t=Test()
print(Test.a) #Accessing outside the class
print(t.x)
t.m1()