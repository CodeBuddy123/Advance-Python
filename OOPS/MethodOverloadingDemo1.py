
#Method overloading is not available in python
#if we declare methods with same name and different param,only latest method is considered
#old method is not available inside the program
class Test:
	def m1(self):
		print('zero arg method') #old method is not available

	def m1(self,x):
		print('one arg method') #only this method is considered

t=Test()
#t.m1() gives error as there is no zero arg method
t.m1(20)