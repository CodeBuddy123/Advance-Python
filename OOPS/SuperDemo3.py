class A:
	def m1(self):
		print('A class method')

class B(A):
	def m1(self):
		print(' B class method')

class C(B):
	def m1(self):
		print('C class method')

class D(C):
	def m1(self):
		super(B,self).m1()  #calling particular super classmethod, calls B class super(A) m1()
		print('D class method')
d=D()
d.m1()