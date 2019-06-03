#constructor is invoked once per object creation
#In python, we can explicitly invoke the constructor, just like any method

class Test:
	def __init__(self):
		print('constructor invoked')

t1=Test() #object being created and at the same time constructor being invoked

t1.__init__() #object is not created,but just constructor is invoked