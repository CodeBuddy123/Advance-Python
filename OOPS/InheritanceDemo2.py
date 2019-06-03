class Parent:
	a=10
	def __init__(self):
		self.b=20

	def m1(self):
		print('Parent class method')

class Child(Parent):
	c=30

	def __init__(self):
		super().__init__() #this line invokes the parent class constructor
		self.d=90

	def m2(self):
		print('Child class method')

c=Child() #Child object is created,calls the constructor
print(c.a,c.b,c.c,c.d)
c.m1()
c.m2()

