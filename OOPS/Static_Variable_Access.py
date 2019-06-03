class Test:
	a=20

	def __init__(self):
		print(self.a)
		print(Test.a)

	def m1(self):
		print(Test.a)
		print(self.a)

	@classmethod
	def m2(cls):
		print(cls.a)
		print(Test.a)

	@staticmethod
	def m3():
		print(Test.a)

t=Test()
t.m1()
t.m2()
t.m3()
print(t.a)
print(Test.a)