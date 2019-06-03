class P:
	a=10

	def __init__(self):
		self.b=20

	def m1(self):
		print('Parent class Instance method')

	@staticmethod
	def m2():
		print('Parent class Static method')

	@classmethod
	def m3(cls):
		print('Parent class class method')

class C(P):
	a=30
	def m4(self):
		print('Accessing Parent class members')
		print(super().a) #Only static variables can be accessed using super()
		super().m2()     #To access instance variables of parent class,use self
		super().m1()
		super().m3()

c=C()
c.m4()