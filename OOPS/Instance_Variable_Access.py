#Instance variable within a class can be accessed using self
#Instance variable from outside a class,can be accessed using object_Ref

class Test:
	def __init__(self):
		self.a=20
		self.b=30
	

	def foo(self):
		print(self.a) #within a class,accessed using self
		print(self.b)

t=Test()
t.foo()
print(t.a)          #from outside a class,objectref.varname is used
print(t.b)