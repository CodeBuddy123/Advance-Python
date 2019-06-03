#__str__ is used to provide meaningful string representation to object ref

class Student:
	def __init__(self,name,marks):
		self.name=name
		self.marks=marks

	def __str__(self):
		return 'Student Name is :{} and marks are:{}'.format(self.name,self.marks)

s1=Student('raj',54)
s2=Student('praveen',87)

print(s1) #trying to print object reference, it calls __str__ method
print(s2)