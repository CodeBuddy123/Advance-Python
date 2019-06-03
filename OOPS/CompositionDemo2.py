class Engine:
	a=20

	def __init__(self):
		self.b=20

	def m1(self):
		print('Engine specific functionality')

class Car:
	def __init__(self):
		self.engine=Engine()

	def m2(self):
		print('Car using engine functionality')
		print(self.engine.a)
		print(self.engine.b)
		self.engine.m1()

c=Car()
c.m2()