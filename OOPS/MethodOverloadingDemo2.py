#var arg method serving the purpose of method overloading

def sum(*numbers):  #var arg method takes any no of args.
	sum=0
	for number in numbers:
		sum=sum+number
	print('The sum of numbers is :',sum)

sum(10,20,30)
sum(20,10,40,50,78) #different no of args are passed to sum method
sum(1,2,4,5,6,4,12,1,1,3,3)