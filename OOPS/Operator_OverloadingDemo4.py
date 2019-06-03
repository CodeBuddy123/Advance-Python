class Employee:
	def __init__(self,name,sal_per_day):
		self.name=name
		self.sal_per_day=sal_per_day

	def __mul__(self,others):
		return self.sal_per_day*others.days

class TimeSheet:
	def __init__(self,days):
		self.days=days

	def __mul__(self,others):
		return self.days*others.sal_per_day

e=Employee('Ramu',150)
t=TimeSheet(25)
print('The salary of employee is {}'.format(e*t)) #This line executes mul method in Employee class
print('The salary of employee is {}'.format(t*e)) #This line executes mul method in TimeSheet class
