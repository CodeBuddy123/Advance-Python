class Employee:
	def __init__(self,salary):
		self.salary=salary

	def __add__(self,other):
		return self.salary+other.salary

	def __lt__(self,other):
		return self.salary<other.salary

	def __le__(self,other):
		return self.salary<=other.salary

	def __gt__(self,other):
		return self.salary>other.salary

	def __ge__(self,other):
		return self.salary>=other.salary

e1=Employee(4000)
e2=Employee(5000)
print(e1+e2)
print(e1<e2)
print(e1>e2)
print(e1<=e2)
print(e1>=e2)