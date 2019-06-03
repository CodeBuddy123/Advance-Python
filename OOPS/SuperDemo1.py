#super() method is used to access parent class constructor,var,methods from childclass

class Person:
	def __init__(self,name,age):
		self.name=name
		self.age=age

	def display(self):
		print('Person Name:',self.name)
		print('Person age:',self.age)


class Student(Person):
	def __init__(self,name,age,rollno,marks):
		super().__init__(name,age) #This will call superclass constructor
		self.rollno=rollno
		self.marks=marks

	def display(self):
		super().display()          #Accessing superclass method display using super()
		print('Student rollno:',self.rollno)
		print('Student Marks:',self.marks)

s=Student('Raj',23,11,87) #creating child class object
s.display()