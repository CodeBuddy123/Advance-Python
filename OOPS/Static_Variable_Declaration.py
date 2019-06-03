class Test:
	'''This is an example to show Static variables declaration'''
	a=10
	def __init__(self):
		Test.b=20

	def m1(self):
		Test.c=30

	@classmethod
	def m2(cls):
		cls.d=40
		Test.e=50
	@staticmethod
	def m3():
		Test.f=60

#print(Test.__dict__) #lists out all the static variables. at this point, only a
t=Test()             #con invoked

#print(Test.__dict__) #a,b 

t.m1()
#print(Test.__dict__)#a,b,c

t.m2()
#print(Test.__dict__)#a,b,c,d,e

t.m3()
#print(Test.__dict__)#a,b,c,d,e,f

Test.g=70 #declaring static variable
print(Test.__dict__)  #a,b,c,d,e,f,g

