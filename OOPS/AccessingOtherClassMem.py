#Accesing one class members in another class

class Employee:
	def __init__(self,eno,ename,esal):
		self.eno=eno
		self.ename=ename
		self.esal=esal

	def display(self):
		print('Employee Details')
		print('*'*25)
		print('Employee No:',self.eno)
		print('Employee Name:',self.ename)
		print('Emploee Salary:',self.esal)
class Test:
	def modify(emp):
		emp.esal=emp.esal+2000
		emp.display()

e=Employee(100,'Ashish',7000)
Test.modify(e)