class Book:
	def __init__(self,pages):
		self.pages=pages

	def __add__(self,other):    #this method is called for every + operation
		return Book(self.pages+other.pages)

	def __str__(self):         #this method returns no of pages as string
		return str(self.pages)

b1=Book(100)
b2=Book(200)
b3=Book(300)
b4=Book(50)         #__str__ method of object class, can be overridden to print meaningful string rep to object
print(b1+b2+b3+b4)#print(Book(650))---> if we try to print object ref, __str__ method is called