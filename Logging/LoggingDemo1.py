'''
Logging Levels in Python
1)CRITICAL LEVEL=50
2)ERROR    LEVEL=40
3)WARNING  LEVEL=30
4)INFO     LEVEL=20
5)DEBUG    LEVEL=10
'''
import logging
logging.basicConfig(filename='log20062019.txt',level=logging.WARNING) #it stores warning messages and higher level messages to warning level in mentioned log file

logging.debug('Debug message')
logging.info('info message')        #writing messages to log file 
logging.warning('Warning message')
logging.error('Error message')
logging.critical('Critical message')

print('logging demo')