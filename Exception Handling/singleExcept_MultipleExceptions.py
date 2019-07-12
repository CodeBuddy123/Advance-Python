try:
	num1=int(input('Enter the Numerator:')) #Risky code,prone to Exception
	num2=int(input('Enter the Denominator:'))
	print(num1/num2)	
except (ZeroDivisionError,ValueError) as msg: #msg variable stores exception description
	print('Please enter valid numbers only and exception msg is:',msg)
	