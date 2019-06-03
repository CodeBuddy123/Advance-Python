import time

class Test:
	def __init__(self):
		print('object intialization')

	def __del__(self):
		print('Fullfilling Last wish and performing cleanup activity')

t=Test()
time.sleep(5)
t=None
time.sleep(5)
print('end of application')