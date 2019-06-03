#A class having more than one parent, is called multiple inheritance
#Python supports multiple inheritance unlike in java
#The method resolution takes place by giving highest priority to left parent than right ones

class A:
	def m2(self):
		print('A class method')

class B:
	def m2(self):
		print('B class method')

class C(B,A): #B and A contains same m2 method, the priority is given to left parent in declaration (B,A)
	def m3(self):
		print('C class method')

c=C()
c.m2()  #when m2 method is called, the output is of B class method as B is having higher priority than A
c.m3()