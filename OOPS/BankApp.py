import sys
import os
class Account:
	'''This is a class to perform banking operations'''
	bank='ASHISH BANK'
	def __init__(self,name,balance=0.0):
		self.name=name
		self.balance=balance

	def deposit(self,amount):
		self.balance=self.balance+amount
		print('Account Balance after Deposit:',self.balance)
		print()

	def withdraw(self,amount):
		if amount>self.balance:
			print('Insufficient funds for Transaction')
			sys.exit()
		self.balance=self.balance-amount
		print('Account Balance after Withdraw:',self.balance)
		print()

print('Welcome to',Account.bank)
name=input('Enter your Name:')

a=Account(name)

while True:
	print('D-Deposit')
	print('W-Withdraw')
	print('E-Exit')

	option=input('Enter your Option for Transaction:').lower()

	if(option=='d'):
		amount=float(input('Enter the amount to be Deposited:'))
		a.deposit(amount)

	elif option=='w':
		while True:
			amount=float(input('Enter the amount to withdraw:'))
			if not(amount>0 and amount%100==0):
				print('Amount must be in multiples of 100')
			else:
				break
		a.withdraw(amount)

	elif option=='e':
		print('Thanks for banking,Have a nice day.')
		#sys.exit()
		os._exit(0)
	else:
		print('Please provide valid option...')