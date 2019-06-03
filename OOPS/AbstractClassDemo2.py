from abc import *

class Parent(ABC):
	@abstractmethod
	def m1(self):
		pass
	@abstractmethod
	def m2(self):
		pass

class C1(Parent):       #one of the child class has one abstract method imp
	def m1(self):
		print('m1 implementation')

class C2(C1):           #next childclass has m2 abstract method implm
	def m2(self):
		print('m2 implementation')

c=C2() #Object can be only created to this childclass bt not to C1 class as its incomplete
c.m1()
c.m2()

#c1=C1()TypeError: Can't instantiate abstract class C1 with abstract methods m2
#c1.m1()