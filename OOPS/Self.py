#to show self variable refers to current class object

class Test:
	def foo(self):
		print(id(self)) #2375864291736
     

t1=Test()
t1.foo()
print(id(t1)) #2375864291736  Both variables have same address,which means they refer to same object