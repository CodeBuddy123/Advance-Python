#to get the count of ref variables for a particular object
import sys
class Test:
	pass

t1=Test()
t2=t1
t3=t1
t4=t1

print(sys.getrefcount(t1)) #total five-t1,t2,t3,t4 and self. python internally provides self ref var to every object
