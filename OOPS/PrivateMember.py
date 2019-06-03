#Private members are available only in the class they are declared

class Test:
	__a=20

	def __init__(self):
		self.__b=30

t=Test()
#print(t.__a)  Not available directly outside the class so it gives error
#print(t.__b)

print(t.__dict__)  #gives dictionary of instance variables of the class 
print(Test.__dict__) #gives dictionary of static variables of the class

print() 
print(t._Test__b)      #Indirectly accessing private members outside the class
print(Test._Test__a)   #Indirectly accessing private memebers outside the class