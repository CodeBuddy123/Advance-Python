import time

class Test:
	def __init__(self):
		print('object intialization')

	def __del__(self):
		print('Fullfilling Last wish and performing cleanup activity')

t1=Test()
t2=t1
t3=t2    #object has three ref var t1 t2 t3

del t1
time.sleep(5)
print('Object not destroyed after deleting t1')

del t2
time.sleep(5)
print('Object not destroyed after deleting t2')
print('Trying to delete last variable')
del t3 #when this statement is being executed,destructor is executed before killing the Test class object
