class Employee:

	def __init__(self,eno,ename,esal,eaddr):

		self.eno=eno
		self.ename=ename
		self.esal=esal
		self.eaddr=eaddr

	def display(self):
		print('Employee Details')
		print('*'*20)
		print('Employee Number:',self.eno)
		print('Employee Name:',self.ename)
		print('Employee Salary:',self.esal)
		print('Employee Address:',self.eaddr)
		print()

e1=Employee(100,'Rajesh',5000,'Hyd')
e2=Employee(200,'Dharmasena',10000,'Srilanka')
e3=Employee(300,'Nigel long',12000,'UK')

e1.display()
e2.display()
e3.display()