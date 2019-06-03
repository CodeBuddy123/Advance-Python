class Parent:
	def m1(self):
		print('parent class method')

class Child(Parent):
	def m1(self):
		print('Child class method')

c=Child()
c.m1()        #same method being redefined in childclass,with new implementation 