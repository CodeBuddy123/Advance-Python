#deletion can be done using del keyword

class Test:
	def __init__(self):
		self.a=10
		self.b=20
		self.c=30

	def foo(self):
		del self.c

t=Test()
del t.b
print(t.__dict__)