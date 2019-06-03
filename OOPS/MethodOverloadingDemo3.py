#default arg method serving the purpose of method overloading

class Test:
	def sum(self,a=None,b=None,c=None):

		if a!=None and b!=None and c!=None:
			print('The sum of three args is',a+b+c)
			

		elif a!=None and b!=None:
			print('The sum of two args is:',a+b)

		elif a!=None:
			print('The sum of one arg is:',a)
		else:
			print('No arg is passed')
t=Test()
t.sum()
t.sum(10)
t.sum(10,20)       #we are able to pass 0,1,2,3 no of args to same method
t.sum(20,30,40)