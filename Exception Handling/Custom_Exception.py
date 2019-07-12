#to raise our own exception, we can use custom exceptions as per our business logic
#In the belong example, my matrimonial site allows age >18 and <60 to get registered

class TooYoungException(Exception):  #this class is reponsible for creating Exception object for TooYoungException
	def __init__(self,msg):          #constructor
		self.msg=msg
	

class TooOldException(Exception):   #this class is reponsible for creating Exception object for TooOldException
	def __init__(self,msg):
		self.msg=msg

print('Welcome to Ashish Matrimonial website')
age=int(input('Enter the age:'))

if age<18:
	raise TooYoungException('You are too young for a marriage.Grow your beard!')

elif age>60:
	raise TooOldException('You are too old for a marriage.Happy Retirement Life!')

else:
	print('You will get Match Details soon by Email.')