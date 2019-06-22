#preparing customized log handler to overcome the root handler shortcomings

import logging

logger=logging.getLogger('demoLogger')           #creating logger object
logger.setLevel(logging.INFO)                    #setting the logger level

consoleHandler=logging.StreamHandler()           #creating handler object

formatter=logging.Formatter('%(asctime)s-%(name)s-%(levelname)s:%(message)s',datefmt='%d/%m/%Y %H:%M:%S')#creating formatter object

consoleHandler.setFormatter(formatter)           #adding formatter object to handler object

logger.addHandler(consoleHandler)                #adding handler object to logger object

logger.debug('debug message')
logger.info('info message')
logger.warning('warning message')                 #adding logger messages to logger object
logger.error('error message')
logger.critical('critical message')
 

