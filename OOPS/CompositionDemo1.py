#Employee has an Account
#Composition can be achieved by using other class  static members using class name
#Instance members of one class can be used in another class by creating object and using mem through ref_Var
class Account:

	def __init__(self,accNo,accName,accType):
		self.accNo=accNo
		self.accName=accName
		self.accType=accType

	def getAccDetails(self):
		print('Account Details')
		print('---------------------')
		print('Account No    :',self.accNo)
		print('Account Name  :',self.accName)
		print('Account Type  :',self.accType)

class Employee:

	def __init__(self,eid,ename,esal,acc):
		self.eid=eid
		self.ename=ename
		self.esal=esal
		self.acc=acc

	def getEmpDetails(self):
		print('Employee Details')
		print('------------------------')
		print('Employee ID     :',self.eid)
		print('Employee Name   :',self.ename)
		print('Employee Salary :',self.esal)
		print()
		self.acc.getAccDetails() #using Account Specific method in Employee class

a=Account('abc123','Ashish','Savings')

emp=Employee('E-111','Ashish',60000,a)

emp.getEmpDetails()