class P:
	a=20
	def __init__(self):
		self.b=30

	def m1(self):
		print('Parent-m1()')

	@staticmethod
	def m2():
		print('Parent-m2()')

	@classmethod
	def m3(cls):
		print('Parent-m3()')

class C(P): #syntax for inheritance --> childclassName(parentclassname)
	pass

c=C()
c.m1()
c.m2()        #All the methods and properties of P class are available to C class
c.m3()
print(c.a)
print(c.b)