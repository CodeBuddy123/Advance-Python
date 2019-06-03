#Protected members are available within the class and from outside they are available in childclasses
class Test:
	_a=20 #it is just a convention but python is not strict about its implementation

	def __init__(self):
		self._b=40

t=Test()
print(Test._a) #outside the class we are accessing bt not in childclass
print(t._b)  #Syntactically it is not implemented by python, so there is no error
