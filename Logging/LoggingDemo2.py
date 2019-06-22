#formatting the log messages 
#format='%(asctime)s:%(levelname)s:%(message)s'
#default mode is append, default file is console[if log file is not mentioned]
#append mode can be changed using filemode='w',where log info is overridden with new info

import logging
logging.basicConfig(filename='log21062019.txt',level=10,format='%(asctime)s:%(levelname)s:%(message)s')
logging.debug('Debug message')
logging.info('Info message')
logging.warning('warning message')
logging.error('Error message')
logging.critical('critical message')