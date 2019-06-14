#fibonacci  numbers below 1000 using generator function

def fib():
	a,b=0,1
	while True:
		yield a
		a,b=b,a+b


for f in fib():
	if(f<1000):
		print(f)
	else:
		break