#operator overloading is implemented by using magic methods

class Book:
	def __init__(self,pages):
		self.pages=pages

	def __add__(self,other):  #corresponding magic method for + operator is __add__
		return self.pages+other.pages


b1=Book(100)
b2=Book(200)
print(b1+b2) #two book objects can be added if we implement magic method