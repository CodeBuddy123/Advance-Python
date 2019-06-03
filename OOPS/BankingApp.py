class Account:
	def __init__(self,name,balance,min_balance):
		self.name=name
		self.balance=balance
		self.min_balance=min_balance

	def deposit(self,amount):
		self.balance=self.balance+amount

	def withdraw(self,amount):
		if self.balance-amount>=self.min_balance:
			self.balance=self.balance-amount
		else:
			print('insufficient funds..')
	def printstatement(self):
		print('Account Balance:',self.balance)


class CurrentAccount(Account):
	def __init__(self,name,balance):
		super().__init__(name,balance,min_balance=-1000)

	def __str__(self):
		return "{}'s CurrentAccount Balance is :{}".format(self.name,self.balance)

class SavingsAccount(Account):
	def __init__(self,name,balance):
		super().__init__(name,balance,min_balance=0)

	def __str__(self):
		return "{}'s SavingsAccount Balance is :{}".format(self.name,self.balance)

c=CurrentAccount('Rajesh',50000)
c.deposit(3000)
print(c)
c.withdraw(5000)
print(c)

print("--------------------------------------------")
s=SavingsAccount('Ashish',20000)
s.deposit(5000)
print(s)
s.withdraw(2500)
print(s)