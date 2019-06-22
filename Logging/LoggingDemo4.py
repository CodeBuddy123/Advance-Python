#to print exception message to the log file

import logging
logging.basicConfig(filename='log_exception.txt',level=logging.INFO,format='%(asctime)s:%(levelname)s:%(message)s')

logging.info('Request Received')

try:
	a=int(input('Enter the first number:'))
	b=int(input('Enter the second number:'))
	print(a/b)

except ZeroDivisionError as msg:
	print('cannot divide with zero')
	logging.exception(msg)

except ValueError as msg:
	print('Please provide int values only')
	logging.exception(msg)

logging.info('Request Processing completed')