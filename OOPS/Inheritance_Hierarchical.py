
#More than one class having same parent
#Here B and C have common parent A
class A:
	def m1(self):
		print('A class method')

class B(A):
	def m2(self):
		print('B class method')

class C(A):
	def m3(self):
		print('C class method')

c=C()
c.m3()
c.m1()

print()
b=B()
b.m2()
b.m1()