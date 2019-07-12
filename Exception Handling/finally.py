#finally block includes clean up code or resource deallocating code
#Case:1 Exception not raised,finally block is executed,Normal termination
'''
try:
	print('try block')
except:
	print('except block')
finally:
	print('finally block')
'''
#Case:2 Exception raised and it is handled, still the finally block gets executed,Normal term
'''
try:
	print('try block')
	print(5/0)
except ZeroDivisionError:
	print('except block')
finally:
	print('Finally block')

'''
#Case-3 Exception raised and is not handled,finally block gets executed,Abnormal termination
'''
try:
	print('try block')
	print(6/0)
except ValueError:
	print('except block')
finally:
	print('finally block')
'''
#Case-4 Finally block doesnt get executed only when PVM shutdown forcefully using os._exit

import os

try:
	print('try block')
	print(7/0)

except ZeroDivisionError:
	os._exit(0)   #forcefully shutting down PVM
	print('except block')
finally:
	print('finally block')   #finally block not executed as already PVM is shutdown