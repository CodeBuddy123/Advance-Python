#program to demonstrate usage of Class in python

class Student:          
	def __init__(self,name,age,address):  #self has to be first argument to the con and instance methods
		self.age=age         
		self.address=address              #copying values from local variables to class level variables
		self.name=name

	def talk(self):          #this is a method,which shows the behaviour of student
		print('My Details')
		print('*'*20)
		print('My name is:',self.name)
		print('My Age is:',self.age)
		print('My Place is:',self.address)

s1=Student('Raghu',21,'Pune') #first instance of class,where a class can have any number of objects
s1.talk()

print()

s2=Student('Kumar',18,'japan') #second instance or object of class
s2.talk()
