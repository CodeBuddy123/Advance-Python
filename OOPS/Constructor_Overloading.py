#method overloading is not applicable in python
#if we declare more than one constructor, the final constructor in the class is only the available con

class Test:

	def __init__(self):
		print('Zero arg constructor')

	def __init__(self,x):
		print('one arg constructor') #final constructor in the sense,when we look from top to bottom

	def __init__(self,x,y):        #only this constructor is considered,the above two are not available
		print('two arg constructor')


#t=Test() gives error as zero arg constructor is not available
#t1=Test(10) gives error as one arg constructor is not available

t2=Test(10,20)  #invokes two arg constructor, which is active constructor in this example
