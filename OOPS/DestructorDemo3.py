import time

class Test:
	def __init__(self):
		print('object intialization')

	def __del__(self):
		print('Fullfilling Last wish and performing cleanup activity')


list=[Test(),Test(),Test()]
del list
time.sleep(5)
print('end of the application')