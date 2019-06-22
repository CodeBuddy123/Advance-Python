#formatting timestamp for log messages
import logging
#logging.basicConfig(filename='log_21062019.txt',level=10,format='%(asctime)s:%(levelname)s:%(message)s',datefmt='%d/%m/%Y %H:%M:%S')#24 hour format
logging.basicConfig(filename='log_21062019.txt',level=10,format='%(asctime)s:%(levelname)s:%(message)s',datefmt='%d/%m/%Y %I:%M:%S %p')#12 hour format
logging.debug('Debug message')
logging.info('Info message')
logging.warning('warning message')
logging.error('Error message')
logging.critical('critical message')