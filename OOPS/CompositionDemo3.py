class X:
	a=10
	def __init__(self):
		self.b=20

	def m1(self):
		print('m1() method of X class')

class Y:
	c=30
	def __init__(self):
		self.d=40
	def m2(self):
		print('m2() method of Y class')

	def m3(self):
		 x1=X()
		 print('X class members')
		 print(x1.a)
		 print(x1.b)
		 x1.m1()
		 print()
		 print('Y class members')
		 print(self.d)
		 print(self.c)
		 self.m2()

y=Y()
y.m3()