from abc import *

class Vehicle(ABC):  #ABC is a class from abc module, this declaration means Vehicle is A.class
	@abstractmethod  #to declare abstract method, use this decorator which belongs to abc module
	def get_no_of_wheels(self):
		pass

class Bus(Vehicle):
	def get_no_of_wheels(self):     #child class is responsible for implementing parent's abstract methods
		return 7

class Car(Vehicle):                 #child class implementing parent's abstract method
	def get_no_of_wheels(self):
		return 4

c=Car()                            #object can only be created if the implementation is complete
print(c.get_no_of_wheels())

b=Bus()
print(b.get_no_of_wheels())
