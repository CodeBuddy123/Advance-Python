class A:
	def m1(self):
		print('A class method')

class B(A):
	def m2(self):
		print('B class method')

class C(B):
	def m3(self):
		print('C class method')


c=C()
c.m1()
c.m2()
c.m3()