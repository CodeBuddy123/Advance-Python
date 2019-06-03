#program to demonstrate usage of Class in python

class Student:          #class is a blueprint or model,which describes about an entity

	def __init__(self):  #self is a python provided variable, which refers to current object
		self.name='Ashish'
		self.age=24         #This method is called constructor,used to initialize instance variables
		self.address='Hyd'  #variables indicate the properties of Student

	def talk(self):          #this is a method,which shows the behaviour of student
		print('My Details')
		print('*'*20)
		print('My name is:',self.name)
		print('My Age is:',self.age)
		print('My Place is:',self.address)

s1=Student() #creating object
s1.talk()    #using ref_var to access method of Student class
print(s1.name)
print(s1.age) #using ref_var to access properties of Student class
print(s1.address)